# encode=utf-8
import pymongo
import random

client = pymongo.MongoClient(host='localhost',port=27017)


def checkColExist():
    dblist = client.list_database_names()
    print(dblist)

def insert():
    for i in range(10):
        col = client.mydb.students
        student = {
            # '_id':'1',
            'name':random.choice('asdfghjkxzcvbnmqweruyio'),
            'age':int(random.random()*20+10),
            'gender':random.choice(['male','female']),
        }
        res = col.insert_one(student)
        print(res)

def find():
    col = client.mydb.students
    # res = col.find_one()
    # print(res)
    # for k in col.find():
    #     print(k)
    for k in col.find({"name":"h", "age":{"$ne":20}},{"_id":False}).limit(10):
        print(k)


# checkColExist()
# insert()
find()

client.close()