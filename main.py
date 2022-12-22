# Veritabanından ilgili bilgileri alma START
import pymongo
import time
from data import IHAs
from data import IKAs
# Veritabanından ilgili bilgileri alma END

# Aktif AGENT SAYISI BULMA START
aktifIHA = 1
aktifIKA = 1
for i in range(0, 15):
    if (IHAs[i]["status"] == "1"):
        aktifIHA += 1
for i in range(0, 5):
    if (IKAs[i]["status"] == "1"):
        aktifIKA += 1
# Aktif AGENT SAYISI BULMA END
print("Araçlar tespit edildi")
# İHA eş zamanlı kalkış START
for i in range(0, aktifIHA):
    IHAs[i]["s_y"] += 50
# İHA eş zamanlı kalkış END

landing = "not"

if (landing == "not"):
    # Rotasyon navigasyon formasyon döngüsü START
    for x in range(0, 500):
        time.sleep(5)
        print("veri simülasyona gitti çalışıyor")
       
        IHAs[0]["s_z"] += 10

        # Formasyon ve navigasyon yaptırma  START
        formasyon = "1"
        if (formasyon == "1"):
            # Okçunun Oku Formasyon yaptırma START
            for i in range(1, int(aktifIHA / 2)):
                IHAs[i]["s_x"] = IHAs[i - 1]["s_x"] - 10
                IHAs[i]["s_y"] = IHAs[i - 1]["s_y"]
                IHAs[i]["s_z"] = IHAs[i - 1]["s_z"] + 10

            IHAs[int(aktifIHA/2) + 1]["s_x"] = IHAs[0]["s_x"] + 10 
            IHAs[int(aktifIHA/2) + 1]["s_y"] = IHAs[0]["s_y"]
            IHAs[int(aktifIHA/2) + 1]["s_z"] = IHAs[0]["s_z"] 

            for i in range(int(aktifIHA/2), aktifIHA):
                IHAs[i]["s_x"] = IHAs[i - 1]["s_x"] - 10
                IHAs[i]["s_y"] = IHAs[i - 1]["s_y"]
                IHAs[i]["s_z"] = IHAs[i - 1]["s_z"] - 10
                
            IKAs[0]["s_x"] = IHAs[0]["a_x"] + 10
            IKAs[0]["s_y"] = 0
            IKAs[0]["s_z"] = IHAs[0]["a_z"]
            if (aktifIKA > 0):
                for i in range(1, aktifIKA-1):
                    IKAs[i]["s_x"] = IKAs[i - 1]["s_x"]
                    IKAs[i]["s_y"] = IKAs[i - 1]["s_y"]
                    IKAs[i]["s_z"] = IKAs[i - 1]["s_z"]
            # Okçunun Oku Formasyon yaptırma END
        elif (formasyon == "2"):
            print("Formasyon 2 yazılacak.")
        # Formasyonve navigasyon yaptırma  END

        # Verileri gönderme START
        myclient = pymongo.MongoClient(
            "mongodb+srv://deniz:727302dk@cluster0.zuwnt7e.mongodb.net/?retryWrites=true&w=majority")
        mydb = myclient["test"]
        mycol = mydb["ihas"]
        mycol2 = mydb["ikas"]
        for i in range(0, aktifIHA):
            name = {"name": IHAs[i]["name"]}
            newvalues = {"$set": {
                "e_x": IHAs[i]["e_x"],
                "e_nx": IHAs[i]["e_nx"],
                "e_y": IHAs[i]["e_y"],
                "e_ny": IHAs[i]["e_ny"],
                "e_z": IHAs[i]["e_z"],
                "e_nz": IHAs[i]["e_nz"],
                "a_x": IHAs[i]["a_x"],
                "a_nx": IHAs[i]["a_nx"],
                "a_y": IHAs[i]["a_y"],
                "a_ny": IHAs[i]["a_ny"],
                "a_z": IHAs[i]["a_z"],
                "a_nz": IHAs[i]["a_nz"],
                "s_x": IHAs[i]["s_x"],
                "s_y": IHAs[i]["s_y"],
                "s_z": IHAs[i]["s_z"],
            }}
            mycol.update_one(name, newvalues)
            # Verileri gönderme END
    # Rotasyon navigasyon formasyon döngüsü END


elif (landing == "ok"):
    for i in range(0, aktifIHA):
        IHAs[i]["s_x"] = IHAs[i]["l_x"]
        IHAs[i]["s_y"] = IHAs[i]["l_y"]
        IHAs[i]["s_z"] = IHAs[i]["l_z"]
    for i in range(0, aktifIKA-1):
        IHAs[i]["s_x"] = IKAs[i]["l_x"]
        IHAs[i]["s_y"] = IKAs[i]["l_y"]
        IHAs[i]["s_z"] = IKAs[i]["l_z"]

        # Verileri gönderme START
    myclient = pymongo.MongoClient(
        "mongodb+srv://deniz:727302dk@cluster0.zuwnt7e.mongodb.net/?retryWrites=true&w=majority")
    mydb = myclient["test"]
    mycol = mydb["ihas"]
    mycol2 = mydb["ikas"]
    for i in range(0, aktifIHA):
        name = {"name": IHAs[i]["name"]}
        newvalues = {"$set": {
            "e_x": IHAs[i]["e_x"],
            "e_nx": IHAs[i]["e_nx"],
            "e_y": IHAs[i]["e_y"],
            "e_ny": IHAs[i]["e_ny"],
            "e_z": IHAs[i]["e_z"],
            "e_nz": IHAs[i]["e_nz"],
            "a_x": IHAs[i]["a_x"],
            "a_nx": IHAs[i]["a_nx"],
            "a_y": IHAs[i]["a_y"],
            "a_ny": IHAs[i]["a_ny"],
            "a_z": IHAs[i]["a_z"],
            "a_nz": IHAs[i]["a_nz"],
            "s_x": IHAs[i]["s_x"],
            "s_y": IHAs[i]["s_y"],
            "s_z": IHAs[i]["s_z"],
        }}
        mycol.update_one(name, newvalues)
        # Verileri gönderme END
