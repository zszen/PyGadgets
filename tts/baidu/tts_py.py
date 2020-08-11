# coding: utf-8
from aip import AipSpeech
from enum import Enum
import os
import sys
import time
sys.path.append(os.path.dirname(__file__)+'/../../')
from core.audio import game
# import pygame
from playsound import playsound
import codecs
import json

# https://console.bce.baidu.com/ai/#/ai/speech/app/list
with open('core/data.json') as f:
    info = json.load(f)
    app_id = info['apikey']['baiduai']['APPID']
    api_key = info['apikey']['baiduai']['APIKey']
    secret_key = info['apikey']['baiduai']['APISecret']


class VoiceType(Enum):
    woman = 0
    man = 1
    oldman = 3
    girl = 4

class baip:
    def __init__(self):
        self.client = AipSpeech(app_id, api_key, secret_key)

    def deal(self, str, voice:VoiceType):
        res = self.client.synthesis(str, 'zh', 1, {
            'vol': 5,
            'per': voice.value,
        })

        file_path_tmp = os.path.dirname(__file__)+'/'+'voice.mp3'
        file_path = u'/users/zszen/Desktop/'+str+'.mp3'
        if not isinstance(res, dict):
            with codecs.open(file_path, 'wb') as f:
                f.write(res)
            with codecs.open(file_path_tmp, 'wb') as f:
                f.write(res)
            playsound(file_path_tmp)
            # game.audioplay().play(file_path)
            print(file_path)
        else:
            print(res)

if __name__ == "__main__":
    p = baip()
    # p.deal('这不是我想要的', VoiceType.woman)
    who = [VoiceType.woman,VoiceType.man,VoiceType.woman,VoiceType.oldman,VoiceType.girl]
    while True:
        talk_who = input('输入发音人(0女，1男，3老，4孩)：')
        talk_str = input('输入内容：')
        
        p.deal(talk_str, who[min(max(int(talk_who),0),4)])
        