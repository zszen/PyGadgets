import os
import threading

org_path = os.path.dirname(__file__)+'/org/'
output_path = os.path.dirname(__file__)+'/done/'

def getfile():
    for img in os.listdir('res'):
        imglow = img.lower()
        if not imglow.endswith('jpg') and not imglow.endswith('png') and not imglow.endswith('jpeg'):
            continue
        outfile = output_path+img+'.png'
        if os.path.exists(outfile):
            continue
        yield img
        # os.system(f'waifu2x -t p -s 2 -n 1 -i {org_path+img} -o {outfile}')
    # break

# os.system(f'waifu2x')

lock = threading.Lock()

def deal_threading(imgs):
    while True:
        try:
            with lock:
                img = next(imgs)
        except StopIteration:
            break
        outfile = output_path+img+'.png'
        os.system(f'waifu2x -t p -s 2 -n 1 -i {org_path+img} -o {outfile}')

if __name__ == "__main__":
    print('deal starting ')
    files = getfile()
    threads = []
    for i in range(0,10):
        t = threading.Thread(target=deal_threading, name=f'thread{i}', args=(files,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    print('done')