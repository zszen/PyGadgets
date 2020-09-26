from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.
# from selenium.webdriver.support.relative_locator import with_tag_name
import re,os
from time import sleep
import json

import requests
import hashlib
import random
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# https://www.ximalaya.com/xiqu/13551750/
data_path = 'snoop/ximalaya/data.json'
data_au_path = 'snoop/ximalaya/data_au.json'

driver = None
data = {}
with open(data_path,'r') as f:
    data = json.load(f)
data_au = {}
try:
    with open(data_au_path,'r') as f:
        data_au = json.load(f)
except:
    pass

def init_webdriver():
    global driver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome('core/driver/chromedriver',options=options)

def close_webdriver():
    global driver
    driver.quit()

def get_list(url:str):
    global data
    driver.get(url)
    if True:
        for idx,li in enumerate(driver.find_elements_by_css_selector('li._Vc')):
            tag_a = li.find_element_by_tag_name('a')
            data[tag_a.text] = tag_a.get_attribute('href')
        with open(data_path,'r+') as f:
            f.write(json.dumps(data))
    get_nextlist()

def get_nextlist():
    page_nexts = driver.find_elements_by_css_selector('li.page-item.active._Xo+li>a')
    if len(page_nexts)==0:
        return
    page_next = page_nexts[0]
    # print("page_next",page_next, page_next.tag_name, page_next.get_attribute('href'))
    next_url = page_next.get_attribute('href')
    print(f'wait secs to get page {page_next.text}')
    sleep(1)
    get_list(next_url)

def get_au_files(data_path):
    with open(data_path, 'r') as f:
        data = json.load(f)
    # print(len(date))
    max = len(data)
    for i,k in enumerate(data):
        print(f'{i}/{max}')
        url = data[k]
        song_id = re.search(r'/(\d+)$',url).group(1)
        try:
            # url = 'file:///Users/zszen/Desktop/Code/PyGadgets/snoop/ximalaya/test2.html'
            # print(url)

            url_au = f"https://www.ximalaya.com/revision/play/v1/audio?id={song_id}&ptype=1"
            # url_au = f"https://www.ximalaya.com/revision/play/tracks?trackIds={song_id}"
            s = requests.get(url_au,headers=get_header(),verify=False)
            data_au_unit = s.json()
            data_au[k] = {
                'au':data_au_unit['data']['src']
                ,'url':url
            }
            # print()
            sleep(random.random()*.5+.5)
            # continue
        except:
            print('err::',k,data[k])
            break
            # continue
        # driver.get(url)
        # sleep(1)
        # play_bts = driver.find_elements_by_css_selector('i.icon.play-icon.fR_')
        # if len(play_bts)==0:
        #     continue
        # play_bts[0].click()
        # sleep(1)

        # st = driver.page_source
        # print("st", st)
        # res = re.search('<iframe .*?>(.*?)</iframe>',st)
        # print(res.group(0))

        # divs = driver.find_elements_by_css_selector('div:before')
        # print("divs", divs[len(divs)-1])
        # print("iframes", iframes)
        # driver.switch_to.frame(0)
        # fr = driver.switch_to.frame(0)
        # print(fr)

        # au = driver.find_elements_by_css_selector('body')
        # print(au[0].text)
        # data_au[k] = {
        #     'url':data[k]
        #     'audio':
        # }
        # print()
        if i%10==0:
            with open(data_au_path,'r+') as f:
                f.write(json.dumps(data_au))
                print(f'saved {i}')
        continue
    

def get_sign(headers):
    serverTimeUrl = "https://www.ximalaya.com/revision/time"
    response = requests.get(serverTimeUrl,headers=headers,verify=False)
    serverTime = response.text
    nowTime = str(round(time.time()*1000))
 
    sign = str(hashlib.md5("himalaya-{}".format(serverTime).encode()).hexdigest()) + "({})".format(str(round(random.random()*100))) + serverTime + "({})".format(str(round(random.random()*100))) + nowTime
    # 在这里添加入请求头
    headers["xm-sign"] = sign
    return headers
 
def get_header():
    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36"
    }
    headers = get_sign(headers)
    return headers

if __name__ == "__main__":
    # init_webdriver()
    # url = input('ximalaya list url:')
    # url = 'https://www.ximalaya.com/xiqu/13551750/'
    # url = 'file:///Users/zszen/Desktop/Code/PyGadgets/snoop/ximalaya/test.html'
    # get_list(url)

    get_au_files(data_path)

    # url = "https://www.ximalaya.com/revision/play/v1/audio?id=139836377&ptype=1"
    
    # url = 'https://www.ximalaya.com/xiqu/13551750/102310355'
    # print(re.search(r'/(\d+)$',url).group(1))

    # url = 'https://www.ximalaya.com/xiqu/13551750/102310354'
    # song_id = '102310354'
    # url_au = f"https://www.ximalaya.com/revision/play/v1/audio?id={song_id}&ptype=1"
    # s = requests.get(url_au,headers=get_header(),verify=False)
    # print("s.json()", s.json())

    # close_webdriver()