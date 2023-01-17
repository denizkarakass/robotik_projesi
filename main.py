for x in range(0, 1000):
    # Veritabanından ilgili bilgileri alma START
    import pymongo
    import time
    time.sleep(0)
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

    IHAs = [IHA1, IHA2, IHA3, IHA4, IHA5, IHA6, IHA7, IHA8,
            IHA9, IHA10, IHA11, IHA12, IHA13, IHA14, IHA15, IHA16]
    IKAs = [IKA1, IKA2, IKA3, IKA4, IKA5]
# Veritabanından ilgili bilgileri alma END

# Aktif AGENT SAYISI BULMA START
    aktifIHA = 1
    aktifIKA = 1
    for i in range(0, 15):
        if (IHAs[i]["status"] == "1"):
            aktifIHA += 1
    for i in range(0, 4):
        if (IKAs[i]["status"] == "1"):
            aktifIKA += 1
# Aktif AGENT SAYISI BULMA END
    print("Araçlar tespit edildi")
    # İHA eş zamanlı kalkış START
    if x == 0:
        for i in range(0, aktifIHA):
            IHAs[i]["s_y"] += 50
        # Verileri gönderme START
        myclient = pymongo.MongoClient(
            "mongodb+srv://deniz:727302dk@cluster0.zuwnt7e.mongodb.net/?retryWrites=true&w=majority")
        mydb = myclient["test"]
        mycol = mydb["ihas"]
        mycol2 = mydb["ikas"]
        for i in range(0, aktifIHA):
            name = {"name": IHAs[i]["name"]}
            newvalues = {"$set": {
                "s_x": IHAs[i]["s_x"],
                "s_y": IHAs[i]["s_y"],
                "s_z": IHAs[i]["s_z"],
            }}
            mycol.update_one(name, newvalues)
        for i in range(0, aktifIKA):
            name2 = {"name": IKAs[i]["name"]}
            newvalues2 = {"$set": {
                "s_x": IKAs[i]["s_x"],
                "s_y": IKAs[i]["s_y"],
                "s_z": IKAs[i]["s_z"],
            }}
        mycol2.update_one(name2, newvalues2)
        print("Kalkış verileri güncellendi.")
        time.sleep(7)
        print("Kalkış tamamlandı.")
    # İHA eş zamanlı kalkış END

  # Veritabanından ilgili bilgileri alma END

    landing = "not"
    engel = "yok"

   # Rotasyon yapma eğer engel varsa START
    for i in range(0, aktifIHA):
        if IHAs[i]["e_z"] < 31 or IHAs[i]["e_nz"] < 31:
          for x in range(0,aktifIHA):  
              # yukarı çıkma
            if IHAs[i]["e_y"] > 31:
                IHAs[x]["s_y"] += 19
                # aşağı inme
            elif IHAs[i]["e_ny"] > 31:
                IHAs[x]["s_y"] -= 19
                # sağa gitme
            elif IHAs[i]["e_x"] > 31:
                IHAs[x]["s_x"] += 19
                # sola gitme
            elif IHAs[i]["e_nx"] > 31:
                IHAs[x]["s_x"] -= 19
            engel = "var"    
                
        if IHAs[i]["e_x"] < 31 or IHAs[i]["e_nx"] < 31 :
          for x in range(0,aktifIHA): 
                 # yukarı çıkma
            if IHAs[i]["e_y"] > 31:
                IHAs[x]["s_y"] += 19
                # aşağı inme
            elif IHAs[i]["e_ny"] > 31:
                IHAs[x]["s_y"] -= 19 
              # ileri gitme
            elif IHAs[i]["e_z"] > 31:
                IHAs[x]["s_z"] += 19
              # geri gitme
            elif IHAs[i]["e_nz"] > 31:
                IHAs[x]["s_z"] -= 19    
                
            engel = "var" 
                
        if IHAs[i]["e_y"] < 31 or IHAs[i]["e_ny"] < 31 :
          for x in range(0,aktifIHA):   
            print("İha " + str(i+1) + ". engelle karşılaştı. Mesafesi:" + str(IHAs[i]["e_x"]) + " " + str(
                IHAs[i]["e_nz"]) + " " + str(IHAs[i]["e_nx"]) + " " + str(IHAs[i]["e_nz"]))
                # ileri gitme
            if IHAs[i]["e_z"] > 31:
                IHAs[x]["s_z"] += 19
                # geri gitme
            elif IHAs[i]["e_nz"] > 31:
                IHAs[x]["s_z"] -= 19
                # sağa gitme
            elif IHAs[i]["e_x"] > 31:
                IHAs[x]["s_x"] += 19
                # sola gitme
            elif IHAs[i]["e_nx"] > 31:
                IHAs[x]["s_x"] -= 19

            engel = "var"

    for i in range(0, aktifIKA):
        if IKAs[i]["e_x"] < 31 or IKAs[i]["e_z"] < 31 or IKAs[i]["e_nx"] < 31 or IKAs[i]["e_nz"] < 31:
          for x in range(0,aktifIKA):   
            print("İka " + str(i+1) + ". engelle karşılaştı.")
            # sağa gitme
            if IKAs[i]["e_z"] > 31:
                IKAs[x]["s_z"] += 19
             # sola gitme
            elif IKAs[i]["e_nz"] > 31:
                IKAs[x]["s_z"] -= 19
             # geri gitme
            elif IKAs[i]["e_x"] > 31:
                IKAs[x]["s_x"] += 19
             # ileri gitme
            elif IKAs[i]["e_nx"] > 31:
                IKAs[x]["s_x"] -= 19
            engel = "var"
    myclient = pymongo.MongoClient(
                "mongodb+srv://deniz:727302dk@cluster0.zuwnt7e.mongodb.net/?retryWrites=true&w=majority")
    mydb = myclient["test"]
    mycol = mydb["ihas"]
    mycol2 = mydb["ikas"]
    for i in range(0, aktifIHA):
                name = {"name": IHAs[i]["name"]}
                newvalues = {"$set": {
                    "s_x": IHAs[i]["s_x"],
                    "s_y": IHAs[i]["s_y"],
                    "s_z": IHAs[i]["s_z"],
                }}
                mycol.update_one(name, newvalues)
    for i in range(0, aktifIKA):
                name2 = {"name": IKAs[i]["name"]}
                newvalues2 = {"$set": {
                    "s_x": IKAs[i]["s_x"],
                    "s_y": IKAs[i]["s_y"],
                    "s_z": IKAs[i]["s_z"],
                }}
                mycol2.update_one(name2, newvalues2)
    print("Rotasyon engel verileri güncellendi.")
    time.sleep(6)
    print("Rotasyon engel kontrol tamamlandı.")
 
    # Rotasyon Verilerini gönderme START
    myclient = pymongo.MongoClient(
        "mongodb+srv://deniz:727302dk@cluster0.zuwnt7e.mongodb.net/?retryWrites=true&w=majority")
    mydb = myclient["test"]
    mycol = mydb["ihas"]
    mycol2 = mydb["ikas"]
    for i in range(0, aktifIHA):
        name = {"name": IHAs[i]["name"]}
        newvalues = {"$set": {
            "s_x": IHAs[i]["s_x"],
            "s_y": IHAs[i]["s_y"],
            "s_z": IHAs[i]["s_z"],
        }}
        mycol.update_one(name, newvalues)
    for i in range(0, aktifIKA):
        name2 = {"name": IKAs[i]["name"]}
        newvalues2 = {"$set": {
            "s_x": IKAs[i]["s_x"],
            "s_y": IKAs[i]["s_y"],
            "s_z": IKAs[i]["s_z"],
        }}
        mycol2.update_one(name2, newvalues2)

    if engel == "yok":
        if (landing == "not"):
            # Navigasyon formasyon döngüsü START
            print("Araçlar navigasyon halinde.")

            # Bu kısımda hangi yöne gideceklerse o yönde ilerlemelerini sağlıyoruz sürünün.
            IHAs[0]["s_z"] += 10

            # Formasyon ve navigasyon yaptırma  START
            formasyon = "1"
            if (formasyon == "1"):
                print("Okçunun Oku Formasyonu Etkin")
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

                IKAs[0]["s_x"] = IHAs[0]["s_x"] - 40
                IKAs[0]["s_y"] = 0
                IKAs[0]["s_z"] = IHAs[0]["s_z"]

                for i in range(1, aktifIKA):
                    IKAs[i]["s_x"] = IKAs[i - 1]["s_x"]
                    IKAs[i]["s_y"] = IKAs[i - 1]["s_y"]
                    IKAs[i]["s_z"] = IKAs[i - 1]["s_z"] - 20
                # Okçunun Oku Formasyon yaptırma END
            elif (formasyon == "2"):
                print("Meşale formasyonu etkin.")
                # Meşale Formasyon yaptırma START
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

                IKAs[0]["s_x"] = IHAs[0]["s_x"] - 40
                IKAs[0]["s_y"] = 0
                IKAs[0]["s_z"] = IHAs[0]["s_z"] + 40

                for i in range(1, aktifIKA):
                    IKAs[i]["s_x"] = IKAs[i - 1]["s_x"]
                    IKAs[i]["s_y"] = IKAs[i - 1]["s_y"]
                    IKAs[i]["s_z"] = IKAs[i - 1]["s_z"] + 20
                # Meşale Formasyon yaptırma END
             # Hareket verileri gönderme START
            myclient = pymongo.MongoClient(
                "mongodb+srv://deniz:727302dk@cluster0.zuwnt7e.mongodb.net/?retryWrites=true&w=majority")
            mydb = myclient["test"]
            mycol = mydb["ihas"]
            mycol2 = mydb["ikas"]
            for i in range(0, aktifIHA):
                name = {"name": IHAs[i]["name"]}
                newvalues = {"$set": {
                    "s_x": IHAs[i]["s_x"],
                    "s_y": IHAs[i]["s_y"],
                    "s_z": IHAs[i]["s_z"],
                }}
                mycol.update_one(name, newvalues)
            for i in range(0, aktifIKA):
                name2 = {"name": IKAs[i]["name"]}
                newvalues2 = {"$set": {
                    "s_x": IKAs[i]["s_x"],
                    "s_y": IKAs[i]["s_y"],
                    "s_z": IKAs[i]["s_z"],
                }}
                mycol2.update_one(name2, newvalues2)
            print("Hareket verileri güncellendi.")
            time.sleep(10)
            print("Hareket tamamlandı.")

        # İniş Yapma
        elif (landing == "ok"):
            for i in range(0, aktifIHA):
                IHAs[i]["s_x"] = IHAs[i]["l_x"]
                IHAs[i]["s_y"] = IHAs[i]["l_y"]
                IHAs[i]["s_z"] = IHAs[i]["l_z"]
            for i in range(0, aktifIKA):
                IKAs[i]["s_x"] = IKAs[i]["l_x"]
                IKAs[i]["s_y"] = IKAs[i]["l_y"]
                IKAs[i]["s_z"] = IKAs[i]["l_z"]

             # Verileri gönderme START
            myclient = pymongo.MongoClient(
                "mongodb+srv://deniz:727302dk@cluster0.zuwnt7e.mongodb.net/?retryWrites=true&w=majority")
            mydb = myclient["test"]
            mycol = mydb["ihas"]
            mycol2 = mydb["ikas"]
            for i in range(0, aktifIHA):
                name = {"name": IHAs[i]["name"]}
                newvalues = {"$set": {
                    "s_x": IHAs[i]["s_x"],
                    "s_y": IHAs[i]["s_y"],
                    "s_z": IHAs[i]["s_z"],
                }}
                mycol.update_one(name, newvalues)
            for i in range(0, aktifIKA):
                name2 = {"name": IKAs[i]["name"]}
                newvalues2 = {"$set": {
                    "s_x": IKAs[i]["s_x"],
                    "s_y": IKAs[i]["s_y"],
                    "s_z": IKAs[i]["s_z"],
                }}
                mycol2.update_one(name2, newvalues2)
            print("İniş verileri güncellendi.")
            time.sleep(1200)
            print("iniş yaptı.")
