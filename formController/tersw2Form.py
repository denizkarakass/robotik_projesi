from data import     IHAs
from data import     IKAs
def tersw2Form():
#IHA:4
#IKA:2
#IHAların x konumu
    o = 10
    IHAs[0]["x"] =  o +45
    IHAs[1]["x"] =  o +45
    IHAs[2]["x"] =  o +95
    IHAs[3]["x"] =  o +95
    #IHAların y konumu
    IHAs[0]["y"] =  100
    IHAs[1]["y"] =  50
    IHAs[2]["y"] =  100
    IHAs[3]["y"] =  50
    #IHAların z konumu
    IHAs[0]["z"] =  o +100
    IHAs[1]["z"] =  o +50
    IHAs[2]["z"] =  o +100 
    IHAs[3]["z"] =  o +50
    #IKAların x konumu
    IKAs[0]["x"] =  o +70
    IKAs[1]["x"] =  o +70
    #IKAların y konumu
    IKAs[0]["y"] = 0
    IKAs[1]["y"] = 0
    #IKAların z konumu
    IKAs[0]["z"] =  o 
    IKAs[1]["z"] =  o +75