# stable-diffusion-webui
stable-diffusion-webui国内定制版

![](screenshot.png)

# #特性
【详细功能展示及图片】(https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Features):
-原有的txt2img和img2img模式
-一键安装并运行脚本(但你仍然必须安装python和git)
——Outpainting
——修复
-颜色草图
-提示矩阵
-稳定扩散升级
-注意，指定文本中模型应该更加注意的部分
穿燕尾服的男人会更注意燕尾服
-一个男人在(燕尾服:1.21)-替代语法
-选择文本并按ctrl+up或ctrl+down自动调整对所选文本的关注(由匿名用户贡献的代码)
—环回，多次执行img2img processing
- X/Y/Z图，一种用不同参数绘制图像的三维图的方法
-文本反转
-有尽可能多的嵌入，你想和使用任何你喜欢的名字为他们
-每个令牌使用不同数量的向量的多个嵌入
-工作与半精度浮点数
-列车嵌入在8GB(也有6GB工作的报告)
-附加标签与:
- GFPGAN，修复面部的神经网络
- CodeFormer，面部恢复工具作为GFPGAN的替代品
- RealESRGAN，神经网络中上层
- ESRGAN，神经网络的上层，有很多第三方模型
- SwinIR和Swin2SR([见这里](https://github.com/AUTOMATIC1111/stable-diffusion-webui/pull/2092))，神经网络的上层
- LDSR，潜扩散超分辨率提升
-调整纵横比选项
-采样方法选择
-调整采样器的eta值(噪音倍增器)
-更先进的噪音设置选项
-随时中断处理
-支持4GB显卡(也报告了2GB工作)
-正确的种子批次
-实时提示令牌长度验证
-生成参数
-用于生成图像的参数与该图像一起保存
-在PNG块为PNG，在EXIF为JPEG
-可以拖动图像到PNG信息选项卡，以恢复生成参数，并自动复制到UI
-可在“设置”中禁用
-拖放图像/文本参数到提示框
-读取生成参数按钮，将提示框中的参数加载到用户界面
—设置页面
从UI运行任意python代码(必须使用——allow-code来启用)
-大多数UI元素的鼠标悬停提示
-可以通过文本配置更改UI元素的默认值/混合/最大/步进值
-平铺支持，一个复选框创建图像，可以平铺像纹理
-进度条和实时图像生成预览
-可以使用单独的神经网络来生成几乎没有VRAM或计算需求的预览
-负提示，一个额外的文本字段，允许您列出您不想在生成的图像中看到的内容
-样式，一种保存部分提示符的方法，以后可以通过下拉菜单轻松应用它们
-变体，一种生成相同图像但具有微小差异的方法
-种子大小调整，一种方法，以产生相同的图像，但略有不同的分辨率
- CLIP询问器，一个试图从图像中猜测提示的按钮
-提示编辑，一种改变提示中期的方法，比如开始做西瓜，中途切换到动漫女孩
—批处理，使用img2img处理一组文件
- Img2img可选，反向欧拉方法的交叉注意控制
-高分辨率修复，一个方便的选项，产生高分辨率的图片在一个点击没有通常的扭曲
-快速重新加载检查点
-检查点合并，一个选项卡，允许您合并最多3个检查点为一个
-[自定义脚本](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Custom-Scripts)与许多扩展从社区
[composial - diffusion](https://energy-based-model.github.io/Compositional-Visual-Generation-with-Composable-Diffusion-Models/)，一种同时使用多个提示的方法
-使用大写的“AND”分隔提示符
-也支持重量提示:“一只猫:1.2和一只狗和一只企鹅:2.2”
-提示符没有符号限制(原来的稳定扩散让你最多使用75个符号)
- DeepDanbooru集成，为动画提示创建danbooru风格的标签
- [xformers](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Xformers)，选择卡的主要速度增加:(在命令行参数中添加——xformers)
-通过扩展:[历史标签](https://github.com/yfszzx/stable-diffusion-webui-images-browser):视图，直接和删除图像方便在UI内
-生成永久选项
-培训标签
-超网络和嵌入式选项
-预处理图像:裁剪，镜像，使用BLIP或deepdanbooru自动标记(用于动画)
-剪辑跳过
——Hypernetworks
洛拉斯(和超网络一样，但更漂亮)
-一个独立的用户界面，你可以选择，预览，嵌入，超网络或洛拉斯添加到您的提示。
-可以从设置界面选择加载不同的VAE
-进度条中的估计完成时间
- - - - - - API
-支持RunwayML专用的[inpainting model](https://github.com/runwayml/stable-diffusion#inpainting-with-stable-diffusion)。
-通过扩展:[美学梯度](https://github.com/AUTOMATIC1111/stable-diffusion-webui-aesthetic-gradients)，一种方法生成图像与特定的美学使用剪辑图像嵌入(实现[https://github.com/vicgalle/stable-diffusion-aesthetic-gradients](https://github.com/vicgalle/stable-diffusion-aesthetic-gradients))
-[稳定扩散2.0](https://github.com/Stability-AI/stablediffusion)支持-参见[wiki](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Features#stable-diffusion-20)的说明
- [Alt-Diffusion](https://arxiv.org/abs/2211.06679)支持-参见[wiki](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Features#alt-diffusion)的说明
-现在没有坏字母了!
—以safetensor格式加载检查点
-简化分辨率限制:生成的图像的分辨率必须是8的倍数，而不是64
-现在有执照了!
-从设置界面重新排列UI中的元素
-

##安装和运行
确保满足所需的[依赖项](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Dependencies)，并遵循[NVidia](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Install-and-Run-on-NVidia-GPUs)(推荐)和[AMD](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Install-and-Run-on-AMD-GPUs) gpu可用的说明。

或者，使用在线服务(如谷歌Colab):

-[网上服务一览表](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Online-Services)

在Windows上自动安装
1. 安装[Python 3.10.6](https://www.python.org/downloads/windows/)，检查“Add Python to PATH”
2. 安装(git) (https://git-scm.com/download/win)。
3.下载stable-diffusion-web存储库，例如运行' git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git '。
4. 将稳定扩散检查点(' model.ckpt ')放置在' models/ stable-diffusion '目录中(参见[dependencies](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Dependencies)以获取它)。
5. 在Windows资源管理器中以普通、非管理员、用户身份运行“web -user.bat”。

##在Linux上自动安装
1. 安装依赖项:
”“bash
# Debian-based:
Sudo apt install wget git python3 python3-venv
#基于红帽的:
Sudo DNF安装wget git python3
# Arch-based:
sudo pacman -S wget git python3
' ' '
2. 在“/home/$(whoami)/stable-diffusion-webui/”目录下安装:
”“bash
bash <(wget - qo - https://raw.githubusercontent.com/AUTOMATIC1111/stable-diffusion-webui/master/webui.sh)
' ' '

安装在苹果芯片上

你可以在这里(https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Installation-on-Apple-Silicon)找到使用说明。

# #贡献
以下是如何添加代码到这个回购:[贡献](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Contributing)

# #文档
文档从这个README移到项目的[wiki](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki)。

# #学分
借用代码的许可证可以在“设置->许可证”屏幕中找到，也可以在“html/ Licenses .html”文件中找到。

-稳定扩散- https://github.com/CompVis/stable-diffusion, https://github.com/CompVis/taming-transformers
- k-diffusion - https://github.com/crowsonkb/k-diffusion.git
—GFPGAN—https://github.com/TencentARC/GFPGAN.git
—CodeFormer—https://github.com/sczhou/CodeFormer
—ESRGAN—https://github.com/xinntao/ESRGAN
- SwinIR - https://github.com/JingyunLiang/SwinIR
- Swin2SR - https://github.com/mv-lab/swin2sr
—LDSR—https://github.com/Hafiidz/latent-diffusion
—MiDaS—https://github.com/isl-org/MiDaS
-优化的想法- https://github.com/basujindal/stable-diffusion
-交叉注意层优化- Doggettx - https://github.com/Doggettx/stable-diffusion，原始的想法提示编辑。
-跨注意层优化- InvokeAI, lstein - https://github.com/invoke-ai/InvokeAI(原来是http://github.com/lstein/stable-diffusion)
亚二次元交叉注意层优化- Alex Birch (https://github.com/Birch-san/diffusers/pull/1)， AminRezaei (https://github.com/AminRezaei0x443/memory-efficient-attention)
-文本反转- Rinon Gal - https://github.com/rinongal/textual_inversion(我们没有使用他的代码，但我们使用了他的想法)。
- SD高档的想法- https://github.com/jquesnelle/txt2imghd
-噪音产生的油漆mk2 - https://github.com/parlance-zz/g-diffuser-bot
- CLIP询问器的想法和借用一些代码- https://github.com/pharmapsychotic/clip-interrogator
-合成扩散的想法- https://github.com/energy-based-model/Compositional-Visual-Generation-with-Composable-Diffusion-Models-PyTorch
- xformer - https://github.com/facebookresearch/xformers
- DeepDanbooru -动漫扩散器https://github.com/KichangKim/DeepDanbooru
-从float16 UNet中以float32精度采样- marunine为思想，Birch-san为扩散器实现的例子(https://github.com/Birch-san/diffusers-play/tree/92feee6)
-指导pix2pix - Tim Brooks(明星)，Aleksander Holynski(明星)，Alexei A. Efros(无明星)- https://github.com/timothybrooks/instruct-pix2pix
-安全建议- RyotaK
-初始梯度脚本-张贴在4chan的匿名用户。谢谢匿名用户。
>>>>>>> 3739664 (first commit)
>>>>>>> ffd0595 (sdwebui)
