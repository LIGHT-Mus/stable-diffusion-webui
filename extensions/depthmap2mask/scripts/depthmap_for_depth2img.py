import torch, gc
import cv2
import requests
import os.path
import contextlib
from PIL import Image
from modules.shared import opts, cmd_opts
from modules import processing, images, shared, devices

from torchvision.transforms import Compose
from repositories.midas.midas.dpt_depth import DPTDepthModel
from repositories.midas.midas.midas_net import MidasNet
from repositories.midas.midas.midas_net_custom import MidasNet_small
from repositories.midas.midas.transforms import Resize, NormalizeImage, PrepareForNet

import numpy as np

class SimpleDepthMapGenerator(object):
    def calculate_depth_maps(self,image,img_x,img_y,model_type,invert_depth):
        try:
            def download_file(filename, url):
                print("Downloading midas model weights to %s" % filename)
                with open(filename, 'wb') as fout:
                    response = requests.get(url, stream=True)
                    response.raise_for_status()
                    # Write response data to file
                    for block in response.iter_content(4096):
                        fout.write(block)

            device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
            # model path and name
            model_dir = "./models/midas"
            # create path to model if not present
            os.makedirs(model_dir, exist_ok=True)
            print("Loading midas model weights ..")
            device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

            #"dpt_large"
            if model_type == 0:
                model_path = f"{model_dir}/dpt_large-midas-2f21e586.pt"
                print(model_path)
                if not os.path.exists(model_path):
                    download_file(model_path,"https://github.com/intel-isl/DPT/releases/download/1_0/dpt_large-midas-2f21e586.pt")
                model = DPTDepthModel(
                    path=model_path,
                    backbone="vitl16_384",
                    non_negative=True,
                )
                net_w, net_h = 384, 384
                resize_mode = "minimal"
                normalization = NormalizeImage(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])

            #"dpt_hybrid" / not working at the moment
            # elif model_type == 1:
            #     model_path = f"{model_dir}/dpt_hybrid-midas-501f0c75.pt"
            #     print(model_path)
            #     if not os.path.exists(model_path):
            #         download_file(model_path,"https://github.com/intel-isl/DPT/releases/download/1_0/dpt_hybrid-midas-501f0c75.pt")
            #     model = DPTDepthModel(
            #         path=model_path,
            #         backbone="vitb_rn50_384",
            #         non_negative=True,
            #     )
            #     net_w, net_h = 384, 384
            #     resize_mode="minimal"
            #     normalization = NormalizeImage(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])

            #"midas_v21"
            elif model_type == 1:
                model_path = f"{model_dir}/midas_v21-f6b98070.pt"
                print(model_path)
                if not os.path.exists(model_path):
                    download_file(model_path,"https://github.com/AlexeyAB/MiDaS/releases/download/midas_dpt/midas_v21-f6b98070.pt")
                model = MidasNet(model_path, non_negative=True)
                net_w, net_h = 384, 384
                resize_mode="upper_bound"
                normalization = NormalizeImage(
                    mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]
                )

            #"midas_v21_small"
            elif model_type == 2:
                model_path = f"{model_dir}/midas_v21_small-70d6b9c8.pt"
                print(model_path)
                if not os.path.exists(model_path):
                    download_file(model_path,"https://github.com/AlexeyAB/MiDaS/releases/download/midas_dpt/midas_v21_small-70d6b9c8.pt")
                model = MidasNet_small(model_path, features=64, backbone="efficientnet_lite3", exportable=True, non_negative=True, blocks={'expand': True})
                net_w, net_h = 256, 256
                resize_mode="upper_bound"
                normalization = NormalizeImage(
                    mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]
                )

            # init transform
            transform = Compose(
                [
                    Resize(
                        img_x,
                        img_y,
                        resize_target=None,
                        keep_aspect_ratio=True,
                        ensure_multiple_of=32,
                        resize_method=resize_mode,
                        image_interpolation_method=cv2.INTER_CUBIC,
                    ),
                    normalization,
                    PrepareForNet(),
                ]
            )
            model.eval()
            # optimize
            if device == torch.device("cuda"):
                model = model.to(memory_format=torch.channels_last)
                if not cmd_opts.no_half:
                    model = model.half()
            model.to(device)

            img = cv2.cvtColor(np.asarray(image), cv2.COLOR_BGR2RGB) / 255.0
            img_input = transform({"image": img})["image"]
            precision_scope = torch.autocast if shared.cmd_opts.precision == "autocast" and device == torch.device("cuda") else contextlib.nullcontext
            # compute
            with torch.no_grad(), precision_scope("cuda"):
                sample = torch.from_numpy(img_input).to(device).unsqueeze(0)
                if device == torch.device("cuda"):
                    sample = sample.to(memory_format=torch.channels_last)
                    if not cmd_opts.no_half:
                        sample = sample.half()
                prediction = model.forward(sample)
                prediction = (
                    torch.nn.functional.interpolate(
                        prediction.unsqueeze(1),
                        size=img.shape[:2],
                        mode="bicubic",
                        align_corners=False,
                    )
                    .squeeze()
                    .cpu()
                    .numpy()
                )
            # output
            depth = prediction
            numbytes=2
            depth_min = depth.min()
            depth_max = depth.max()
            max_val = (2**(8*numbytes))-1

            # check output before normalizing and mapping to 16 bit
            if depth_max - depth_min > np.finfo("float").eps:
                out = max_val * (depth - depth_min) / (depth_max - depth_min)
            else:
                out = np.zeros(depth.shape)
            # single channel, 16 bit image
            img_output = out.astype("uint16")

            # # invert depth map
            if invert_depth:
                img_output = cv2.bitwise_not(img_output)

            # three channel, 8 bits per channel image
            img_output2 = np.zeros_like(image)
            img_output2[:,:,0] = img_output / 256.0
            img_output2[:,:,1] = img_output / 256.0
            img_output2[:,:,2] = img_output / 256.0
            img = Image.fromarray(img_output2)
            return img
        except Exception:
            raise
        finally:
            del model
            gc.collect()
            devices.torch_gc()
