from data import IHAs
from data import IKAs
 #IHA:4
 #IKA:3

def aForm():
    o = 10
    #IHAların x konumu
    IHAs[0]["x"] = o 
    IHAs[1]["x"] = o + 60
    IHAs[2]["x"] = o + 60
    IHAs[3]["x"] = o 
    #IHAların y konumu
    IHAs[0]["y"] = 100
    IHAs[1]["y"] = 100
    IHAs[2]["y"] = 100
    IHAs[3]["y"] = 100
    #IHAların z konumu
    IHAs[0]["z"] = o 
    IHAs[1]["z"] = o 
    IHAs[2]["z"] = o + 60
    IHAs[3]["z"] = o + 60
    #IKAların x konumu
    IKAs[0]["x"] = o + 30
    IKAs[1]["x"] = o + 60
    IKAs[2]["x"] = o 
    #IKAların y konumu
    IKAs[0]["y"] = 0
    IKAs[1]["y"] = 0
    IKAs[2]["y"] = 0
    #IKAların z konumu
    IKAs[0]["z"] = o + 90
    IKAs[1]["z"] = o + 120
    IKAs[2]["z"] = o + 120