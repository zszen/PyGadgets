import re
import urllib.request
import requests
from bs4 import BeautifulSoup
import os
import json
import shutil
import sys

file_cfg = './lizhi/conf.cfg'
json_data = None
filename_download_current = ""
folder_download = './lizhi/podcasts'

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
# https://www.lizhi.fm/1991282/5096298613617271430?u=2674259910694143020
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
        print("!!!"+html['msg'])
        return None

def download_progress(block_num, block_size, total_size):
    '''回调函数
       @block_num: 已经下载的数据块
       @block_size: 数据块的大小
       @total_size: 远程文件的大小
    '''
    sys.stdout.write('\r>> Downloading %s %.1f%%\r' % (filename_download_current,
                     float(block_num * block_size) / float(total_size) * 100.0))
    sys.stdout.flush()

def downloadFromPage(startUrl):
    global json_data,filename_download_current
    page = requests.get(startUrl)
    userId = re.findall('(/[0-9]{5,10}/)', startUrl)[0]
    downloadurl = get_music_lizhifm(startUrl)
    urlList = []
    # print(page.content)
    bs = BeautifulSoup(page.content, features='lxml')
    # print()
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
        title = bs.select(".audioName")[0].text
        # print(title)
        if title.find('付费') == -1:
            filename = '%s/%s/%s.mp3'%(folder_download,folder_name,title)
            # if not os.path.exists(filename):
            filename_download_current = filename
            if "last" not in json_data[folder_name] or json_data[folder_name]['last']!=downloadurl:
                if not os.path.exists(folder_download+'/'+folder_name):
                    os.mkdir(folder_download+'/'+folder_name)
                json_data[folder_name]['last'] = downloadurl
                urllib.request.urlretrieve(downloadurl, filename, download_progress)
    save_cfg()
    # get next url
    for link in bs.findAll('a'):
        url = link.get('href')
        downloadableUrl = re.findall('(^[0-9]{19}$)', url)
        if downloadableUrl:
            urlList.append(downloadableUrl[0])
    if(len(urlList) == 2):
        nextUrl = 'https://www.lizhi.fm'+userId+urlList[1]
        print('nextUrl: ' + nextUrl)
        downloadFromPage(nextUrl)
    else:
        print('urlList length error:')
        # save_cfg()
        return
        # exit()

if __name__ == '__main__':
    print('*' * 30 + 'ready to download' + '*' * 30)
    clear_all()
    url = input('[请输入初始下载链接]:')
    # url = 'https://www.lizhi.fm/1991282/5096298613617271430?u=2674259910694143020'
    if url!='':
        downloadFromPage(url)
    for k in json_data:
        url = json_data[k]['url']
        print(k)
        downloadFromPage(url)
    save_cfg()
