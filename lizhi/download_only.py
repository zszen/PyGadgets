import re
import urllib.request
import requests
from bs4 import BeautifulSoup
import os
import json
import shutil
import sys

json_data = {}
filename_download_current = ""
folder_download = './lizhi/podcasts'

def get_music_lizhifm(url):
    id = url.rsplit('/', 1)[1]
    url = 'http://www.lizhi.fm/media/url/{}'.format(id)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    }
    html = requests.get(url, headers=headers).json()
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
    bs = BeautifulSoup(page.content, features='lxml')
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
        if title.find('付费') == -1:
            filename = '%s/%s/%s.mp3'%(folder_download,folder_name,title)
            filename_download_current = filename
            if "last" not in json_data[folder_name] or json_data[folder_name]['last']!=downloadurl:
                if not os.path.exists(folder_download+'/'+folder_name):
                    os.mkdir(folder_download+'/'+folder_name)
                json_data[folder_name]['last'] = downloadurl
                urllib.request.urlretrieve(downloadurl, filename, download_progress)
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
        return

if __name__ == '__main__':
    print('*' * 30 + 'ready to download' + '*' * 30)
    url = input('[请输入初始下载链接]:')
    if url!='':
        downloadFromPage(url)
