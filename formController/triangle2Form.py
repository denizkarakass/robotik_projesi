from data import IHAs
from data import IKAs
def triangle2Form():
    o = 10
#IHA:5
#IKA:1
#IHAların x konumu
    IHAs[0]["x"] = o +10
    IHAs[1]["x"] = o +40
    IHAs[2]["x"] = o +10
    IHAs[3]["x"] = o +10
    IHAs[4]["x"] = o +40

#IHAların y konumu
    IHAs[0]["y"] = 150
    IHAs[1]["y"] = 150
    IHAs[2]["y"] = 150
    IHAs[3]["y"] = 75
    IHAs[4]["y"] = 75

#IHAların z konumu
    IHAs[0]["z"] = o +20
    IHAs[1]["z"] = o +20
    IHAs[2]["z"] = o +60
    IHAs[3]["z"] = o +20
    IHAs[4]["z"] = o +60

#IKAların x konumu
    IKAs[0]["x"] =  o +10

#IKAların y konumu
    IKAs[0]["y"] = 0

#IKAların z konumu
    IKAs[0]["z"] =  o +60