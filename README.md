# awesome script


[Bilibili_Download.py](./some_script/Bilibili_Download.py)

B站有很多学习视频，很多都是分集的视频列表，有时候希望批量下载这些视频到本地观看。找到 [you-get](https://github.com/soimort/you-get) 
这个神器，这个下载工具可以跑满网速，下载速度惊人，关键是它可以下载很多网站的流视频。
这是一个调用 you-get 工具批量下载B站的视频列表的脚本，主要依赖于 requests 和 you-get 库。
B站的视频都是流视频，通过 you-get 下载的视频文件和音频文件是分离的，需要通过 [FFmpeg](https://www.ffmpeg.org/) 
这个工具来下载，可以去官网下载二进制文件添加到系统环境变量PATH中就可以了。


