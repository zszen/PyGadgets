import re
import os
import json
import shutil
from bs4 import BeautifulSoup
import sys
import urllib.request
import requests

url = "http://tingapi.ting.baidu.com/v1/restserver/ting"
dl_path = './songs'
max_count = 10

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
}

def get_list(type):
    params_list = {
        'method':'baidu.ting.billboard.billList',
        'type':type,
        'size':max_count,
        'offset':'0',
    }
    json_data = requests.get(url, params=params_list, headers=headers).json()
    # print(json_data)
    return json_data['song_list']

def get_recommand(id):
    params_recommand = {
        'method':'baidu.ting.song.getRecommandSongList',
        'song_id':id,
        'num':max_count,
    }
    json_data = requests.get(url, params=params_recommand, headers=headers).json()
    # print(json_data)
    return json_data

def get_song(song_info):
    params_getSong = {
        'method':'baidu.ting.song.play',
        'songid':song_info['song_id'],
    }
    json_data = requests.get(url, params=params_getSong).json()
    song_file = json_data['bitrate']['file_link']
    # print(json_data['bitrate']['file_link'])
    song_album = json_data['songinfo']['pic_radio']
    # print(song_album)
    return song_file

def download_progress(block_num, block_size, total_size):
    '''回调函数
       @block_num: 已经下载的数据块
       @block_size: 数据块的大小
       @total_size: 远程文件的大小
    '''
    sys.stdout.write('\r>> Downloading %s %.1f%%\r' % (filename,
                     float(block_num * block_size) / float(total_size) * 100.0))
    sys.stdout.flush()

if not os.path.exists(dl_path):
    os.makedirs(dl_path)

lst = get_list(21)
for k in lst:
    file = get_song(k)
    title = k['title']
    # print(k['title'])
    filename = '%s/%s.mp3'%(dl_path,title)
    urllib.request.urlretrieve(file, filename, download_progress)
    print('download %s'%title)