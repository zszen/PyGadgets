# 首先先通过官方网站登陆设置把文章下载下来, 将文字放到org目录下
import os
import re
import requests

curFolderPath = None
curFileName = None

re_mdLink = r'(\!\[.*?\]\((.*?)\))'
re_siteAndFile = r'^https?://([^/]+).+?([^/]+)\?.+$'

def mkdir_recurse(path):
    if not os.path.exists(path):
        mkdir_recurse(os.path.dirname(path))
        if not os.path.exists(path):
            os.makedirs(path)

def replace_title(matched):
    return matched.group(1)+'# '+matched.group(2)
            
def replace_localImg(matched):
    url = matched.group(2)
    res = re.search(re_siteAndFile, url)
    filename = res.group(2)
    if not os.path.exists(curFolderPath+'/img/'+filename):
        res = requests.get(url)
        mkdir_recurse(curFolderPath+'/img/')
        with open(curFolderPath+'/img/'+filename, 'wb') as f:
            f.write(res.content)
    return '![](./img/%s)'%filename

def markdown_download():
    global curFolderPath
    global curFileName
    file_count = 0
    file_cur = 0
    for root,dirs,files in os.walk(top=os.path.dirname(__file__)+'/org'):
        file_count+=len(files)
    for root,dirs,files in os.walk(top=os.path.dirname(__file__)+'/org'):
        for fileName in files:
            file_cur+=1
            if fileName.startswith('.'):
                print(f'==[skip] {fileName}== {file_cur+1}/{file_count}')
                continue
            # root = '/Users/zszen/Desktop/后期/爬虫.荔枝FM/blog/jianshu/org/区块链游戏'
            # fileName = '安装顺序.md'
            path_converted = root.replace('/org/','/converted/')
            mkdir_recurse(path_converted)
            curFolderPath = path_converted
            curFileName = fileName
            filePath_org = root + '/'+fileName
            filePath_converted = path_converted +'/'+fileName
            f = open(filePath_org, 'r')
            fw = open(filePath_converted,'w')
            fw.write('# -= %s =-\n\n'%re.sub(r'\.md','',curFileName))
            all_percent = int((file_cur+1)/file_count*100)
            print(f'{all_percent}% =={fileName}==')
            fr = f.readlines()
            line_num = len(fr)
            for i,line in enumerate(fr):
                line = re.sub(r'(\!\[.*?\]\((.*?)\))', replace_localImg, line)
                line = re.sub(r'^(#{1,7}) ?(.+)$',replace_title, line)
                fw.write(line)
                ps = int((i+1)/line_num*20)
                ps_percent = int((i+1)/line_num*100)
                print('='*ps+'-'*(20-ps)+f' {ps_percent}%\r', end='')
            # return

if __name__ == "__main__":
    markdown_download()
    print('\n==done==')