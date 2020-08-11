from PIL import Image
from PIL import PsdImagePlugin
import re

def get_size():
    f = input('image file:')
    f = f.rstrip()
    f = f.replace('\ ',' ')
    print(f)
    if not re.search(r'\.((png)|(jpg)|(jpeg)|(gif)|(bmp))', f):
        print('it\'s not image')
        # exit(0)
        return
    im = Image.open(f)
    print(f'图片大小是{im.size}')
    im.close()

if __name__ == "__main__":
    while 1:
        get_size()