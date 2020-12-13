import os,re
import requests,urllib
import ssl
import threading
import shutil
# import urllib2

# context = ssl._create_unverified_context()
# print(urllib2.urlopen("https://www.youku.com/", context=context).read())

thread_num = 50
path_savelist = 'm3u8/'
link_site_path = 'https://yj.yongjiu6.com'

# def together_links(f):
#     with open(f,'r') as file:
#         t = ''
#         ls = file.readlines()
#         for line in ls:
#             if re.search(r'.*\.ts$',line):
#                 if re.search(r'^http',line):
#                     t+=line
#                 else:
#                     t+=link_site_path+line
#         with open(path_savelist+'list.txt', 'w+') as fw:
#             fw.write(t)

# def download():
#     with open(path_savelist+'list.txt', 'r') as f:
#         fs = f.readlines()
#         max = len(fs)
#         for idx,fl in enumerate(fs):
#             fl = fl.strip()
#             # print(f'{idx+1}/{len(fs)}')
#             # download_single(idx+1,fl)
#             yield idx+1,max,fl

def combin():
    result = []
    paths = os.listdir(f"{path_savelist}list")
    for path in paths:
        if path.find(".ts")<0:
            continue
        result.append(path)
    result.sort(key= lambda x:int(x[-6:-3]))
    # print()
    # print(result)
    # os.system(f'ffmpeg -i "concat:{}" -c copy {output}.mp4')
    str_combin = path_savelist+'list/'+f'|{path_savelist}list/'.join(result)
    output = f'{path_savelist}output.mp4'
    os.system(f'ffmpeg -i "concat:{str_combin}" -c copy {output}')
    print('合并完毕 output.mp4')

# def Schedule_cmd(blocknum, blocksize, totalsize):
#     speed = (blocknum * blocksize) / (time.time() - start_time)
#     # speed_str = " Speed: %.2f" % speed
#     speed_str = " Speed: %s" % format_size(speed)
#     recv_size = blocknum * blocksize

#     # 设置下载进度条
#     # f = sys.stdout
    # pervent = recv_size / totalsize
    # percent_str = "%.2f%%" % (pervent * 100)
    # n = round(pervent * 50)
    # s = ('#' * n).ljust(50, '-')
    # f.write(percent_str.ljust(8, ' ') + '[' + s + ']' + speed_str)
    # f.flush()
    # time.sleep(0.1)
    # f.write('\r')

# def download_single(info):
#     idx = info[0]
#     max = info[1]
#     link = info[2]
#     res = re.search(r'[^/]+(?!.*/)', link)
#     # filename = res.group(0)
#     filename = f'{idx}'
#     filepath = f'{path_savelist}list/{filename}.ts'
#     if os.path.exists(filepath):
#         print(f'跳过完成: {idx}/{max} {filename}')
#         return
#     else:
#         print(f'正在下载: {idx}/{max} {filename}')
#     # urllib.request.urlretrieve(url=link, filename=f'{path_savelist}list/{filename}',reporthook=Schedule_cmd) 
#     r = requests.get(link, stream=False)
#     with open(filepath,'wb') as f:
#         f.write(r.content)
#     print(f'完成: {idx}/{max} {filename}')

# lock = threading.Lock()

# def loop(pool):
#     while True:
#         try:
#             with lock:
#                 data = next(pool)
#         except StopIteration:
#             break
#         download_single(data)

if __name__ == "__main__":
    while True:
        # f = input('clear list folder [y/N]:')
        # if f=='y':
        #     shutil.rmtree(f'{path_savelist}list')
        #     os.mkdir(f'{path_savelist}list')
        # # f = input('m3u8 file:')
        # # f = f.strip(' ')
        # f = 'm3u8/index.m3u8'
        # together_links(f)
        # # download()
        # pool = download()
        # pool_thread = []
        # for i in range(thread_num):
        #     thread = threading.Thread(target=loop,name=f'i',args=(pool,))
        #     thread.start()
        #     pool_thread.append(thread)
        # for k in pool_thread:
        #     k.join()
        # print('==多线程下载结束==')
        combin()
        break

        