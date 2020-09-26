import os,re
import threading
import subprocess
import shutil

is_same_folder = True
is_remove_orgfile = True
is_detect_samename = True
is_convert_mp3 = False
output_path = f'{os.path.expanduser("~")}/Desktop/mp3recode/'
if not os.path.exists(output_path):
    os.mkdir(output_path)

lock = threading.Lock()
def loop(pool):
    while True:
        try:
            with lock:
                fp = next(pool)
        except StopIteration:
            break
        filename = os.path.basename(fp).split('.')[0]
        skip_convert = False
        if is_detect_samename and os.path.exists(f'{os.path.dirname(fp)}/{filename}.mp3'):
            skip_convert = True
        if not skip_convert:
            if is_same_folder:
                cmd = f'ffmpeg -i \"{fp}\" -codec:a libmp3lame -qscale:a 2 \"{os.path.dirname(fp)}/{filename}.mp3\"'
            else:
                cmd = f'ffmpeg -i \"{fp}\" -codec:a libmp3lame -qscale:a 2 \"{output_path}{filename}.mp3\"'
            p = subprocess.Popen(args=cmd , shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True)
            for line in iter(p.stdout.readline, b''):
                print(f'{line}')
            p.stdout.close()
            p.wait()
        if is_remove_orgfile:
            os.remove(fp)

def getlist(folder):
    folder = folder.rstrip()
    folder = folder.replace('\ ',' ')
    if os.path.isdir(folder):
        for p,fd,fl in os.walk(folder):
            for fp in fl:
                if is_convert_mp3:
                    if fp.startswith('.') or not re.search(r'\.(mp3|wav|ogg|mp4|mkv|m4a|m4v|avi|mpeg|wma|wmv)', fp.lower()):
                        continue
                else:
                    if fp.startswith('.') or not re.search(r'\.(wav|ogg|mp4|mkv|m4a|m4v|avi|mpeg|wma|wmv)', fp.lower()):
                        continue
                yield p+'/'+fp
    else:
        yield 

if __name__ == "__main__":
    folder = input('folder to convert:')
    pool = getlist(folder)
    ths = []
    for k in range(20):
        t = threading.Thread(target=loop, name=f'thread k', args=(pool,))
        t.start()
        ths.append(t)
    for k in ths:
        k.join()
    print('==end==')