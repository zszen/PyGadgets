##################################
####将文件夹下所有子文件夹独立打包成压缩包， （多线程
##################################
import zipfile
import os
import threading

thread_max = 4
thread_lock = threading.Lock()

def loop(fl):
    while True:
        try:
            with thread_lock:
                f = next(fl)
                print(os.path.basename(f))
        except StopIteration:
            print('end one trhead')
            break
        # print(f)
        zipme(f)
    
def zipme(f):
    path = os.path.dirname(f)

    z = zipfile.ZipFile(f'{f}.zip','w',zipfile.ZIP_DEFLATED)
    z.write(f,os.path.basename(f))

    for p,fd,fl in os.walk(f):
        rel_path = p.split(path)[1]
        for fi in fl:
            z.write(f'{p}/{fi}',f'{rel_path}/{fi}')
    z.close()


def get_folders():
    folder = input('zip folder (single for all file):')
    f = folder.rstrip()
    folder = f.replace('\ ',' ')
    print('doing....')
    for f in os.listdir(folder):
        if not os.path.isdir(f'{folder}/{f}'):
            continue
        yield f'{folder}/{f}'

if __name__ == "__main__":
    fl = get_folders()
    ts = []
    for i in range(thread_max):
        t = threading.Thread(name=f'{i}',args=(fl,), target=loop)
        ts.append(t)
        t.start()
    for t in ts:
        t.join()
    print('==end==')