from data import     IHAs
from data import     IKAs
def squareForm():
#IHA:4
#IKA:2
#IHAların x konumu
    o = 10
    IHAs[0]["x"] =  o +25
    IHAs[1]["x"] =  o +25
    IHAs[2]["x"] =  o +75
    IHAs[3]["x"] =  o +75
    #IHAların y konumu
    IHAs[0]["y"] =  100
    IHAs[1]["y"] =  100
    IHAs[2]["y"] =  100
    IHAs[3]["y"] =  100
    #IHAların z konumu
    IHAs[0]["z"] =  o +100
    IHAs[1]["z"] =  o +50
    IHAs[2]["z"] =  o +100 
    IHAs[3]["z"] =  o +50
    #IKAların x konumu
    IKAs[0]["x"] =  o +50
    IKAs[1]["x"] =  o +50
    #IKAların y konumu
    IKAs[0]["y"] = 0
    IKAs[1]["y"] = 0
    #IKAların z konumu
    IKAs[0]["z"] =  o 
    IKAs[1]["z"] =  o +75
    