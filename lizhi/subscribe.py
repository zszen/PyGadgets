import re
import urllib.request
import requests
from bs4 import BeautifulSoup
import os
import json
import shutil
import sys
import datetime
import time
sys.path.append(os.path.dirname(__file__)+'/..')
from color.colorprint import cc
from enum import Enum
import threading

class DownloadFilter(Enum):
    blockForbid = 1 << 0 #屏蔽关键词组
    blockUnWanna = 1 << 1 #只下载需求词
    addByInput = 1 << 2 #只下载输入文本
    clearHistoryFile = 1<<3 # 清空以前的音频
    history = 1<<4 # 下载历史文件
    continuity = 1<<5 # 连续下载当前节目
    none = 0

file_cfg = './lizhi/conf.cfg'
json_data = None
folder_download = './lizhi/podcasts'
current_author_name = ""
current_title_name = ""
current_file_path = ""
thread_num = 10
dl_timeoutp = 5
# 增加下载音频
# dfilter = DownloadFilter.blockForbid.value | DownloadFilter.addByInput.value
dfilter = DownloadFilter.blockForbid.value | DownloadFilter.blockUnWanna.value | DownloadFilter.history.value | DownloadFilter.continuity.value
rStrForbid = r'(付费|预告|鬼影重重|影榴莲)'
rStrDownload = r'(风水|恐怖|传说|故事|毛嗑|鬼|灵异|灵异|怪物|怪谈|头七|神秘|怪谈|事件|死|妖怪|仙|奇谈|诡|魂|亲历|清明|七月|7月|档案|外星人|惊魂|奇了怪了|x事在身边)'

def clear_all():
    make_sure_remove_all = input('你确定要清空%s吗? (OK / any)'%folder_download)
    if make_sure_remove_all.startswith("OK"):
        print("清理开始")
        if os.path.exists(folder_download):
            for k in os.listdir(folder_download):
                if os.path.isdir(folder_download+'/'+k):
                    shutil.rmtree(folder_download+'/'+k)
        print("清理完毕")
    else:
        print("放弃清理")

def load_cfg():
    global json_data
    if os.path.exists(file_cfg):
        with open(file_cfg,'r') as f:
            try:
                json_data = json.load(f)
            except Exception as e:
                json_data = {}
            f.close()

def save_cfg():
    with open(file_cfg,'w') as f:
        f.seek(0)
        f.truncate()
        f.write(json.dumps(json_data))
        f.close()

load_cfg()

print('============')
for i,k in enumerate(json_data):
    print('[%d] %s'%(i,k))
print('============')

# _ud.mp3:超高清; _hd.mp3:高清; _sd.m4a:低清

def get_music_lizhifm(url):
    id = url.rsplit('/', 1)[1]
    url = 'http://www.lizhi.fm/media/url/{}'.format(id)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    }
    html = requests.get(url, headers=headers).json()
    # print(html)
    if html['data']:
        mp3_url = html['data']['url']
        return mp3_url
    else:
        cc.print("!!!%s"%html['msg'],cc.red)
        return None

def download_progress(block_num, block_size, total_size):
    '''回调函数
       @block_num: 已经下载的数据块
       @block_size: 数据块的大小
       @total_size: 远程文件的大小
    '''
    sys.stdout.write('\r>> Downloading [%s] %s %.1f%%\r' % (current_author_name, current_title_name,
                     float(block_num * block_size) / float(total_size) * 100.0))
    sys.stdout.flush()

