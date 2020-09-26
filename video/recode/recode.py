import os,re

if __name__ == "__main__":
    while True:
        f = input('video file:')
        fd = f.strip()
        fd = fd.replace('\ ',' ')
        rec = re.compile(r'(mp4|mov|m4v|avi|mkv|3gp|flv)$', re.I)
        if rec.search(fd):
            # print(os.path.exists(fd))
            os.system(f'ffmpeg -i \"{fd}\" \"{os.path.dirname(fd)}/{os.path.basename(fd)}_fix.mp4\"')
        else:
            print('error file')
        