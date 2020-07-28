from aip import AipSpeech
from enum import Enum
import os
import sys
import time
sys.path.append(os.path.dirname(__file__)+'/../../')
from core.audio import game
# import pygame
from playsound import playsound

# https://console.bce.baidu.com/ai/#/ai/speech/app/list
app_id = '21659659'
api_key = '9s2OPYG6AXi4HQyWUMQGclCG'
secret_key = 'NerueBTX1FpdhABl5RgGr3DmVKmdzEdw'

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

        file_path = os.path.dirname(__file__)+'/'+'voice.mp3'
        if not isinstance(res, dict):
            with open(file_path, 'wb') as f:
                f.write(res)
            # game.audioplay().play(file_path)
            time.sleep(.2)
            print(file_path)
            playsound(file_path)
        else:
            print(res)

if __name__ == "__main__":
    p = baip()
    p.deal('节后返程注意，前方路段拥挤，请您', VoiceType.girl)