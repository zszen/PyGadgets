from PIL import Image
import re,os

def get_files_input():
    files = input('resize files:')
    res = re.split(r'(\.((png)|(jpg)|(jpeg))) ?', files)
    pool = []
    for i in range(0,len(res),6):
        try:
            pool.append(res[i]+res[i+1])
        except:
            pass
    print("files", len(pool))
    return pool

def get_resize_info():
    resize = input('resize(128 or 64x128): ')
    resize = re.split(r'x',resize)
    for i,k in enumerate(resize):
        try:
            resize[i] = int(k)
        except:
            print('need numbers')
            return get_resize_info()
    return resize

def deal_resize(file_path, resize):
    im = Image.open(file_path)
    if len(resize)==1:
        size = resize[0],resize[0]
    else:
        size = resize[0],resize[1]
    im.thumbnail(size)
    im.save(file_path)
    im.close()

if __name__ == "__main__":
    resize = get_resize_info()
    files = get_files_input()
    for k in files:
        deal_resize(k,resize)
    print('===done===')