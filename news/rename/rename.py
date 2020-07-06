import os
import re
# import shutil

path = ''
reg = r'(S\d{2}E\d{2}).*(\.mp4|\.mpeg|\.rmvb|\.mkv)'

for k in os.listdir(path):
    res = re.search(reg, k)
    if res:
        os.rename(path+k, path+res.group(1)+res.group(2))
        
# for k in os.listdir('./'):
#     # print(k)
#     if re.search(r'\.rmvb',k):
#         res = re.search(r'第(\d+)集',k)
#         count = int(res.group(1))
#         os.rename(k,'%02d.rmvb'%count)
#         # print(res.group(1))
#         pass