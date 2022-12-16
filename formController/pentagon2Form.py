from data import IHAs
from data import IKAs
def pentagon2Form():
#IHA:4
#IKA:1
#IHAların x konumu
    o = 10
    IHAs[0]["x"] = o +10
    IHAs[1]["x"] = o +15,0
    IHAs[2]["x"] = o +35,0
    IHAs[3]["x"] = o +40,12

#IHAların y konumu
    IHAs[0]["y"] = 50
    IHAs[1]["y"] = 100
    IHAs[2]["y"] = 50
    IHAs[3]["y"] = 100

#IHAların z konumu
    IHAs[0]["z"] = o +29.34
    IHAs[1]["z"] = o +10
    IHAs[2]["z"] = o +10
    IHAs[3]["z"] = o +29.34

#IKAların x konumu
    IKAs[0]["x"] = o +25,

#IKAların y konumu
    IKAs[0]["y"] = 0

#IKAların z konumu
    IKAs[0]["z"] = o +41,84
