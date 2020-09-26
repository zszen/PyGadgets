import os,re

def get_files_input():
    files = input('resize files:')
    # files = '/Users/zszen/Desktop/Download/twitter/EfGvEKkUYAEU1IX.png /Users/zszen/Desktop/Download/twitter/EfGvEKtUYAE4pQF.png'
    res = re.split(r'(\.((png)|(jpg)|(jpeg))) ?', files)
    pool = []
    for i in range(0,len(res),6):
        try:
            pool.append(res[i]+res[i+1])
        except:
            pass
    # print("files", len(pool))
    return pool

if __name__ == "__main__":
    while True:
        # files = get_files_input()
        for f in get_files_input():
            # f = input('image need scale:')
            f = f.rstrip()
            f = f.replace('\ ',' ')
            if not re.search(r'\.((png)|(jpg)|(jpeg)|(gif)|(bmp))', f):
                print('it\'s not image')
                # exit(0)
                continue
            filename = os.path.basename(f).split('.')[0]
            outfile = os.path.dirname(f)+'/'+filename+'_4x.png'
            os.system(f'waifu2x -t p -s 2 -n 1 -i \"{f}\" -o \"{outfile}\"')
            os.system(f'waifu2x -t p -s 2 -n 1 -i \"{outfile}\" -o \"{outfile}\"')
            print(f'done {outfile}')