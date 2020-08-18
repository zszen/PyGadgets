from PIL import Image
import re
# from skimage import io,color
# import skimage


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


if __name__ == "__main__":
    fs = get_files_input()
    for fp in fs:
        # rgb = skimage.io.imread(fp)
        # lab = skimage.color.rgb2lab(rgb)
        # print(lab)
        # im = Image.open(fp)
        # im.show()
