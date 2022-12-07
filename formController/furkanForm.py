from data import IHAs
from data import IKAs


def furkanForm():
    # IKA:1
    # IHA:7
    o = 20
    # IHAların x konumu
    IHAs[0]["x"] = + o + 10
    IHAs[1]["x"] = + o + 29
    IHAs[2]["x"] = + o + 125
    IHAs[3]["x"] = + o + 106
    IHAs[4]["x"] = + o + 77
    IHAs[5]["x"] = + o + 51
    IHAs[6]["x"] = + o + 93
    # IHAların y konumu
    IHAs[0]["y"] = + 100
    IHAs[1]["y"] = + 100
    IHAs[2]["y"] = + 100
    IHAs[3]["y"] = + 100
    IHAs[4]["y"] = + 100

    IHAs[5]["y"] = + 100
    IHAs[6]["y"] = + 100
    # IHAların z konumu
    IHAs[0]["z"] = + o
    IHAs[1]["z"] = + o + 106
    IHAs[2]["z"] = + o + 37
    IHAs[3]["z"] = + o + 92
    IHAs[4]["z"] = + o + 59


    IHAs[5]["z"] = + o + 77
    IHAs[6]["z"] = + o + 13
    # IKAların x konumu
    IKAs[0]["x"] = + o + 63
    # IKAların y konumu
    IKAs[0]["y"] = + 0
    # IKAların z konumu
    IKAs[0]["z"] = + o + 71
