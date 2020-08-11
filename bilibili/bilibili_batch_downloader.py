"""Stub file for the 'time' module."""
from selenium import webdriver
from time import sleep
# import ffmpeg
# import imageio
import requests, time, hashlib, urllib.request, re, json
# from moviepy.editor import *
import os, sys
import subprocess

# imageio.plugins.ffmpeg.download()

start_time = time.time()

def get_play_list(start_url, cid, quality):
    entropy = 'rbMCKn@KuamXWlPMoJGsKcbiJKUfkPF_8dABscJntvqhRSETg'
    appkey, sec = ''.join([chr(ord(i) + 2) for i in entropy[::-1]]).split(':')
    params = 'appkey=%s&cid=%s&otype=json&qn=%s&quality=%s&type=' % (appkey, cid, quality, quality)
    chksum = hashlib.md5(bytes(params + sec, 'utf8')).hexdigest()
    url_api = 'https://interface.bilibili.com/v2/playurl?%s&sign=%s' % (params, chksum)
    headers = {
        'Referer': start_url,  # 注意加上referer
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.30 Safari/537.36'
    }
    # print(url_api)
    html = requests.get(url_api, headers=headers).json()
    # print(json.dumps(html))
    video_list = []
    for i in html['durl']:
        video_list.append(i['url'])
    # print(video_list)
    return video_list


# 下载视频
'''
 urllib.urlretrieve 的回调函数：
def callbackfunc(blocknum, blocksize, totalsize):
    @blocknum:  已经下载的数据块
    @blocksize: 数据块的大小
    @totalsize: 远程文件的大小
'''


def Schedule_cmd(blocknum, blocksize, totalsize):
    speed = (blocknum * blocksize) / (time.time() - start_time)
    # speed_str = " Speed: %.2f" % speed
    speed_str = " Speed: %s" % format_size(speed)
    recv_size = blocknum * blocksize

    # 设置下载进度条
    f = sys.stdout
    pervent = recv_size / totalsize
    percent_str = "%.2f%%" % (pervent * 100)
    n = round(pervent * 50)
    s = ('#' * n).ljust(50, '-')
    f.write(percent_str.ljust(8, ' ') + '[' + s + ']' + speed_str)
    f.flush()
    # time.sleep(0.1)
    f.write('\r')


def Schedule(blocknum, blocksize, totalsize):
    speed = (blocknum * blocksize) / (time.time() - start_time)
    # speed_str = " Speed: %.2f" % speed
    speed_str = " Speed: %s" % format_size(speed)
    recv_size = blocknum * blocksize

    # 设置下载进度条
    f = sys.stdout
    pervent = recv_size / totalsize
    percent_str = "%.2f%%" % (pervent * 100)
    n = round(pervent * 50)
    s = ('#' * n).ljust(50, '-')
    print(percent_str.ljust(6, ' ') + '-' + speed_str)
    f.flush()
    time.sleep(2)
    # print('\r')


# 字节bytes转化K\M\G
def format_size(bytes):
    try:
        bytes = float(bytes)
        kb = bytes / 1024
    except:
        print("传入的字节格式不对")
        return "Error"
    if kb >= 1024:
        M = kb / 1024
        if M >= 1024:
            G = M / 1024
            return "%.3fG" % (G)
        else:
            return "%.3fM" % (M)
    else:
        return "%.3fK" % (kb)


