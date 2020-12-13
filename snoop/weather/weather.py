from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from pyecharts.charts import Line3D,Bar,Bar3D,Scatter3D
from pyecharts import options as opts
from pyecharts.globals import ThemeType
import re
import time
import json

# def init():
#     headers = {
#         'Referer': start_url,  # 注意加上referer
#         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.30 Safari/537.36'
#     }

url_format = 'https://m.tianqi.com/lishi/changping/%%DATE%%.html'

# for i in range(2011,2021):
#     print(i)
datas = {}
with open('snoop/weather/data.json','r') as f:
    datas = json.load(f)

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36",
    "referer": "https://api.bilibili.com/x/web-interface/search/all/v2?context=&page=1&order=&keyword=%E7%BC%96%E7%A8%8B&duration=&tids_1=&tids_2=&__refresh__=true&highlight=1&single_column=0&jsonp=jsonp&callback=__jp2"
}


# print("r", r.content)
# with open('snoop/weather/cache.html','w+') as f:
    # f.write(hbody.text)


def getTemprature(val):
    bs = BeautifulSoup( val, features='lxml')
    area = bs.find_all('div','count_temp')
    # print(area[0].find_all('h4'))
    # print(area[0].find_all('h5'))
    vals = area[0].find_all('h5')
    hi = re.search(r'\-?\d+',vals[0].string)
    lo = re.search(r'\-?\d+',vals[1].string)
    # print("hi", hi)
    # data = {'high':int(hi.group(0)), 'low':int(lo.group(0))}
    data = [int(hi.group(0)), int(lo.group(0))]
    return data




# grap = Line3D()
# grap.add('2020',['9','10','11','12'],[1,2,3,6,8])
# grap.show_config()
# es = EffectScatter('tu')
# es.add_xaxis('xx',['9','10','11','12'],[1,2,3,6,8])
# grap.render()

bar = (
    Scatter3D(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    # .add_xaxis(["2017", "2018", "2019", "2020"])
    # .add_yaxis("10月", [5, 20, 36, 10])
    # .add('北京气温',[[2019,10,10],[2020,10,11]],itemstyle_opts=opts.ItemStyleOpts(color='red'),)
    # .add('北京气温',[[2019,10,3],[2020,10,4]],itemstyle_opts=opts.ItemStyleOpts(color='blue'),)
    # .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(max_=20),
    )
)

# with open('snoop/weather/cache.html','r') as f:
#     te = getTemprature(f.read())
#     datas[2020] = {10,te}
    # bar.add('北京气温',[[10,2020,te['low']],[10,2020,te['high']]],itemstyle_opts=opts.ItemStyleOpts(color='red'),)

# for y in range(2020,2011-1, -1): 
#     # y = 2019
#     for m in range(9,13):
#         print(f'{y}/{m}')
#         time.sleep(.2)
#         url = url_format.replace('%%DATE%%',f'{y}{str(m).zfill(2)}')
#         hbody = requests.get(url,headers=headers)
#         te = getTemprature(hbody.content)
#         if y not in datas:
#             datas[y] = {}
#         datas[y][m]=te
    
# with open('snoop/weather/data.json','w+') as f:
#     str = json.dumps(datas)
#     print("str", str)
#     f.write(str)

# arr_hi = []
# for k in datas:
#     # print(k)
#     for j in datas[k]:
#         if datas[k][j][0]==0:
#             continue
#         arr_hi.append([int(j),int(k),datas[k][j][0]])
# # print("arr_hi", arr_hi)
# bar.add('北京气温',arr_hi,itemstyle_opts=opts.ItemStyleOpts(color='red'),)

arr_lo = []
for k in datas:
    # print(k)
    for j in datas[k]:
        if datas[k][j][1]==0 and datas[k][j][0]==0:
            continue
        arr_lo.append([int(j),int(k),datas[k][j][1]])
# print("arr_hi", arr_hi)
bar.add('北京气温',arr_lo,itemstyle_opts=opts.ItemStyleOpts(color='red'),)

bar.render('snoop/weather/weather.html')
# render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# 也可以传入路径参数，如 bar.render("mycharts.html")