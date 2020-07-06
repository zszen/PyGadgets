from tkinter import *
from PIL import Image as Img
from PIL import ImageSequence as Ims
from tkinter.filedialog import *
from shutil import rmtree
from os import makedirs

info = {
    'path':[]
}  #用 字典型 info 来存放 所读取所有文件的 path

def make_app():
    app = Tk()
    Label(app,text='compress tool', font=('Arial', 10)).pack()
    Listbox(app, name='lbox', bg='#f2f2f2').pack(fill=BOTH, expand=True)
    Button(app,text='| pick |', command=select, bg = "blue", fg = "red").pack()
    Button(app,text='| start |', command=compress, bg = "blue", fg = "red").pack()
    app.geometry('300x400')
    return app

def compress_unit(path:str):
    in_filename = path.split('/')[-1]
    out_path='%s/img'%(os.path.dirname(__file__))   #在本程序目录下输出图片
    in_gif = Img.open(path)
    pool_gif = [i.copy() for i in Ims.Iterator(in_gif)]
    duration = in_gif.info['duration']/0.9
    index = 0
    imglist = []
    # filename = './%s' % output         #
    # makedirs(file)
    for frame in pool_gif:
        # x = 135
        # y = 10
        # w = 250
        # h = 220
        # region = frame.crop((x, y, x + w, y + h))

        frame.save(out_path+"/%d.png" % index)  #当然这里用quality=N 则下面就不需要对读出来数据处理
        im = Img.open(out_path+"/%d.png" % index)
        im.thumbnail((198, 198), Img.ANTIALIAS)  #数据处理
        imglist.append(im)
        index += 1
    imglist[0].save(out_path+"/"+in_filename, 'gif', save_all=True, append_images=imglist[1:], loop=0, duration=duration)

def compress():
     for f in info['path']:
        compress_unit(f)
        # rmtree(file)

def select():
    f_name=askopenfilenames()
    lbox=app.children['lbox']
    info ['path'] = f_name
    if info['path']:
        for name in f_name:
            lbox.insert(END, name.split('/')[-1])

app=make_app()
app.mainloop()