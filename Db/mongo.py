import pymongo
import uuid

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["testdb"]
mycoll = mydb["tc"]

my_id = uuid.UUID('{00010203-0405-0607-0809-0a0b0c0d0e0f}')
#mycoll.insert({"a": my_id})


rs = mycoll.find()
for r in rs:
    print(r)


