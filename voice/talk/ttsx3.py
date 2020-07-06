import pyttsx3

engine = pyttsx3.init()
# engine.setProperty('voice', 'zh')
engine.say("你好")
engine.runAndWait()