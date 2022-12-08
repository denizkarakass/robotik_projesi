from data import IHAs
from data import IKAs
def futbolteamForm():
    #IKA:1
    #IHA:10
    #IKA kaleci
    #IHA geri kalan takım
    o = 50
    #IHAların x konumu
    IHAs[0]["x"]=o + 40
    IHAs[1]["x"]=o + 60
    IHAs[2]["x"]=o + 80
    IHAs[3]["x"]=o + 100
    IHAs[4]["x"]=o + 50
    IHAs[5]["x"]=o + 70
    IHAs[6]["x"]=o + 90
    IHAs[7]["x"]=o + 50
    IHAs[8]["x"]=o + 70
    IHAs[9]["x"]=o + 90
    #IHAların y konumu
    IHAs[0]["y"]= 100
    IHAs[1]["y"]= 100
    IHAs[2]["y"]= 100
    IHAs[3]["y"]= 100
    IHAs[4]["y"]= 100
    IHAs[5]["y"]= 100
    IHAs[6]["y"]= 100
    IHAs[7]["y"]= 100
    IHAs[8]["y"]= 100
    IHAs[9]["y"]= 100
    #IHAların z konumu
    IHAs[0]["z"]=  o + 40
    IHAs[1]["z"]=  o + 40
    IHAs[2]["z"]=  o + 40
    IHAs[3]["z"]=  o + 40
    IHAs[4]["z"]=  o + 70
    IHAs[5]["z"]=  o + 70
    IHAs[6]["z"]=  o + 70
    IHAs[7]["z"]=  o + 100
    IHAs[8]["z"]=  o + 100
    IHAs[9]["z"]=  o + 100
    #IKAların x konumu
    IKAs[0]["x"]= +o + 70
    #IKAların y konumu    
    IKAs[0]["y"]= 0
    #IKAların z konumu    
    IKAs[0]["z"] =o + 20