def downloadFromPage(startUrl):
    global json_data,current_file_path,current_author_name,current_title_name
    # if startUrl == 'https://www.lizhi.fm/1027923/5115069225546210310':
    #     print(123)
    page = requests.get(startUrl)
    userId = re.findall('(/[0-9]{5,10}/)', startUrl)[0]
    downloadurl = get_music_lizhifm(startUrl)
    # print(page.content)
    # with open('tmp.tmp','w') as f:
    #     f.write(page.text)
    bs = BeautifulSoup(page.content, features='lxml')
    # print(bs.find('div', attrs=''))
    if downloadurl:
        try:
            folder_name = bs.select('.breadcrumbs a')[1].text
        except Exception as e:
            print(e)
            folder_name = "未知电台"
        if folder_name not in json_data:
            json_data[folder_name] = {}
        json_data[folder_name]['url'] = startUrl
        date = bs.select(".audioTime")[0].text
        dt = time.strptime(date, '%Y-%m-%d')
        dt_str = time.strftime('%y%m%d', dt)
        title = bs.select(".audioName")[0].text
        if re.search(rStrForbid, title) is None or dfilter&DownloadFilter.blockForbid.value==0:
            if re.search(rStrDownload, title) is not None or dfilter&DownloadFilter.blockUnWanna.value==0:
                filename = '%s/%s/%s_%s.mp3'%(folder_download,folder_name,dt_str ,title)
                # if not os.path.exists(filename):
                current_file_path = filename
                current_author_name = folder_name
                current_title_name = title
                if "last" not in json_data[folder_name] or json_data[folder_name]['last']!=downloadurl:
                    if re.search(rStrDownload, title) is None:
                        cc.print(f'downloading {filename}', cc.red)
                    else:
                        cc.print(f'downloading {filename}', cc.yellow)
                    if not os.path.exists(folder_download+'/'+folder_name):
                        os.mkdir(folder_download+'/'+folder_name)
                    json_data[folder_name]['last'] = downloadurl
                    urllib.request.urlretrieve(downloadurl, filename, download_progress)
                else:
                    cc.print(f'had downloaded {title}', cc.white)
            else:
                cc.print(f'skip {title}', cc.white)
        else:
            cc.print(f'skip {title}', cc.white)
    else:
        cc.print(f'skip 抢先听/付费', cc.white)
    save_cfg()

    if dfilter&DownloadFilter.continuity.value:
        # get next url
        urlList = []
        for link in bs.findAll('a'):
            url = link.get('href')
            # print(link.previous_sibling)
            downloadableUrl = re.findall('(^[0-9]{17,21}$)', url)
            if downloadableUrl:
                urlList.append(downloadableUrl[0])
            if url=='0':
                urlList.append(url)
        # print(urlList)
        if(len(urlList) == 2):
            nextUrl = 'https://www.lizhi.fm'+userId+urlList[len(urlList)-1]
            cc.print('nextUrl: ' + nextUrl, cc.blue)
            downloadFromPage(nextUrl)
        else:
            cc.print('..搜索结束',cc.blue)
            # save_cfg()
            return
            # exit()

def get_download_url():
    for k in json_data:
        url = json_data[k]['url']
        yield url
        # downloadFromPage(url)

lock = threading.Lock()
def loop_thread(dl_urls):
    # print(f'thread {threading.current_thread().name} is running')
    while True:
        try:
            with lock:
                url = next(dl_urls)
        except StopIteration:
            break
        print(url)
        try:
            downloadFromPage(url)
            save_cfg()
        except:
            print(f'except fail : {url}')
    # print(f'thread {threading.current_thread().name} end !')


if __name__ == '__main__':
    cc.print('*' * 30 + ' ready to download ' + '*' * 30, cc.cyan)
    if dfilter&DownloadFilter.clearHistoryFile.value:
        clear_all()
    if dfilter&DownloadFilter.addByInput.value:
        # url = 'https://www.lizhi.fm/1991282/5096298613617271430?u=2674259910694143020'
        url = input('[请输入新的荔枝下载链接]:')
        if url!='':
            downloadFromPage(url)
            save_cfg()
    if dfilter&DownloadFilter.history.value:
        dl_urls = get_download_url()
        threads = []
        for i in range(0, thread_num):
            t = threading.Thread(target=loop_thread, name=f'thread{i}', args=(dl_urls,))
            t.start()
            threads.append(t)
        for t in threads:
            t.join()
    cc.print('*' * 30 + ' end ' + '*' * 30, cc.white)
