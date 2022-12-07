from data import IHAs
from data import IKAs


for i in range(0, IHAs.len()):
    if (IHAs[i]["status"] == "1"):
        while ((IHAs[i]["e_x"] < 10) or (IHAs[i]["e_py"] < 10) or (IHAs[i]["e_ny"] < 10)
               or (IHAs[i]["e_pz"] < 10) or (IHAs[i]["e_nz"] < 10)):
            # yukarı çıkma
            if (IHAs[i]["e_y"] > 10):
              IHAs[i]["y"] += 10
             # aşağı inme
            elif(IHAs[i]["e_y"] < 10):
              IHAs[i]["y"] -= 10   
            # sağa gitme
            if(IHAs[i]["e_z"] > 10):
              IHAs[i]["z"] += 10  
            # sola gitme
            elif(IHAs[i]["e_z"] < 10):
              IHAs[i]["z"] -= 10    
            # geri gitme   
            if(IHAs[i]["e_x"] < 10):
              IHAs[i]["x"] -= 10
              
        while (IHAs[i]["e-y"] < 10):
            IHAs[i]["x"] += 10
        while (IHAs[i]["e-z"] < 10):
            IHAs[i]["x"] += 10
