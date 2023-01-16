fire = "not"

if (fire == "ok"):
    for i in range(0, aktifIHA):
        IHAs[i]["s_x"] = IHAs[i]["f_x"]
        IHAs[i]["s_y"] = IHAs[i]["f_y"]
        IHAs[i]["s_z"] = IHAs[i]["f_z"]
    for i in range(0, aktifIKA):
        IKAs[i]["s_x"] = IKAs[i]["f_x"]
        IKAs[i]["s_y"] = IKAs[i]["f_y"]
        IKAs[i]["s_z"] = IKAs[i]["f_z"]