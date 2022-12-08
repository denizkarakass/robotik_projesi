from data import     IHAs
from data import     IKAs
def newmoonForm():
#IKA:3
#IHA:7
    o = 10   
#IHAların x konumu
    IHAs[0]["x"] += o + 100
    IHAs[1]["x"] += o + 50
    IHAs[2]["x"] += o + 30
    IHAs[3]["x"] += o + 10
    IHAs[4]["x"] += o + 30
    IHAs[5]["x"] += o + 50
    IHAs[6]["x"] += o + 100
#IHAların y konumu
    IHAs[0]["y"] += 100
    IHAs[1]["y"] += 100
    IHAs[2]["y"] += 100
    IHAs[3]["y"] += 100
    IHAs[4]["y"] += 100
    IHAs[5]["y"] += 100
    IHAs[6]["y"] += 100
#IHAların z konumu
    IHAs[0]["z"] += o + 60
    IHAs[1]["z"] += o + 100
    IHAs[2]["z"] += o + 80
    IHAs[3]["z"] += o + 50
    IHAs[4]["z"] += o + 20
    IHAs[5]["z"] += o + 10
    IHAs[6]["z"] += o + 40
#IKAların x konumu
    IKAs[0]["x"] += o + 75
    IKAs[1]["x"] += o + 50
    IKAs[2]["x"] += o + 75
#IKAların y konumu
    IKAs[0]["y"] += 0
    IKAs[1]["y"] += 0
    IKAs[2]["y"] += 0
#IKAların z konumu
    IKAs[0]["z"] += o + 70
    IKAs[1]["z"] += o + 50
    IKAs[2]["z"] += o + 30