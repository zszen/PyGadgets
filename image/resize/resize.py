from PIL import Image
import re,os

def get_files_input():
    files = input('resize files:')
    pool = []
    f = files.rstrip()
    files = f.replace('\ ',' ')
    if os.path.isdir(files):
        for p,fd,fi in os.walk(files):
            for f in fi:
                if not re.search(r'\.((png)|(jpg)|(jpeg))$',f):
                    continue
                pool.append(f'{p}/{f}')
    else:
        res = re.split(r'(\.((png)|(jpg)|(jpeg))) ?', files)
        for i in range(0,len(res),6):
            try:
                string = res[i]+res[i+1]

                pool.append(string)
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
    f = file_path.rstrip()
    file_path = f.replace('\ ',' ')
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