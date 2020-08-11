import os
from PIL import Image
import xmltodict
import json
import difflib
import re
import shutil
import threading

fix_path = '/fixed/'

def warning_tip(info):
    print('warning %s'%info)

def find_tps(path):
    for path,folderNames, fileNames in os.walk(path):
        for f in fileNames:
            if not f.endswith('.tps'):
                continue
            yield (path,f)

def parse_tps(tps):
    with open(tps) as f:
        tps_res = xmltodict.parse(f.read())
        filename = tps_res['data']['struct']['array'][1]['filename']
        png_path_f = tps_res['data']['struct']['filename'][0]
        plist_path_f = tps_res['data']['struct']['map'][0]['struct'][0]['filename']
        conf =tps_res['data']['struct']['array'][0]['struct']
        folders = tps_res['data']['struct']['array'][1]['filename']
        for k in conf:
            if k['string'][0] is None:
                k['string'][0] = ""
            png_path = png_path_f.replace('{v}',k['string'][0])
            plist_path = plist_path_f.replace('{v}',k['string'][0])
            scale = float(k['double'])
            yield (plist_path, png_path, folders, scale)
        
def str2list(str):
    return [int(k) for k in re.sub(r'(\{|\})', '',str).split(',')]

def parse_plist(path, ps):
    res_dic = [ps[2]+'/'+k for k in os.listdir(path+'/'+ps[2])]
    # res_dic.extend([ps[2][1]+'/'+k for k in os.listdir(path+'/'+ps[2])])
    with open(path+'/'+ps[0],'r') as f:
        pd = xmltodict.parse(f.read())
    png_size = str2list(pd['plist']['dict']['dict'][1]['string'][2])
    res_img = Image.new('RGBA', png_size)
    for i,k in enumerate(pd['plist']['dict']['dict'][0]['key']):
        v = pd['plist']['dict']['dict'][0]['dict'][i]
        r = 'true' in v
        f = str2list(v['string'][3])
        res = difflib.get_close_matches(k,res_dic,1,0)[0]
        filename = res.lower()
        if not filename.endswith('.jpg') and not filename.endswith('.jpeg') and not filename.endswith('.png') and not filename.endswith('.gif'):
            continue
        s_small = str2list(v['string'][1])
        s = str2list(v['string'][2])
        org_f = Image.open(path+'/'+res)
        if r:
            org_f = org_f.transpose(Image.ROTATE_270)
        if ps!=1:
            if r:
                org_f = org_f.resize((s[1], s[0]))
            else:
                org_f = org_f.resize(s)
        rect = (f[0],f[1])
        org_f = org_f.crop(((s[0]-s_small[0])/2,(s[1]-s_small[1])/2, org_f.size[0], org_f.size[1]))
        rgba = org_f.split()

        if len(rgba)==4:
            res_img.paste(org_f, rect, mask=rgba[3])
        else:
            res_img.paste(org_f, rect)
    res_img.save(path+fix_path+os.path.split(ps[1])[1])
    shutil.copyfile(path+'/'+ps[0], path+fix_path+os.path.split(ps[0])[1])

lock = threading.Lock()

def deal_threading(tpss):
    while True:
        try:
            with lock:
                t = next(tpss)
        except StopIteration:
            break
        print(f'dealing {t[1]}')
        plists = parse_tps(t[0]+'/'+t[1])
        for p in plists:
            print(f'dealing {p[0]}')
            parse_plist(t[0], p)

if __name__ == "__main__":
    # tpss = find_tps('./')
    tp_path = input('tps path: ')
    tpss = find_tps(tp_path)
    threads = []
    for i in range(0,1):
        t = threading.Thread(target=deal_threading, name=f'thread{i}', args=(tpss,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    print('done')
