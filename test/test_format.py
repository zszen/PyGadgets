import re, os, json

with open('/Users/zszen/Desktop/info.txt', 'r+') as f:
    str = f.read()
    lst = re.split(r'(\d+.*?：)',str)
    del lst[0]
    for k in range(int(len(lst)/2)):
        res = re.split(r'^(\d+)(.*?)(\((.*?)\))?：',lst[k*2])
        if res[4] is None:
            idx = res[1]
            title = '---'
            title_en = res[2]
        else:
            idx = res[1]
            title = res[2]
            title_en = res[4]
        content = lst[k*2+1].replace('\n\n','')
        res = re.split(r'^(.*)\n',content)
        if len(res)>1:
            del res[0]
            content1 = res[0]
            if len(res)>1:
                del res[0]
                content2 = ''.join(res)
                content2 = content2.replace('\n','')
        print(f'{idx}|{title_en}|{title} | {content1} | {content2}')
    