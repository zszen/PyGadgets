import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print('请说～')
    audio = r.listen(source)

query = r.recognize_sphinx(audio, language='zh-CN')
print(query)