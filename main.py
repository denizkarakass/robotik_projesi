# Veritabanından ilgili bilgileri alma START
from data import IHAs
from data import IKAs
# Veritabanından ilgili bilgileri alma END

# Aktif AGENT SAYISI BULMA START
aktifIHA = 1
aktifIKA = 1
for i in range(0, 9):
    if (IHAs[i]["status"] == "1"):
        aktifIHA += 1
for i in range(0, 2):
    if (IKAs[i]["status"] == "1"):
        aktifIKA += 1
# Aktif AGENT SAYISI BULMA END

# İHA eş zamanlı kalkış START
for i in range(0, aktifIHA + 1):
    IHAs[i]["s_y"] += 50
# İHA eş zamanlı kalkış END

# Rotasyon, navigasyon ve formasyon döngüsü START
sayac = 1
for x in range(0, sayac):
 sayac += 1
 # Rotasyon yapma eğer engel varsa START
 for i in range(0, aktifIHA):
    if ((IHAs[i]["e_x"] < 30) or IHAs[i]["e_y"] < 30 or IHAs[i]["e_z"] < 30
            or IHAs[i]["e_nx"] < 30 or IHAs[i]["e_ny"] < 30 or IHAs[i]["e_nz"] < 30):
        # yukarı çıkma
        if (IHAs[i]["e_y"] > 30):
            IHAs[i]["s_y"] += 10
        # aşağı inme
        elif (IHAs[i]["e_ny"] > 30):
            IHAs[i]["s_y"] -= 10
        # sağa gitme
        if (IHAs[i]["e_z"] > 30):
            IHAs[i]["s_z"] += 10
        # sola gitme
        elif (IHAs[i]["e_nz"] > 30):
            IHAs[i]["s_z"] -= 10
        # geri gitme
        if (IHAs[i]["e_x"] > 30):
            IHAs[i]["s_x"] += 10
        # ileri gitme
        elif (IHAs[i]["e_nx"] > 30):
            IHAs[i]["s_x"] -= 10
            
 for i in range(0, aktifIKA):
    if ((IKAs[i]["e_x"] < 30) or IKAs[i]["e_y"] < 30 or IKAs[i]["e_z"] < 30
            or IKAs[i]["e_nx"] < 30 or IKAs[i]["e_ny"] < 30 or IKAs[i]["e_nz"] < 30):
        # sağa gitme
        if (IKAs[i]["e_z"] > 30):
            IKAs[i]["s_z"] += 10
        # sola gitme
        elif (IKAs[i]["e_nz"] > 30):
            IKAs[i]["s_z"] -= 10
        # geri gitme
        if (IKAs[i]["e_x"] > 30):
            IKAs[i]["s_x"] += 10
        # ileri gitme
        elif (IKAs[i]["e_nx"] > 30):
            IKAs[i]["s_x"] -= 10
 # Rotasyon yapma eğer engel varsa END
 
 #Formasyonlar yaptırma ve navigasyon START
 formasyon = "1"
 if(formasyon == "1"):
   # Yılan Üçlemesi Formasyon yaptırma START
   for i in range(1,int(aktifIHA / 2) + 1 ):
    IHAs[i]["s_x"] = IHAs[i - 1]["a_x"] + 10
    IHAs[i]["s_y"] = IHAs[i - 1]["a_y"]
    IHAs[i]["s_z"] = IHAs[i - 1]["a_z"] + 10
    
   IHAs[int(aktifIHA/2) + 1]["s_x"] = IHAs[0]["a_x"] + 10
   IHAs[int(aktifIHA/2) + 1]["s_y"] = IHAs[0]["a_y"]
   IHAs[int(aktifIHA/2) + 1]["s_z"] = IHAs[0]["a_z"] + 10    
   
   for i in range(int(aktifIHA/2) + 2 ,aktifIHA):
    IHAs[i]["s_x"] = IHAs[i - 1]["a_x"] + 10
    IHAs[i]["s_y"] = IHAs[i - 1]["a_y"]
    IHAs[i]["s_z"] = IHAs[i - 1]["a_z"] + 10
   IKAs[0]["s_x"]  = IHAs[0]["a_x"] + 10
   IKAs[0]["s_y"]  = 0
   IKAs[0]["s_z"]  = IHAs[0]["a_z"]
   if(aktifIKA > 0):
    for i in range(1, aktifIKA):
      IKAs[i]["s_x"] = IKAs[i - 1]["a_x"]
      IKAs[i]["s_y"] = IKAs[i - 1]["a_y"]
      IKAs[i]["s_z"] = IKAs[i - 1]["a_z"]           
  # Yılan Üçlemesi Formasyon yaptırma END
 elif(formasyon == "2"):
     print("Formasyon 2 yazılacak.")
 #Formasyonlar yaptırma ve navigasyon END  
# Rotasyon, navigasyon ve formasyon döngüsü END

landing = "not"
if(landing == "ok"):
    for i in range(0,aktifIHA):
        IHAs[i]["s_x"] = IHAs[i]["l_x"]
        IHAs[i]["s_y"] = IHAs[i]["l_y"]
        IHAs[i]["s_z"] = IHAs[i]["l_z"] 
    for i in range(0,aktifIKA):
        IHAs[i]["s_x"] = IKAs[i]["l_x"]
        IHAs[i]["s_y"] = IKAs[i]["l_y"]
        IHAs[i]["s_z"] = IKAs[i]["l_z"] 
            