#  下载视频
def down_video(video_list, title, start_url, page):
    num = 1
    print('[下载P{}段视频]:'.format(page) + title)
    currentVideoPath = os.path.join(sys.path[0], 'download')  # 当前目录作为下载目录
    for i in video_list:
        opener = urllib.request.build_opener()
        # 请求头
        opener.addheaders = [
            # ('Host', 'upos-hz-mirrorks3.acgvideo.com'),  #注意修改host,不用也行
            ('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:56.0) Gecko/20100101 Firefox/56.0'),
            ('Accept', '*/*'),
            ('Accept-Language', 'en-US,en;q=0.5'),
            ('Accept-Encoding', 'gzip, deflate, br'),
            ('Range', 'bytes=0-'),  # Range 的值要为 bytes=0- 才能下载完整视频
            ('Referer', start_url),  # 注意修改referer,必须要加的!
            ('Origin', 'https://www.bilibili.com'),
            ('Connection', 'keep-alive'),
        ]
        urllib.request.install_opener(opener)
        # 创建文件夹存放下载的视频
        if not os.path.exists(currentVideoPath):
            os.makedirs(currentVideoPath)
        # 开始下载
        if len(video_list) > 1:
            urllib.request.urlretrieve(url=i, filename=os.path.join(currentVideoPath, r'{}-{}.flv'.format(title, num)),reporthook=Schedule_cmd) 
            print('[视频合并完成]' + title)
            subprocess.Popen('ffmpeg -i "%s" -vcodec copy -acodec copy "%s"'%(os.path.join(currentVideoPath, os.path.join(currentVideoPath, r'{}-{}.mp4'.format(title, num))),r'{}.mp4'.format(title)), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        else:
            urllib.request.urlretrieve(url=i, filename=os.path.join(currentVideoPath, r'{}.flv'.format(title)),reporthook=Schedule_cmd) 
            print('[视频合并完成]' + title)
            ffcmd = 'ffmpeg -i "%s" -vcodec copy -acodec copy "%s"'%(os.path.join(currentVideoPath, r'{}.flv'.format(title)), os.path.join(currentVideoPath, r'{}.mp4'.format(title)))
            subprocess.Popen(ffcmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        num += 1

# 合并视频
def combine_video(video_list, title):
    currentVideoPath = os.path.join(sys.path[0], 'download')  # 当前目录作为下载目录
    if not os.path.exists(currentVideoPath):
        os.makedirs(currentVideoPath)
    if len(video_list) >= 2:
        # 视频大于一段才要合并
        print('[下载完成,正在合并视频...]:' + title)
        # 定义一个数组
        L = []
        # 访问 video 文件夹 (假设视频都放在这里面)
        root_dir = currentVideoPath
        # 遍历所有文件
        for file in sorted(os.listdir(root_dir), key=lambda x: int(x[x.rindex("-") + 1:x.rindex(".")])):
            # 如果后缀名为 .mp4/.flv
            if os.path.splitext(file)[1] == '.flv':
                # 拼接成完整路径
                filePath = os.path.join(root_dir, file)
                # 载入视频
                video = VideoFileClip(filePath)
                # 添加到数组
                L.append(video)
        # 拼接视频
        final_clip = concatenate_videoclips(L)
        # 生成目标视频文件
        final_clip.to_videofile(os.path.join(root_dir, r'{}.flv'.format(title)), fps=24, remove_temp=False)
        print('[视频合并完成]' + title)
        subprocess.Popen('ffmpeg -i %s -vcodec copy -acodec copy %s'%(r'{}.flv'.format(title),r'{}.mp4'.format(title)), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    else:
        # 视频只有一段则直接打印下载完成
        print('[视频合并完成]:' + title)

def getAid(Bvid):
    Bid=Bvid
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }
    url = "https://api.bilibili.com/x/web-interface/view?bvid="+Bid
    r = requests.get(url,headers=headers)
    j = json.loads(r.text)
    # print(j["data"]["aid"])
    return j["data"]["aid"]


def download(BVid):
    # 用户输入av号或者视频链接地址
    start = 'https://www.bilibili.com/video/av' + str(getAid(BVid))

    if start.isdigit() == True:  # 如果输入的是av号
        # 获取cid的api, 传入aid即可
        start_url = 'https://api.bilibili.com/x/web-interface/view?aid=' + start
    else:
        # https://www.bilibili.com/video/av46958874/?spm_id_from=333.334.b_63686965665f7265636f6d6d656e64.16
        start_url = 'https://api.bilibili.com/x/web-interface/view?aid=' + re.search(r'/av(\d+)/*', start).group(1)

    # 视频质量
    # <accept_format><![CDATA[flv,flv720,flv480,flv360]]></accept_format>
    # <accept_description><![CDATA[高清 1080P,高清 720P,清晰 480P,流畅 360P]]></accept_description>
    # <accept_quality><![CDATA[80,64,32,16]]></accept_quality>
    #quality = input('请输入您要下载视频的清晰度(1080p:80;720p:64;480p:32;360p:16)(填写80或64或32或16):')
    quality='80'
    # 获取视频的cid,title
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }
    html = requests.get(start_url, headers=headers).json()
    data = html['data']
    video_title=data["title"].replace(" ","_")
    cid_list = []
    if '?p=' in start:
        # 单独下载分P视频中的一集
        p = re.search(r'\?p=(\d+)',start).group(1)
        cid_list.append(data['pages'][int(p) - 1])
    else:
        # 如果p不存在就是全集下载
        cid_list = data['pages']
    # print(cid_list)
    for item in cid_list:
        cid = str(item['cid'])
        title = item['part']
        if not title:
            title = video_title
        title = re.sub(r'[\/\\:*?"<>|]', '', title)  # 替换为空的
        #print('[下载视频的cid]:' + cid)
        #print('[下载视频的标题]:' + title)
        page = str(item['page'])
        start_url = start_url + "/?p=" + page
        video_list = get_play_list(start_url, cid, quality)
        start_time = time.time()
        down_video(video_list, title, start_url, page)
        combine_video(video_list, title)


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome('core/driver/chromedriver',chrome_options=chrome_options)
BVlist=[]

def nextPage():
    try:
        for page in driver.find_elements_by_class_name("be-pager-next"):
            page.click()
    except:
        return 0
    else:
        print('-'*40+'翻页'+'-'*40)
        return 1


def getBV():
    for link in driver.find_elements_by_class_name("small-item"):
        print(link.get_attribute('data-aid'))
        BVlist.append(link.get_attribute('data-aid'))

def downBV(*,bv:str):
    BVlist.append(bv)
    count=1
    total=len(BVlist)
    for video in BVlist:
        print('='*40+' '+str(count)+'/'+str(total)+' '+'='*40)
        download(video) 
        count+=1
    print('done')

def downPlaylist(*, favor:str):
    driver.get(favor)
    sleep(3)
    getBV()
    # while(nextPage()):
    #     sleep(3)
    #     getBV()
    total=len(BVlist)
    print('\n抓取到'+str(total)+'个视频')
    driver.quit()
    count=1
    for video in BVlist:
        print('='*40+' '+str(count)+'/'+str(total)+' '+'='*40)
        download(video) 
        count+=1


#收藏夹地址，注意收藏夹一定要是公开的
# downPlaylist(favor='https://www.bilibili.com/video/BV16t411y7zx')
bv_url = input("输入网址: ")
res = re.search(r'(BV((?!\/).)+)', bv_url)
if res:
    bv = res.group(1)
    downBV(bv=bv)
print('== end ==')


#默认下载地址为本py文件所在目录下的download文件夹
#默认下载画质为优先1080p

#由收藏夹地址抓取收藏夹内视频BV号的功能由本人实现
#下载功能完全照搬Henryhaohao的Bilibili_video_download
#BV号转AV号部分的代码，来源于上述项目的issue:'针对BV号的问题',作者CodeForWuyu




