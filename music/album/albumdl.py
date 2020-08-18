import os,re
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import urllib
import threading
import subprocess

options = webdriver.chrome.options.Options()
options.add_argument('--headless')

output_path = '/Users/zszen/Desktop/mp3cover/'
if not os.path.exists(output_path):
    os.mkdir(output_path)

def searchAlbum(file_name, song_name):
    url = f'https://music.163.com/#/search/m/?s={song_name}&type=1'
    driver = webdriver.Chrome('core/driver/chromedriver',options=options)
    driver.get(url)
    driver.implicitly_wait(1)
    current_window = driver.current_window_handle
    driver.switch_to.frame('g_iframe')
    driver.find_element_by_class_name('item').find_elements_by_class_name('w0')[0].find_elements_by_tag_name('a')[0].click()
    # print(res)
    # exit()
    driver.implicitly_wait(1)
    all_window=driver.window_handles
    for window in all_window:
        if window != current_window:
            driver.switch_to.window(window)
            break
    current_window = driver.current_window_handle  # 获取当前窗口handle name
    # res = driver.find_element_by_xpath('div')
    # print(driver.page_source)
    # with open('/Users/zszen/Desktop/tmp2.html','w+') as f:
    #     f.write(driver.page_source)
    album_url = driver.find_elements_by_tag_name('img')[0].get_attribute('src')
    return downAlbum(file_name, album_url)

def downAlbum(file_name, album_url):
    # file_name = '123'
    # album_url = 'http://p2.music.126.net/VLul3Z3HN9_5uDHODl-f4w==/109951164218413147.jpg?param=130y130'
    # urllib.request.urlretrieve(album_url, '/Users/zszen/Desktop/')
    album_url = re.split(r'\?',album_url)[0]
    # res = re.search(r'(\w+\.(jpg|png))', album_url)
    # if not res:
    #     return None
    # filename = res.group(0)
    file_name = re.split(r'\.mp3',file_name)[0]
    # print("file_name", file_name)
    filename = f'{output_path}{file_name}.jpg'
    urllib.request.urlretrieve(album_url, filename=filename)
    return filename

def combinAlbum(fp):
    filename = os.path.basename(fp)
    res = re.split(r' ?- ?|.mp3',filename)
    songname = res[len(res)-2]
    cover = searchAlbum(filename, songname)
    op = output_path+os.path.basename(fp)
    # os.system(f'ffmpeg -y -i {fp} -i {cv} -map 0:0 -map 1:0 -c copy -id3v2_version 3 {op}')
    cmd = f'ffmpeg -y -i \"{fp}\" -i \"{cover}\" -map 0:0 -map 1:0 -c copy -id3v2_version 3 \"{op}\"'
    p = subprocess.Popen(args=cmd , shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True)
    p.wait()
    os.remove(cover)

def getFp(folder):
    for p,fds,fps in os.walk(folder):
        for fp in fps:
            if fp.startswith('.') or not fp.endswith('.mp3'):
                continue
            yield p+'/'+fp

lock = threading.Lock()
def loop(pool):
    while True:
        try:
            with lock:
                fp = next(pool)
        except StopIteration:
            break
        print(f'dealing {fp}')
        combinAlbum(fp)

def major(fd):
    if os.path.isdir(fd):
        pool = getFp(fd)
        ths = []
        for k in range(20):
            t = threading.Thread(target=loop,name=f't{k}',args=(pool,))
            t.start()
            ths.append(t)
        for t in ths:
            t.join()
    else:
        fd = fd.strip()
        fd = fd.replace('\ ',' ')
        if fd.endswith('.mp3'):
            combinAlbum(fd)
        else:
            print('there not have any mp3 file')

if __name__ == "__main__":
    fd = input('music folders:')
    major(fd)
    print('== end ==')