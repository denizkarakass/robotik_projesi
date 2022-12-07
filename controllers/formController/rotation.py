from modelController import IHAs

# Mesafe hesaplamaları
xDistance = abs(IHAs[0]["x"] - IHAs[1]["x"])
yDistance = abs(IHAs[0]["y"] - IHAs[1]["y"])
zDistance = abs(IHAs[0]["z"] - IHAs[1]["z"])

print(xDistance)

# Eğer çarpışma durumu riski olmazsa bunları uygulayacak.
if xDistance > 5:
    IHAs[0]["x"] += 10
    IHAs[1]["x"] += 10
    print("10 birim ileri")
if zDistance > 5:
    IHAs[0]["y"] += 10
    IHAs[1]["y"] += 10
    print("10 birim çapraz")

# Eğer çarpışma riski olursa bunları uygulayacak.
if xDistance < 5:
    IHAs[0]["x"] += 5
    IHAs[1]["x"] += -5  # Aradaki mesafeyi açmak için ters yöne yönlendiritoruz.
if yDistance < 5:
    IHAs[0]["y"] += 5
    IHAs[1]["y"] += -5
if zDistance < 5:
    IHAs[0]["z"] += 5
    IHAs[1]["z"] += -5


# Engele 20 birim mesafeden az kaldığı zaman kaçma hareketi yapıcak
if IHAs[0]["e-x"] < 20 and IHAs[0]["e-x"] != 0:
   IHAs[0]["y"] += 20

if IHAs[0]["e-y"] < 20 and IHAs[0]["e-y"] != 0:
   IHAs[0]["y"] += 20