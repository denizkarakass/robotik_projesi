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