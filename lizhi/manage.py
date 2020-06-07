import re
import urllib.request
import requests
from bs4 import BeautifulSoup
import os
import json
import shutil
import sys

file_cfg = './lizhi/conf tmp.cfg'
json_data = None

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

# print(json_data)
while(True):
    lst = []
    for i,k in enumerate(json_data):
        lst.append(k)
        print('[%d] %s'%(i,k))
    dk = input('选择删除的序号 (直接enter结束):')
    if dk == '':
        break
    dkInt = int(dk)
    if dkInt<0 or dkInt>=len(lst):
        input('错误序号, 请重试')
        continue
    input('删除序号[%d] %s , 继续'%(dkInt,lst[dkInt]))
    if lst[dkInt] not in json_data.keys():
        continue
    del json_data[lst[dkInt]]

save_cfg()