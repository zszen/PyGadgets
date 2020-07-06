import os

def speechIt(str):
    os.system("say %s"%str)
    # os.system("say hello")

speechIt('你好')