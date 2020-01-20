# awesome-script

### [Bilibili_Download.py](./some_script/Bilibili_Download.py)

B站有很多学习视频，很多都是分集的视频列表，有时候希望批量下载这些视频到本地观看。找到 [you-get](https://github.com/soimort/you-get) 这个神器，这个下载工具可以跑满网速，下载速度惊人，关键是它可以下载很多网站的流视频。
[Bilibili_Download.py](./some_script/Bilibili_Download.py) 这个脚本调用了 you-get 来批量下载哔哩哔哩视频。

B站的视频都是流视频，通过 you-get 下载的视频文件和音频文件是分离的，需要通过 [FFmpeg](https://www.ffmpeg.org/) 这个工具来进行合成，可以去官网下载二进制文件添加到系统环境变量PATH中就可以了。



### you-get

you-get 是一个用 Python 写的下载神器，官网是 https://github.com/soimort/you-get/

它可以下载 哔哩哔哩，YouTube 等网站的视频。



用法笔记：

```shell
# 查看视频信息
you-get -i  url
```







### [FFmpeg](https://www.ffmpeg.org/)

[FFmpeg](https://www.ffmpeg.org/) 是视频处理中最常用的开源软件。



它功能强大，用途广泛，大量用于视频网站和商业软件（比如 Youtube 和 iTunes），也是许多音频和视频格式的标准编码/解码实现。

FFmpeg 本身是一个庞大的项目，包含许多组件和库文件，最常用的是它的命令行工具。

#### FFmpeg 下载安装

去官网下载二进制版解压到本地目录后，然后将解压目录添加到操作系统的 PATH 环境变量下。

在 命令行中输入` ffmpeg  version` 如果有正常输出，即安装成功。

#### 视频文件（容器）

视频文件本身其实是一个容器（container），里面包括了视频和音频，也可能有字幕等其他内容。

常见的容器格式有以下几种。一般来说，视频文件的后缀名反映了它的容器格式。

> - MP4
> - MKV
> - WebM 
> - AVI  （Audio Video Interleaved 音视频交错格式）
> - MPEG      家里常看的VCD、SVCD、[DV](https://link.zhihu.com/?target=http%3A//product.pcpop.com/DV/00000_1.html)D就是这种格式
> - FLV     



我们知道Windows系统中的文件名都有后缀，例如 1.docx，2.wps，3.psd等等。

Windows设置后缀名的目的是让系统中的应用程序来识别并关联这些文件，让相应的文件由相应的应用程序打开。

例如你双击1.doc文件，它会知道让Microsoft Office去打开，而不会用Photoshop去打开这个文件。

所以常见的视频文件格式如 1.avi，2.mpg 这些都叫做视频的文件格式，它由你电脑上安装的视频播放器关联。

你可以随意改扩展名，但是真的对视频真正的一点影响都没有，千万不要以为 avi 改成 mp4，视频就变成 mp4 格式了。

下面的命令查看 FFmpeg 支持的容器。

```bash
$ ffmpeg -formats
```





