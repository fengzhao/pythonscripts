import os
import requests


# https://blog.csdn.net/zhouruifu2015/article/details/5083651629
# https://www.bilibili./video/av46939522/?p=2
def handle_url(base_url, page):
    param = {'p': page}
    r = requests.get(base_url, param)
    return r.url


# 调you-get工具进行下载
def cmd_download(dowmload_url):
    info = os.system(r'you-get  -o H:\学习资料\GIT学习视频   --format=dash-flv720  {}'.format(dowmload_url))
    print(info)
    return 1


def main():
    start_page = eval(input('请输入起始页码：'))
    end_page = eval(input('请输入结束页码：'))
    base_url = 'https://www.bilibili.com/video/av46939522/'
    for page in range(start_page, end_page + 1):
        download_url = handle_url(base_url, page)
        cmd_download(download_url)
        

if __name__ == '__main__':
    main()
