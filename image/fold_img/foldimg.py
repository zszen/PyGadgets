import re,os
import shutil

folder_img = 'image'

def deal_fold():
    path = input('folder need fold image:')
    if not os.path.exists(path):
        return
    path_img = f'{path}/{folder_img}'
    if not os.path.exists(path_img):
        os.makedirs(path_img)
    if not os.path.exists(path_img):
        return
    for f in os.listdir(path):
        if not re.search(r'\.(jpg|png|gif|jpeg|webp)',f):
            continue
        shutil.move(f'{path}/{f}',path_img)
    # for p,fds,fls in os.walk(path):
    #     print(fds,fls)
    #     # if f
    #     # for fl in fls:

if __name__ == "__main__":
    while True:
        deal_fold()