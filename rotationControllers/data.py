import pymongo
myclient = pymongo.MongoClient(
    "mongodb+srv://deniz:727302dk@cluster0.zuwnt7e.mongodb.net/?retryWrites=true&w=majority")
mydb = myclient["test"]
mycol = mydb["ihas"]
mycol2 = mydb["ikas"]

IHA1 = mycol.find_one({"name": "İHA1"})
IHA2 = mycol.find_one({"name": "İHA2"})
IHA3 = mycol.find_one({"name": "İHA3"}) 
IHA4 = mycol.find_one({"name": "İHA4"})
IHA5 = mycol.find_one({"name": "İHA5"})
IHA6 = mycol.find_one({"name": "İHA6"})
IHA7 = mycol.find_one({"name": "İHA7"})
IHA8 = mycol.find_one({"name": "İHA8"})
IHA9 = mycol.find_one({"name": "İHA9"})

IKA1 = mycol2.find_one({"name": "İKA1"})
IKA2 = mycol2.find_one({"name": "İKA2"})
IKA3 = mycol2.find_one({"name": "İKA3"})



IHAs = [IHA1, IHA2, IHA3, IHA4, IHA5, IHA6, IHA7, IHA8, IHA9]
IKAs = [IKA1, IKA2, IKA3]
