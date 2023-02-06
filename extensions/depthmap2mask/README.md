# depthmap2mask

Made as a script for the [AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) repository.


## 💥 Installation 💥

Copy the url of that repository into the extension tab :

![image](https://user-images.githubusercontent.com/15731540/204056273-fc27d1cf-48ac-4dc3-b737-95b4b1efd32e.png)

OR copy that repository in your extension folder :

![image](https://user-images.githubusercontent.com/15731540/203840272-83cccb24-4417-44bc-99df-e45eb5f3360c.png)

You might need to restart the whole UI. Maybe twice.

if you are on colab you can also add this line in a code block before starting the UI/after the installation cells :

    !git clone https://github.com/Extraltodeus/depthmap2mask.git /content/stable-diffusion-webui/extensions/depthmap2mask

## The look

![image](https://user-images.githubusercontent.com/15731540/204043153-09cbffd9-28ac-46be-ad99-fc7f2c8656a3.png)

## What does this extension do?

It creates masks for img2img based on a depth estimation made by [MiDaS](https://github.com/isl-org/MiDaS).

![smallerone](https://user-images.githubusercontent.com/15731540/204043576-5dc02def-29f8-423e-a69e-d392f47d3602.png)![5050](https://user-images.githubusercontent.com/15731540/204043582-ae46d0b8-3c4b-43d5-b669-eaf2659ced14.png)

## Where to find it after installing it?

Go to your img2img tab then select it from the custom scripts list at the bottom.

## Explanations of the different UI elements

- Contrasts cut level

![image](https://user-images.githubusercontent.com/15731540/204043824-6067bd9e-49d6-488b-8f99-47928c31ae46.png)

This slider is **purely optional**.
The depthmap is in levels of gray. Each pixel has a value in between 0 and 255 depending if they are black (0) or white (255). That threshold slider will cut to black every pixel below the selected value and scale from black to white what is above its value.

Or in a more human language, it will give more depth to your depthmaps while removing a lot of information.

Example before/after with the slider's value around 220 and using the MiDaS-Large model:

![00073--1 0- sampler -85-8 1-ac07d41f-20221125174853](https://user-images.githubusercontent.com/15731540/204044001-4e672bbe-4ff8-46ef-ae87-ec3377e7aa37.png)![00074--1 0- sampler -85-8 1-ac07d41f-20221125174934](https://user-images.githubusercontent.com/15731540/204044306-80c77ba3-3b38-4ea6-941c-f6c6006c8b4e.png)

Using the MiDaS small model will give you similar if not more interesting results.

![smallerone](https://user-images.githubusercontent.com/15731540/204043576-5dc02def-29f8-423e-a69e-d392f47d3602.png)![5050](https://user-images.githubusercontent.com/15731540/204043582-ae46d0b8-3c4b-43d5-b669-eaf2659ced14.png)

So that's more of an extra-extra option or a way to make sure that your backgrounds are untouched by using a low value (like 50).

- Match input size/Net width/Net height

![image](https://user-images.githubusercontent.com/15731540/204044819-0618bf27-0692-4a20-922f-73e33822dc6f.png)

Match input size (On by default) will make the depth analysis at the same size as the original image. Better not to touch it unless you are having performance issues.

The sliders below will be the resolution of the analysis if Match input size is turned off.

You can also just use these functionalities to test out different results.

- Misc options

![image](https://user-images.githubusercontent.com/15731540/204045429-778f3084-63ad-421d-ad43-af9a20c49621.png)

- Override options :

    These two options simply overrides the inpainting Masked content method and mask blur. I added these because using "original" for Masked content and Mask Blur at 0 just works better. This saves you the clics needed to switch to the intpaint tab/reupload the image to that tab and select the right options.
    
- MiDaS models :

    I'll let you try what suits your needs the most.
    
- Turn the depthmap into absolute black/white

![image](https://user-images.githubusercontent.com/15731540/204057815-1e7d1d38-2fbb-43a1-bb08-133e574138c2.png)

This option will cut out the background of an image into pure black and make the foreground pure white. Like a clean cut.

### Alpha Cropping

You can also save a version of the input image which has had all the masked content replaced with transparent pixels. This is useful when extracting the subject from the background, so that it can be used in designs.

![Image](https://i.imgur.com/yFX6LyQ.jpeg)

Simply check the "Save alpha mask" option before generating.

## Tips

- Avoid using Euler a or you might get really bad results. Usually DDIM works best.

## Credits/Citation

Thanks to [thygate](https://github.com/thygate) for letting me blatantly copy-paste some of his functions for the depth analysis integration in the webui.

This repository runs with [MiDaS](https://github.com/isl-org/MiDaS).

```
@ARTICLE {Ranftl2022,
    author  = "Ren\'{e} Ranftl and Katrin Lasinger and David Hafner and Konrad Schindler and Vladlen Koltun",
    title   = "Towards Robust Monocular Depth Estimation: Mixing Datasets for Zero-Shot Cross-Dataset Transfer",
    journal = "IEEE Transactions on Pattern Analysis and Machine Intelligence",
    year    = "2022",
    volume  = "44",
    number  = "3"
}
```
```
@article{Ranftl2021,
	author    = {Ren\'{e} Ranftl and Alexey Bochkovskiy and Vladlen Koltun},
	title     = {Vision Transformers for Dense Prediction},
	journal   = {ICCV},
	year      = {2021},
}
```

## Bug reporting

- Please check if similar issues exist before creating a new one.
- Make sure to do a "git pull" from your webui folder in order to have your webui up to date
- Provide as many details as possible when creating a new issue.

## Examples using different MiDaS models and denoising strength
![00056-589874964- sampler -32-7-ac07d41f-20221125174017](https://user-images.githubusercontent.com/15731540/204048931-20b19823-bba9-44be-a4ff-4d3ae65dd120.png)![00064-1584461722- sampler -32-7-ac07d41f-20221125174328](https://user-images.githubusercontent.com/15731540/204048940-fada95f2-fcb0-4cf7-ba0c-6a1fd6b904ea.png)![00100-717650490- sampler -84-8 1-ac07d41f-20221125175700](https://user-images.githubusercontent.com/15731540/204048949-a4faf745-e9b5-437e-870d-be8ea7bd4b5d.png)


<sub>I forgot my settings but in the end it's all pretty easy to guess what you need.</sub>
