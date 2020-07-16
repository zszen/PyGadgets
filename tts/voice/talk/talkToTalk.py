# -*- coding: utf-8 -*-
import requests, datetime, os, re, json, time, random

class TalkSelf:
    def __init__(self):
        super().__init__()
        self.data_history = os.path.dirname(__file__)+'/conf/history.conf'
        self.data_filter = os.path.dirname(__file__)+'/conf/filter.json'
        self.pool_history = []
        self.pool_history_addition = []
        self.pool_block = []
        self.pool_topic = []
        self.dic_replace = {}
        self.str_block = None
        self.ps_changeTopic = .5
        self.time_delay = .1
        self.load_conf()
        self.load_filter()
        # 实时注入
        self.pool_talkRepeat = []

    def load_conf(self):
        file = None
        try:
            file = open(self.data_history, 'r')
            for line in file.readlines():
                self.pool_history.append(line.strip('\n'))
        except:
            print('no history')

    def save_conf(self):
        # if len(self.pool_history_addition)<10:
        #     return
        with open(self.data_history, 'a') as f:
            f.write('\n'.join(self.pool_history_addition)+'\n')
            self.pool_history.extend(self.pool_history_addition)
            self.pool_history_addition = []

    def load_filter(self):
        file = None
        try:
            file = open(self.data_filter, 'r')
        except:
            file = open(self.data_filter, 'w')
        try:
            json_data = json.load(file)
            self.pool_block = json_data['block']
            self.pool_topic.extend(json_data['topic']['def'])
            # self.pool_topic.extend(json_data['topic']['animal'])
            # self.pool_topic.extend(json_data['topic']['emotion'])
            self.dic_replace = json_data['replace']
            self.str_block = '|'.join(self.pool_block)
        except:
            print('no filter')

    def changeTalk(self, talk=None):
        random.seed(random.random()*time.time())
        if talk is None:
            if self.pool_history is not None and len(self.pool_history)>0:
                talk = random.choice(self.pool_history)
                while re.search(r'(《|》|“|”|\[|\])',talk) is not None and len(talk)>15 and len(talk)<3:
                    talk = random.choice(self.pool_history)
            elif self.pool_topic is not None and len(self.pool_topic)>0:
                talk = random.choice(self.pool_topic)
            else:
                talk = "你好"
        else:
            isNeedSave = True
            if re.search('({})'.format(self.str_block),talk): # and self.ps_changeTopic>random.random():
                isNeedSave = False
                talk = random.choice(self.pool_topic)
            if talk in self.pool_history and self.ps_changeTopic>random.random():
                isNeedSave = False
                # talk = self.changeTalk() 
                # try:
                #     # res = requests.post("http://www.tuling123.com/openapi/api?key=43b9314790964a7cb6da4379eede2391&userid=951&info="+talk)
                #     # res = res.json()
                #     # talk = self.changeTalk(res["text"])
                # except :
                talk = self.changeTalk() 
            
            for i,k in enumerate(self.dic_replace):
                talk = re.sub(k,self.dic_replace[k],talk)
            if isNeedSave:
                if talk not in self.pool_history_addition:
                    self.pool_history_addition.append(talk)
                    self.save_conf()
        return talk

    def talkAI(self):
        talk = self.changeTalk()
        self.voice("话题", talk)
        while True:
            try:
                res = requests.post("http://api.qingyunke.com/api.php?key=free&appid=0&msg=" + talk)
                res = res.json()
                talk = self.changeTalk(res["content"])
            except Exception as e:
                talk = self.changeTalk()
            self.voice("小云", talk)
            
            try:
                res = requests.post("https://api.ownthink.com/bot?spoken=" + talk)
                res = res.json()
                talk = self.changeTalk(res["data"]["info"]["text"])
            except Exception as e:
                talk = self.changeTalk()
            self.voice("小思", talk)

    def voice(self, target, talk):
        print("{}：{}  ({})".format(target, talk, datetime.datetime.now()))
        # os.system('say "{}"'.format(talk))
        os.popen('say "{}"'.format(talk[0:15]))
        time.sleep(.06*len(talk))

if __name__=="__main__":
    talkSelf = TalkSelf()
    talkSelf.talkAI()