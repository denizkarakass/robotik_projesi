# 9 İHA ve 3 İKA ile oluşturulan formasyon
# üstte yıldız şekli alıp altta üçgen şekli alıyor

from data import     IKAs
from data import     IHAs


def triangleStar2Form():
    o = 30
    IHAs[0]["x"] = o
    IHAs[1]["x"] = o + 10
    IHAs[2]["x"] = o - 10
    IHAs[3]["z"] = o 
    IHAs[4]["z"] = o - 20
    IHAs[5]["x"] = o + 10
    IHAs[5]["z"] = o 
    IHAs[6]["x"] = o - 10
    IHAs[6]["z"] = o - 20
    IHAs[7]["x"] = o - 10
    IHAs[7]["z"] = o 
    IHAs[8]["x"] = o + 10
    IHAs[8]["z"] = o - 20

    IKAs[0]["x"] = o
    IKAs[0]["z"] = o - 5
    IKAs[1]["x"] = o + 5
    IKAs[1]["z"] = o - 10
    IKAs[2]["x"] = o - 5
    IKAs[2]["z"] = o - 10


