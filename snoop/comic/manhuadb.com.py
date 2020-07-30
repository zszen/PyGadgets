import os
import re
from bs4 import BeautifulSoup
import requests
from lxml import etree
import threading
import time

root = os.path.dirname(__file__)
site = 'https://www.manhuadb.com/'
comic_page = f'manhua/139/1328_13264%s.html'


def get_page(url, page=1):
    if page == 1:
        url = url%''
    else:
        url = url%(f'_p{page}')
    res = requests.request(url=url, method='get')
    # return res.content
    return res.content.decode('utf-8')

def down(url, page=1):
    html = get_page(url, page)
    if parse_page(html, page):
        return html
    return None

def parse_title(content):
    bs = BeautifulSoup(content, features="html.parser")
    title = bs.title.text
    if not os.path.exists(f'{root}/dl/{title}'):
        os.mkdir(f'{root}/dl/{title}')
    return title

def parse_page(content, page):
    bs = BeautifulSoup(content, features="html.parser")
    # if content:
    #     print(type(content))
    # else:
    #     f = open(os.path.dirname(__file__)+'/tmp.html', 'r')
    #     bs = BeautifulSoup(f.read(), features="html.parser")
    #     f.close()
    title = parse_title(content)
    time.sleep(.5)
    for k in bs.find_all('img'):
        img = k.get('src')
        if re.search(r'\d+_?\w*\.jpg', img):
            html = requests.get(img, timeout=8)
            if html.status_code!=200:
                return False
            print(img)
            if os.path.exists(f'{root}/dl/{title}/{page}.jpg'):
                return True
            with open(f'{root}/dl/{title}/{page}.jpg','wb') as f:
                f.write(html.content)
            return True
    return False

# def next_charpter(url):

def parse_charpter(url):
    title = parse_title(get_page(site+url))
    max_num = 0
    for k in os.listdir(f'{root}/dl/{title}'):
        res = re.search('(\d+).jpg',k)
        if res:
            max_num = max(max_num, int(res.group(1)))
    for k in range(max_num+1, 500):
        yield k
    # bs = BeautifulSoup(html, features="html.parser")
    # a = bs.select('a.active')[0].findNext('a')
    
lock = threading.Lock()
def loop_thread(url, dls):
    # isEnd = False
    while True:
        try:
            with lock:
                dl_id = next(dls)
        except StopIteration:
            break
        print(dl_id)
        if not down(site+url,dl_id):
            break

if __name__ == "__main__":
    # parse_charpter(comic_page)
    # parse()
    # threads = []
    dls = parse_charpter(comic_page)
    for k in range(0, 2):
        t = threading.Thread(target=loop_thread, name=f'thread{k}', args=(comic_page, dls,))
        t.start()
    
    # print('done')
    # for k in range(max_num+1,500):
    #     html = down(site+url,k)
    #     if html==None:
    #         break