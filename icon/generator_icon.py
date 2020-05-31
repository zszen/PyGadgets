# encoding=utf-8
# -*- coding: utf-8 -*-
import os
import os.path
from PIL import Image
rootdir=os.path.abspath('.')
os.path.join(rootdir,'ios')

# type 输出图片类型（png, gif, jpeg...）

def ResizeImage(filein, fileout, width, height, type):
    img = Image.open(filein)
    # resize image with high-quality
    out = img.resize((width, height),Image.ANTIALIAS) 
    out.save(fileout, type)


a=[1024,512,180,167,152,144,120,114,100,87,80,76,72,60,58,57,50,40,29,20]
for i in a:
    ResizeImage(rootdir+'/icon.png',rootdir+'/ico/'+str(i)+'.png',i,i,'png')