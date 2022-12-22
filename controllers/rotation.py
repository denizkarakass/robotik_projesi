from data import IHAs
from data import IKAs
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
            # ileri gitme
            if (IHAs[i]["e_x"] > 30):
                IHAs[i]["s_x"] += 10
            # geri gitme
            elif (IHAs[i]["e_nx"] > 30):
                IHAs[i]["s_x"] -= 10

for i in range(0, aktifIKA-1):
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
