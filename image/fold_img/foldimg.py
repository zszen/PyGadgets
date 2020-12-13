import re,os
import shutil

folder_img = 'image'

def deal_fold():
    path = input('folder need fold image:')
    path = path.strip(' ')
    if not os.path.exists(path):
        print('no path')
        return
    path_img = f'{path}/{folder_img}'
    if not os.path.exists(path_img):
        os.makedirs(path_img)
    if not os.path.exists(path_img):
        print('image path not exit')
        return
    for f in os.listdir(path):
        f_low = f.lower()
        if not re.search(r'\.(jpg|png|gif|jpeg|webp)',f_low):
            continue
        target_img = f'{path_img}/{f}'
        if os.path.exists(target_img):
            os.remove(target_img)
        # shutil.copyfile(f'{path}/{f}',f'{path_img}/{f}')
        shutil.move(f'{path}/{f}',f'{path_img}')
        # os.system('')
    # for p,fds,fls in os.walk(path):
    #     print(fds,fls)
    #     # if f
    #     # for fl in fls:

if __name__ == "__main__":
    while True:
        deal_fold()