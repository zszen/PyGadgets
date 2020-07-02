import os
import re
# from zipfile import ZipFile
import rarfile
import shutil
from PIL import Image

maxSize = 1000
path = 'image/smaller/source'

def resizeUnit(file):
    # file = '/Users/zszen/Downloads/1143个C4D创意精品模型/[11-04-16]+-+Liquidate+Iso+Virgin.jpg'
    name, ext = os.path.splitext(file)
    # print(ext)
    size = maxSize,maxSize
    im = Image.open(file)
    im.thumbnail(size)
    # im.save(name+'.thumbnail'+ext)
    im.save(file)

def smallerSizeImage():
    for k in os.listdir(path):
        if not k.lower().endswith('.jpg'):
            continue
        image = path+'/'+k
        resizeUnit(image)


print('==dealing==')

smallerSizeImage()

print('==end==')