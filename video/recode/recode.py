import os,re

if __name__ == "__main__":
    while True:
        f = input('video file:')
        fd = f.strip()
        fd = fd.replace('\ ',' ')
        rec = re.compile(r'(mp4|mov|m4v|avi|mkv|3gp|flv|webm|rmvb|rm)$', re.I)
        filename = os.path.splitext(os.path.basename(fd))[0]
        if rec.search(fd):
            # print(os.path.exists(fd))
            os.system(f'ffmpeg -i \"{fd}\" \"{os.path.dirname(fd)}/{filename}_fix.mp4\"')
        else:
            print('error file')
        