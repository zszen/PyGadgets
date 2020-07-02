import os
from lxml import etree
from bs4 import BeautifulSoup

webfile = f'{os.path.dirname(__file__)}/test_baidu.html'

def parseStr():
    f = open(webfile,'r')
    str = f.read()
    html = etree.HTML(str)
    res = etree.tostring(html)
    print(res.decode('utf-8'))

def parsePage():
    html = etree.parse(webfile, etree.HTMLParser())
    res = etree.tostring(html)
    print(res.decode('utf-8'))

def parseEl():
    html = etree.parse(webfile, etree.HTMLParser())
    res = html.xpath('//span/input[@class="s_ipt"]/@maxlength')
    print(res)

def bs():
    f = open(webfile,'r')
    str = f.read()
    bs = BeautifulSoup(str, 'lxml')
    print(bs.span.input)

def parselxml():
    # root = '<root><child1>child1 test</child1><child2>child2 test</child2></root>123'
    root = '''<div class="result c-container new-pmd" id="1" srcid="205" tpl="se_com_default" data-click="{&quot;rsv_bdr&quot;:&quot;0&quot;,&quot;p5&quot;:1}" acblock="0"><h3 class="t"><a data-click="{
			'F':'778317EA',
			'F1':'9D73F1E4',
			'F2':'4CA6DD6B',
			'F3':'54E5243F',
			'T':'1593697087',
						'y':'B37FDDCF'
												}" href="http://tieba.baidu.com/p/5914871028" target="_blank" ac_redirectstatus="2">现在<em>X99</em>平台上什么<em>cpu</em>啊_图拉丁吧_百度贴吧</a><button style="display:unset;" class="ghhider ghhb" href="http://tieba.baidu.com/p/5914871028" meta="tieba.baidu.com" data-host="tieba.baidu.com" title="点击即可屏蔽 null 放开，需要在自定义中手动配置放开" acenv="0" ac_redirectstatus="2">block</button></h3><div class="c-row c-gap-top-small"><div class="general_image_pic c-span3" style="position:relative;top:2px;"><a class="c-img c-img3 c-img-radius-large" style="height:85px" href="http://tieba.baidu.com/p/5914871028" target="_blank" ac_redirectstatus="2"><img class="c-img c-img3 c-img-radius-large" src="https://dss2.bdstatic.com/6Ot1bjeh1BF3odCf/it/u=53483642,1469185123&amp;fm=85&amp;app=92&amp;f=JPEG?w=121&amp;h=75&amp;s=4A86C80B06A534BA0E81C8960300A023" style="height:85px;"><span class="c-img-border c-img-radius-large">&nbsp;-&nbsp;tieba.baidu.com</span></a></div><div class="c-span9 c-span-last"><p class="f13 c-color-gray2">回复数: 171 发贴时间: 2018年10月15日</p><div class="c-abstract"><div>1楼: 捡漏捡了张16美金的<em>x99</em>..正好室友想...</div><div>6楼: 前排压压预算..室友只有500美金装机...</div></div><div class="f13 c-gap-top-xsmall se_st_footer"><a target="_blank" href="http://www.baidu.com/link?url=RW2f5CRI6dME6eJo-yAt4CIvsjBUMYk5-iwjQzQKmQonG9jIsFhWiBYh4cl19AUs" class="c-showurl c-color-gray" style="text-decoration:none;position:relative;"><div class="c-img c-img-circle c-gap-right-xsmall" style="display: inline-block;width: 16px;height: 16px;position: relative;top: 3px;"><span class="c-img-border c-img-source-border c-img-radius-large"></span><img src="https://timg01.bdimg.com/timg?pacompress=&amp;imgtype=0&amp;sec=1439619614&amp;autorotate=1&amp;di=0b474c1dcc0a8fb2f4c854e2aa1a4641&amp;quality=90&amp;size=b870_10000&amp;src=http%3A%2F%2Fpic.rmb.bdstatic.com%2Fe276f64f216d357e1fc0b6e78f2693c8.png"></div>百度贴吧</a><div class="c-tools c-gap-left" id="tools_13330069501643714082_1" data-tools="{&quot;title&quot;:&quot;现在X99平台上什么cpu啊_图拉丁吧_百度贴吧&quot;,&quot;url&quot;:&quot;http://www.baidu.com/link?url=RW2f5CRI6dME6eJo-yAt4CIvsjBUMYk5-iwjQzQKmQonG9jIsFhWiBYh4cl19AUs&quot;}"><i class="c-icon f13"></i></div><span class="c-icons-outer"><span class="c-icons-inner"></span></span><a data-click="{'rsv_snapshot':'1'}" href="http://cache.baiducontent.com/c?m=9f65cb4a8c8507ed4fece76310508c31490797634b87834e29938448e435061e5a24febc2c21160ed6c67e670bbb0c01aaa639383c0837b7ea99ca0d&amp;p=c9759a46d6c11df404a2c7710f518c&amp;newp=9e759a46d6c102ec0be2966f1c5594231610db2151d4d6176b82c825d7331b001c3bbfb423281605d7ce7f6c07af4c58edf43178350923a3dda5c91d9fb4c57479cb64&amp;s=9d8b0f029490d14d&amp;user=baidu&amp;fm=sc&amp;query=x99+cpu&amp;qid=ab035a400012f8d5&amp;p1=1" target="_blank" class="m c-gap-left c-color-gray kuaizhao">百度快照</a></div></div></div><div><ul class="subLink_answer" style="padding-top: 6px;"><li><h4 class="f14"><a href="http://www.baidu.com/link?url=WaRhpB5Nu57QwNHz9h7ObxUwzRsoZl-Asg8DcTM7LO6FcrPRC6jsxX-xYh_7lu0u" target="_blank"><em>X99</em>上什么u最有性价比?_图拉丁吧</a></h4><div style="margin-top: 1px;"><span class="date">2019年01月05日</span><i class="subLink_answer_dis date">-</i><em>X99</em>上什么u最有性..5820k 999(能超轻松4.5,缺点在华硕板子上只能2...</div></li><li><h4 class="f14"><a href="http://www.baidu.com/link?url=WaRhpB5Nu57QwNHz9h7ObxUwzRsoZl-Asg8DcTM7LO5PS5N0TSfLbjD6J94-GPKM" target="_blank">你们<em>x99</em>主板上的是什么<em>cpu</em>_图拉丁吧</a></h4><div><span class="date">2017年03月08日</span><i class="subLink_answer_dis date">-</i>你们<em>x99</em>主板上的是..我觉得大部分都是e5 2683 v3... 你们<em>x99</em>主板...</div></li></ul><a href="http://www.baidu.com/link?url=-2JHZJyk0IvczXdrS06kzosXXzbQN-l0TmfqvGDNk0AuapuLXB7D5W1Se97SYTSfz6IFO2jAcFYl5VuwR5-atoLeYa8Ypp0pTREVoho3uLW" target="_blank" class="c c-gap-top-xsmall" style="display:block;">更多同站结果&gt;</a></div></div>
            <div class="result c-container new-pmd" id="1" srcid="205" tpl="se_com_default" data-click="{&quot;rsv_bdr&quot;:&quot;0&quot;,&quot;p5&quot;:1}" acblock="0"><h3 class="t"><a data-click="{
			'F':'778317EA',
			'F1':'9D73F1E4',
			'F2':'4CA6DD6B',
			'F3':'54E5243F',
			'T':'1593697087',
						'y':'B37FDDCF'
												}" href="http://tieba.baidu.com/p/5914871028" target="_blank" ac_redirectstatus="2">现在<em>X99</em>平台上什么<em>cpu</em>啊_图拉丁吧_百度贴吧</a><button style="display:unset;" class="ghhider ghhb" href="http://tieba.baidu.com/p/5914871028" meta="tieba.baidu.com" data-host="tieba.baidu.com" title="点击即可屏蔽 null 放开，需要在自定义中手动配置放开" acenv="0" ac_redirectstatus="2">block</button></h3><div class="c-row c-gap-top-small"><div class="general_image_pic c-span3" style="position:relative;top:2px;"><a class="c-img c-img3 c-img-radius-large" style="height:85px" href="http://tieba.baidu.com/p/5914871028" target="_blank" ac_redirectstatus="2"><img class="c-img c-img3 c-img-radius-large" src="https://dss2.bdstatic.com/6Ot1bjeh1BF3odCf/it/u=53483642,1469185123&amp;fm=85&amp;app=92&amp;f=JPEG?w=121&amp;h=75&amp;s=4A86C80B06A534BA0E81C8960300A023" style="height:85px;"><span class="c-img-border c-img-radius-large">&nbsp;-&nbsp;tieba.baidu.com</span></a></div><div class="c-span9 c-span-last"><p class="f13 c-color-gray2">回复数: 171 发贴时间: 2018年10月15日</p><div class="c-abstract"><div>1楼: 捡漏捡了张16美金的<em>x99</em>..正好室友想...</div><div>6楼: 前排压压预算..室友只有500美金装机...</div></div><div class="f13 c-gap-top-xsmall se_st_footer"><a target="_blank" href="http://www.baidu.com/link?url=RW2f5CRI6dME6eJo-yAt4CIvsjBUMYk5-iwjQzQKmQonG9jIsFhWiBYh4cl19AUs" class="c-showurl c-color-gray" style="text-decoration:none;position:relative;"><div class="c-img c-img-circle c-gap-right-xsmall" style="display: inline-block;width: 16px;height: 16px;position: relative;top: 3px;"><span class="c-img-border c-img-source-border c-img-radius-large"></span><img src="https://timg01.bdimg.com/timg?pacompress=&amp;imgtype=0&amp;sec=1439619614&amp;autorotate=1&amp;di=0b474c1dcc0a8fb2f4c854e2aa1a4641&amp;quality=90&amp;size=b870_10000&amp;src=http%3A%2F%2Fpic.rmb.bdstatic.com%2Fe276f64f216d357e1fc0b6e78f2693c8.png"></div>百度贴吧</a><div class="c-tools c-gap-left" id="tools_13330069501643714082_1" data-tools="{&quot;title&quot;:&quot;现在X99平台上什么cpu啊_图拉丁吧_百度贴吧&quot;,&quot;url&quot;:&quot;http://www.baidu.com/link?url=RW2f5CRI6dME6eJo-yAt4CIvsjBUMYk5-iwjQzQKmQonG9jIsFhWiBYh4cl19AUs&quot;}"><i class="c-icon f13"></i></div><span class="c-icons-outer"><span class="c-icons-inner"></span></span><a data-click="{'rsv_snapshot':'1'}" href="http://cache.baiducontent.com/c?m=9f65cb4a8c8507ed4fece76310508c31490797634b87834e29938448e435061e5a24febc2c21160ed6c67e670bbb0c01aaa639383c0837b7ea99ca0d&amp;p=c9759a46d6c11df404a2c7710f518c&amp;newp=9e759a46d6c102ec0be2966f1c5594231610db2151d4d6176b82c825d7331b001c3bbfb423281605d7ce7f6c07af4c58edf43178350923a3dda5c91d9fb4c57479cb64&amp;s=9d8b0f029490d14d&amp;user=baidu&amp;fm=sc&amp;query=x99+cpu&amp;qid=ab035a400012f8d5&amp;p1=1" target="_blank" class="m c-gap-left c-color-gray kuaizhao">百度快照</a></div></div></div><div><ul class="subLink_answer" style="padding-top: 6px;"><li><h4 class="f14"><a href="http://www.baidu.com/link?url=WaRhpB5Nu57QwNHz9h7ObxUwzRsoZl-Asg8DcTM7LO6FcrPRC6jsxX-xYh_7lu0u" target="_blank"><em>X99</em>上什么u最有性价比?_图拉丁吧</a></h4><div style="margin-top: 1px;"><span class="date">2019年01月05日</span><i class="subLink_answer_dis date">-</i><em>X99</em>上什么u最有性..5820k 999(能超轻松4.5,缺点在华硕板子上只能2...</div></li><li><h4 class="f14"><a href="http://www.baidu.com/link?url=WaRhpB5Nu57QwNHz9h7ObxUwzRsoZl-Asg8DcTM7LO5PS5N0TSfLbjD6J94-GPKM" target="_blank">你们<em>x99</em>主板上的是什么<em>cpu</em>_图拉丁吧</a></h4><div><span class="date">2017年03月08日</span><i class="subLink_answer_dis date">-</i>你们<em>x99</em>主板上的是..我觉得大部分都是e5 2683 v3... 你们<em>x99</em>主板...</div></li></ul><a href="http://www.baidu.com/link?url=-2JHZJyk0IvczXdrS06kzosXXzbQN-l0TmfqvGDNk0AuapuLXB7D5W1Se97SYTSfz6IFO2jAcFYl5VuwR5-atoLeYa8Ypp0pTREVoho3uLW" target="_blank" class="c c-gap-top-xsmall" style="display:block;">更多同站结果&gt;</a></div></div>'''
    html = etree.HTML(root)
    tags = html.xpath('//div/h3/a')
    for k in tags:
        print(k.xpath('string()'))
        print(k.xpath('@href')[0])

# parseStr()
# parsePage()
# parseEl()
# bs()
parselxml()