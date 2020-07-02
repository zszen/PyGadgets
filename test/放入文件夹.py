import os
import re
# from zipfile import ZipFile
import rarfile
import shutil
from PIL import Image


path = '/Users/zszen/Downloads/1143个C4D创意精品模型/'

def makeDirAndSetIn():
    for k in os.listdir(path):
        if os.path.isdir(path+k):
            # print(1)
            continue
        else:
            file = path+k
            if file.endswith('.rar'):
                # print(k)
                res = re.search(r'(.*?)\.rar',k)
                if res:
                    # print(res.group(1))
                    os.makedirs(path+res.group(1))
                    os.rename(path+k, path+res.group(1)+'/'+k)
                    print([path+k, path+res.group(1)+'/'+k])
                    # exit()

def copyTxtToEachDir():
    file = 'readme.txt'
    for k in os.listdir(path):
        if os.path.isdir(path+k):
            isNeedCopy = True
            for j in os.listdir(path+k):
                if file==j:
                    isNeedCopy = False
            if isNeedCopy:
                os.system('cp -i %s %s'%(path+file, path+k))

def unzipSomeFolder():
    folders = ('缩略图','预览图')
    folder = '缩略图'
    for k in os.listdir(path):
        if os.path.isdir(path+k):
            if os.path.exists(path+k+'/'+folders[0]) or os.path.exists(path+k+'/'+folders[1]):
                continue
            for j in os.listdir(path+k):
                file = path+k+'/'+j
                if file.endswith('.rar'):
                    rf = rarfile.RarFile(file)
                    # print(k,re.search(r'(.*\.rar)',k))
                    # for f in rf.infolist():
                    #     print(f.filename , k+'/'+folder)
                    #     if f.filename == k+'/'+folder:
                    #         print('ok')
                    try:
                        rf.extract(k+'/'+folder, path=path+k, pwd='yshqxxpt')
                        shutil.move(path+k+'/'+k+'/'+folder, path+k)
                        shutil.rmtree(path+k+'/'+k)
                    except Exception as e:
                        print(e)
                    print(k)
                    # with ZipFile(file,'r') as zipObj:
                    #     print(zipObj.namelist())
                    # ZipFile.namelist()
                    # ZipFile.extract('folder', )
                    # exit()

def resizeUnit(file):
    # file = '/Users/zszen/Downloads/1143个C4D创意精品模型/[11-04-16]+-+Liquidate+Iso+Virgin.jpg'
    name, ext = os.path.splitext(file)
    # print(ext)
    size = 400,400
    im = Image.open(file)
    im.thumbnail(size)
    # im.save(name+'.thumbnail'+ext)
    im.save(file)

def resizeAllImage():
    for k in os.listdir(path):
        # if k!='443个 精品工程收集':
        #     continue
        if os.path.isdir(path+k):
            for j in os.listdir(path+k):
                if os.path.isdir(path+k+'/'+j):
                    count = 0
                    for l in os.listdir(path+k+'/'+j):
                        if not l.lower().endswith('.jpg') and not l.lower().endswith('.png'):
                            # print(l)
                            continue
                        image = path+k+'/'+j+'/'+l
                        count+=1
                        resizeUnit(image)
                        # print(image)
                        # exit()
                    print(k,count)

def combinAlThumb():
    toPath = '缩略图/'
    for k in os.listdir(path):
        if os.path.isdir(path+k):
            for j in os.listdir(path+k):
                if os.path.isdir(path+k+'/'+j):
                    if not os.path.exists(path+toPath+k):
                        shutil.copytree(path+k+'/'+j, path+toPath+k)
                    # os.rename(path+toPath+j, path+toPath+k)

print('====starting=====')

# makeDirAndSetIn()
# copyTxtToEachDir()
# unzipSomeFolder()
# resizeUnit()
# resizeAllImage()
combinAlThumb()

print('====done=====')