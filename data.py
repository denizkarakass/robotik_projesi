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
IHA10 = mycol.find_one({"name": "İHA10"})
IHA11 = mycol.find_one({"name": "İHA11"})
IHA12 = mycol.find_one({"name": "İHA12"})
IHA13 = mycol.find_one({"name": "İHA13"})
IHA14 = mycol.find_one({"name": "İHA14"})
IHA15 = mycol.find_one({"name": "İHA15"})
IHA16 = mycol.find_one({"name": "İHA16"})

IKA1 = mycol2.find_one({"name": "İKA1"})
IKA2 = mycol2.find_one({"name": "İKA2"})
IKA3 = mycol2.find_one({"name": "İKA3"})
IKA4 = mycol2.find_one({"name": "İKA4"})
IKA5 = mycol2.find_one({"name": "İKA5"})
IKA6 = mycol2.find_one({"name": "İKA6"})
IKA7 = mycol2.find_one({"name": "İKA7"})
IKA8 = mycol2.find_one({"name": "İKA8"})


IHAs = [IHA1, IHA2, IHA3, IHA4, IHA5, IHA6, IHA7, IHA8,
        IHA9, IHA10, IHA11, IHA12, IHA13, IHA14, IHA15, IHA16]
IKAs = [IKA1, IKA2, IKA3, IKA4, IKA5, IKA6, IKA7, IKA8]
