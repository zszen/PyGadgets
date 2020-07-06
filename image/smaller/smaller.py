import os
import re
# from zipfile import ZipFile
import rarfile
import shutil
from PIL import Image


def resizeUnit(file, *, size=None, scale=None):
    # file = '/Users/zszen/Downloads/1143个C4D创意精品模型/[11-04-16]+-+Liquidate+Iso+Virgin.jpg'
    name, ext = os.path.splitext(file)
    # print(ext)
    im = Image.open(file)
    # print(im.size)
    if size is not None:
        if im.size[0]<=size[0] and im.size[1]<=size[1]:
            im.close()
            return
        im.thumbnail(size)
        print(file)
    elif scale is not None:
        size = im.size[0]*scale, im.size[1]*scale
        im.thumbnail(size)
        print(file)
    im.save(file)
    im.close()

def smallerSizeImage():
    for k in os.listdir(path):
        if not k.lower().endswith('.jpg') and not k.lower().endswith('.png'):
            continue
        image = path+'/'+k
        size = maxSize,maxSize
        resizeUnit(image, size=size)
        # resizeUnit(image, scale=.5)


print('==dealing==')

maxSize = 1136
path = '/Users/Shared/Relocated Items/Security/Developer/xcode/projects/game_dev/121020BubbleShooter/res.svn/待分析/物理碰撞app/simbols/s'
smallerSizeImage()

print('==end==')