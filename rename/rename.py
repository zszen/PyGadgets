import os
import re
# import shutil

path = '/Volumes/media2/movie/超级蜱人/'
reg = r'(S\d{2}E\d{2}).*(\.mp4)'

for k in os.listdir(path):
    res = re.search(reg, k)
    if res:
        os.rename(path+k, path+res.group(1)+res.group(2))
        