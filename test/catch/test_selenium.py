from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from lxml import etree
import requests
import re

def getRealUrl(url):
    if not url.startswith('http'):
        return None
    tmpPage = requests.get(url, allow_redirects=False)
    if tmpPage.status_code == 200:
        # print(tmpPage.text.encode('utf-8'))
        # urlMatch = re.search(r'URL=\'(.*?)\'', tmpPage.text.encode('utf-8'))
        # originalURLs.append((urlMatch.group(1), tmpurl[1]))
        return None
    elif tmpPage.status_code == 302:
        str = tmpPage.headers.get('location')
        if str.startswith('/baidu.php'):
            return None
        return str
        # originalURLs.append((tmpPage.headers.get('location'), tmpurl[1]))
    else:
        print('No URL found!!')
        return None
        # return url

def getData():
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')
    browser = webdriver.Chrome(f'{os.getcwd()}/enviroment/chromedriver',options=option)
    browser.get('https://www.baidu.com')
    input = browser.find_element_by_class_name('s_ipt')
    input.send_keys('确诊')
    input.send_keys(Keys.ENTER)
    # time.sleep(1)
    wait = WebDriverWait(browser, 10)
    # button = wait.until(EC.element_to_be_clickable(By.CSS_SELECTOR,'#s_btn'))
    # print(button)

    time.sleep(1)

    html = browser.page_source
    # print(html)
    data = etree.HTML(html)
    res = data.xpath('//div/h3/a')
    for k in res:
        url = getRealUrl(k.xpath('@href')[0])
        if not url:
            continue
        title = k.xpath('string()')
        title = title.strip()
        print(f"\033[32;1m{title}\033[0m")
        print(url)

    # button = browser.find_element_by_class_name('btn-search')
    # button.click()

    # time.sleep(3)
    browser.quit()


# print(getRealUrl('http://www.baidu.com/baidu.php?url=0s0000aPch_Smgbn9uPiZ0_o8Lk29Oo7sSAgWuKQmmD9gvWNQU4pH8XPfGdANvn-nagpliLsvnGGYosptMSQHni_HAqHrAtTUewBiTMbmxt8MJDOEEkSRIUWivI-3XM0zxwCxAS7H1tr8iiZKNS9dYHJgcFg396BTEI-3_c3ykeNJiRouy1yKzq2NzJZrNLaya37BW_6Tfwzp7xaLSv-TCiS3e1M.DR_NR2Ar5Od66sw5I7M9CE9exQQTBaPrMLek8sHfGmEukmntgUZdsw5I7qehnMHbtXMk3e_MyPqK5L8mEukmc8v5-tIMA1xYeS1_ozITI7MwqehrMFdHYRArMxbotUnhOuktXoPLqZ6BHnkudCrmJCRnTXZWeTrHl3TMdxfHGs455QI9zXTQVrZFqXMxbotUnhOuktTrH1JCpprZWqUe8glnyZWtEOOJSe-SW7OOqJN9h9moer5ZBC0.U1Yk0ZDqXjb4FHcsmLKd0ZKGm1Yk0ZfqXjb4FHcsmLKd0A-V5HDYPWD0u1dsT1c0Iybqmh7GuZR0TA-b5HD0mv-b5Hn4n0KVIjYknH0znNtknjDLg1DsnH-xn1msnfKopHYk0ZFY5HD1rfK-pyfqn1D4njIxnHfdn7t1nHnzP-t1nWD1rNt1nHcdndt1nW0YPNt1nWc1n7t1nHTsr7t1nWDsPdtzPWndn7t1nHm1rfKBpHYkPHNxnHR3g1csP7tznHT0Uynqn1KxnH6dPHcvPjmYP7tknj0kg100TgKGujYs0Z7Wpyfqn0KzuLw9u1Ys0A7B5HKxn0K-ThTqn0KsTjYs0A4vTjYsQW0snj0snj0s0AdYTjYs0AwbUL0qn0KzpWYs0Aw-IWdsmsKhIjYs0ZKC5H00ULnqn0KBI1Ykn0K8IjYs0ZPl5fK9TdqGuAnqTZnVmLf0pywW5Nwj0Zw9ThI-IjYvndtsg1msnsKYIgnqP1f3PHcznWnzPjnzP1D3PWR1nfKzug7Y5HDdrHnvrH6sn1m1PWn0Tv-b5yFWPjRzPWf4nj0srjDsnhR0mLPV5HnswHb4PHDvnRujrHfvnbn0mynqnfKsUWYs0Z7VIjYs0Z7VT1Ys0ZGY5H00UyPxuMFEUHYsg1Kxn7ts0Aw9UMNBuNqsUA78pyw15HKxn7tsg100TA7Ygvu_myTqnfKsThqb5H6Yrjn4nWm1PWR0uAPGujYs0ANYpyfqQHD0mgPsmvnqn0KdTA-8mvnqn0KkUymqn0KhmLNY5H00pgPWUjYs0ZGsUZN15H00mywhUA7M5HD0UAuW5H00uAPWujY0IZF9uARqPHTsnH010AFbpyfqwRPDnYn3PWmsPHuAfHwKPjmswDcYnbcYPDnsn1RdPDm0TA7zmy4o5H00mMfqn0KEmgwL5H00ULfqn0KETMKY5H0WnanWnansc10Wna3snj0snj0WnanWnanVc108nj0snj0sc1D8nj0snj0s0Z7xIWYsQWT3g108njKxna3sn7tsQW0kg108njuxna3zPsKBTdqsThqbpyfqnHf0mLFW5HDYrjc4&ck=0.0.0.0.0.0.0.0&shh=www.baidu.com'))
getData()