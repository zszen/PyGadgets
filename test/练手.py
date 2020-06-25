import re
import enum
import asyncio
import threading
import inspect
import ctypes

def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")

def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)

def BigLetter(matched):
    return matched.group(1).upper()


def f1():
    print('=1=')
    str_in = "I?���love�??�the�?great�?�?wall�in��?beijing"
    str_out = str_in
    # 修正大小写
    str_out = re.sub(r'\?(\w)', BigLetter, str_out)
    # 去掉不必要的问号
    str_out = re.sub(r'(\?|�)', ' ', str_out)
    # 去掉不必要的空格
    str_out = re.sub(r' {2,4}', ' ', str_out)
    print(str_out)

list_empty = []
def f2(val):
    if val==0:
        print('=2=')
    global list_empty
    list_empty.append(val)
    f2(val+2) if val<100 else print(list_empty)
        
# list_sequence = []

# class SequenceType(enum.Enum):
#     quence=0,
#     custom=1,

# async def f3(*,delay,func):
#     await asyncio.sleep(delay)
#     func()

# def callback1(n):
#     print('n {}'.format(n))


f1()
f2(0)

# def a():
#     print('a')
# 
# def b():
#     print('b')
# 
# def c():
#     print('c')
# 
# loop = asyncio.get_event_loop()
# loop = asyncio.get_event_loop()
# ft = asyncio.Future()
# loop.run_until_complete(f3(delay=5,func=a))
# loop.run_until_complete(f3(delay=3,func=b))
# loop.run_until_complete(f3(delay=10,func=c))
# try:
#     loop.run_forever()
# finally:
#     loop.close()

def f3(loop):
    asyncio.set_event_loop(loop)
    
    async def a():
        while True:
            print('a')
            await asyncio.sleep(1)

    async def b():
        while True:
            print('b')
            await asyncio.sleep(2)
    
    future = asyncio.gather(a(), b())
    loop.run_until_complete(future)

# loop_thread = None
# def f3_thread(*,func):
loop_thread = asyncio.new_event_loop()
t = threading.Thread(target=f3, args=(loop_thread,))
t.daemon = True
t.start()
    # return t


# t = f3_thread(func=f3)

loop_main = asyncio.get_event_loop()
async def m():
    global t
    while True:
        await asyncio.sleep(4)
        if t!=None:
            stop_thread(t)
            t = None
loop_main.run_until_complete(m())