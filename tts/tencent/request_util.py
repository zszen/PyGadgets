# coding=UTF-8
import urllib
import base64
import hmac
import hashlib
import requests
import configparser

auth_file_path = "./conf/tcloud_auth.ini"
param_file_path = "./conf/request_parameter.ini"

class authorization:
    AppId = 0
    SecretId = ""
    SecretKey = ""
    Expired = 3600
    conf=configparser.ConfigParser()

    def init(self):
        print("init")
        self.conf.read(auth_file_path)
        self.AppId = self.conf.getint("authorization", "AppId")
        self.SecretId = self.conf.get("authorization", "SecretId")
        self.SecretKey = self.conf.get("authorization", "SecretKey")
        print(self)

    def verify_param(self):
        if len(str(self.AppId)) == 0:
            print('AppId can not empty')
        if len(str(self.SecretId)) == 0:
            print('SecretId can not empty')
        if len(str(self.SecretKey)) == 0:
            print('SecretKey can not empty')

    def init_auth(self, appid, secret_id, secret_key):
        self.AppId = appid
        self.SecretId = secret_id
        self.SecretKey = secret_key

    def generate_sign(self, request_data):
        url = "tts.cloud.tencent.com/stream"
        sign_str = "POST" + url + "?"
        sort_dict = sorted(request_data.keys())
        for key in sort_dict:
            sign_str = sign_str + key + "=" + urllib.parse.unquote(str(request_data[key])) + '&'
        sign_str = sign_str[:-1]
        print(sign_str)
        # print(hmac.new(bytes(self.SecretKey,'utf-8'),bytes(sign_str,'utf-8'),hashlib.sha1).hexdigest())
        # print(base64.b64encode(bytes("c1a38b82f06dee2f7fcd6c1923e2c21a30167645",'utf-8')))
        bstr = hmac.new(bytes(self.SecretKey,'utf-8'),bytes(sign_str,'utf-8'),hashlib.sha1).hexdigest()
        authorization = base64.b64encode(bytes(bstr,'utf-8'))
        print(authorization)
        return authorization

class request:
    Text = "五一小长假去哪里玩啊"
    Action = "TextToStreamAudio"
    Codec = "pcm"
    Expired = 0
    ModelType = 0
    PrimaryLanguage = 1
    ProjectId = 0
    SampleRate = 16000
    SessionId = "123"
    Speed = 0
    VoiceType = 0
    Volume = 5
    conf=configparser.ConfigParser()

    def init(self):
        print("init")
        self.conf.read(param_file_path)
        self.Text = self.conf.get("parameter", "Text")
        self.Action = self.conf.get("parameter", "Action")
        self.Codec = self.conf.get("parameter", "Codec")
        self.Expired = self.conf.getint("parameter", "Expired")
        self.ModelType = self.conf.getint("parameter", "ModelType")
        self.PrimaryLanguage = self.conf.getint("parameter", "PrimaryLanguage")
        self.ProjectId = self.conf.getint("parameter", "ProjectId")
        self.SampleRate = self.conf.getint("parameter", "SampleRate")
        self.SessionId = self.conf.get("parameter", "SessionId")
        self.Speed = self.conf.getint("parameter", "Speed")
        self.VoiceType = self.conf.getint("parameter", "VoiceType")
        self.Volume = self.conf.getint("parameter", "Volume")
        print(self)

    def verify_param(self):
        if len(str(self.Action)) == 0:
            print('Action can not empty')
        if len(str(self.SampleRate)) == 0:
            print('SampleRate is not set, assignment default value 16000')
            self.SampleRate = 16000

    def init_param(self, text, action, codec, expired, model_type, prim_lan, project_id, sample_rate, session_id, speed, voice_type, volume):
        self.Action = action
        self.Text = text
        self.Codec = codec
        self.Expired = expired
        self.ModelType = model_type
        self.PrimaryLanguage = prim_lan
        self.ProjectId = project_id
        self.SampleRate = sample_rate
        self.SessionId = session_id
        self.Speed = speed
        self.VoiceType = voice_type
        self.Volume = volume

    
