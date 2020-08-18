import os,re
import threading
import subprocess

output_path = '/Users/zszen/Desktop/mp3recode/'
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
        cmd = f'ffmpeg -i \"{fp}\" -codec:a libmp3lame -qscale:a 2 \"{output_path}{filename}.mp3\"'
        p = subprocess.Popen(args=cmd , shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True)
        for line in iter(p.stdout.readline, b''):
            print(f'{line}')
        p.stdout.close()
        p.wait()

def getlist(folder):
    for p,fd,fl in os.walk(folder):
        for fp in fl:
            if fp.startswith('.') or not re.search(r'\.(mp3|mp4|mkv|m4a|m4v|avi|mpeg|wma|wmv|wav)', fp.lower()):
                continue
            yield p+'/'+fp

if __name__ == "__main__":
    folder = input('folder to convert:')
    if os.path.isdir(folder):
        pool = getlist(folder)
        ths = []
        for k in range(20):
            t = threading.Thread(target=loop, name=f'thread k', args=(pool,))
            t.start()
            ths.append(t)
        for k in ths:
            k.join()
    else:
        folder = folder.rstrip()
        folder = folder.replace('\ ',' ')
        os.system(f'ffmpeg -i \"{folder}\" -codec:a libmp3lame -qscale:a 2 \"{output_path}{os.path.basename(folder)}\"')
    print('==end==')