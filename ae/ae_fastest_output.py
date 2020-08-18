import threading
import os
import sys
sys.path.append(os.path.dirname(__file__)+'/..')
import subprocess
import time
import re

# 线程数量
core_num = 9
fps = 30
# aerender 位置
path_aerender = '/Applications/Adobe After Effects CC 2019/aerender'
# path_output = '~/Desktop/output.mp4'
# 处理速度
render_count = 0
render_count_his = 0
fps_count = render_count-render_count_his

lock = threading.Lock()
def loop_thread(idx):
    global render_count, tm, render_count_his, fps_count
    p = subprocess.Popen(args=f'"{path_aerender}" -project {path_project4output}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True)
    for line in iter(p.stdout.readline, b''):
        print(line)
        # linestr = line.decode('gb2312')
        # print(linestr)
        # linestr = str(line,'unicode')
        # if not re.search(r'Seconds', linestr):
        #     continue
        # if re.search(r'Skipping', linestr):
        #     continue
        # render_count+=1
        # if time.time()-tm>1:
        #     tm = time.time()
        #     fps_count = render_count-render_count_his
        #     render_count_his = render_count
        #     print(f'处理速度：{fps_count} fps')
    p.stdout.close()
    p.wait()
    print(f'线程 {idx} 结束 !')
    # p.communicate()

if __name__ == "__main__":
    print('*'*20+' start '+'*'*20)
    print(f'线程数：{core_num}')
    # 项目文件位置
    render_count = 0
    path_project4output = input('项目文件地址：')
    # filename = os.path.basename(path_project4output)
    # ffmpeg_cmd = f'ffmpeg -threads {core_num} -y -r {fps} -i '
    print('等待启动ae核心')
    tm_total = time.time()
    tm = time.time()
    threads = []
    for i in range(0,core_num):
        t = threading.Thread(target=loop_thread, name=f'thread{i}', args=(i,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    print(f'使用{time.time()-tm_total}s时间')
    print('*'*20+' end '+'*'*20)