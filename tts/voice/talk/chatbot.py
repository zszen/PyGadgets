from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot('Training demo')
trainer = ListTrainer(chatbot)

trainer.train([
    "你好",
    "你好,很高兴认识你",
    "你叫什么名字?",
    "我叫Siri",
])


print(chatbot.get_response('你好?'))
print(chatbot.get_response('你叫什么名字?'))

bot = Bot()

