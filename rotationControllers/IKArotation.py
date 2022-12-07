from data import IKAs

for i in range(0, IKAs.len()):
    if (IKAs[i]["status"] == "1"):
        while ((IKAs[i]["e_x"] < 10) or (IKAs[i]["e_y"] < 10) or (IKAs[i]["e_ny"] < 10)
               or (IKAs[i]["e_z"] < 10) or (IKAs[i]["e_nz"] < 10)):
            # sağa gitme
            if(IKAs[i]["e_z"] > 10):
              IKAs[i]["z"] += 10  
            # sola gitme
            elif(IKAs[i]["e_z"] < 10):
              IKAs[i]["z"] -= 10    
            # geri gitme   
            if(IKAs[i]["e_x"] < 10):
              IKAs[i]["x"] -= 10
            # ileri gitme   
            if(IKAs[i]["e_x"] > 10):
              IKAs[i]["x"] += 10  