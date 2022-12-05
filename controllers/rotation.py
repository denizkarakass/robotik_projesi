from modelController import IKHAs

# Mesafe hesaplamaları
xDistance = abs(IKHAs[0]["x"] - IKHAs[1]["x"])
yDistance = abs(IKHAs[0]["y"] - IKHAs[1]["y"])
zDistance = abs(IKHAs[0]["z"] - IKHAs[1]["z"])

print(xDistance)

# Eğer çarpışma durumu riski olmazsa bunları uygulayacak.
if xDistance > 5:
    IKHAs[0]["x"] += 10
    IKHAs[1]["x"] += 10
    print("10 birim ileri")
if zDistance > 5:
    IKHAs[0]["y"] += 10
    IKHAs[1]["y"] += 10
    print("10 birim çapraz")

# Eğer çarpışma riski olursa bunları uygulayacak.
if xDistance < 5:
    IKHAs[0]["x"] += 5
    IKHAs[1]["x"] += -5  # Aradaki mesafeyi açmak için ters yöne yönlendiritoruz.
if yDistance < 5:
    IKHAs[0]["y"] += 5
    IKHAs[1]["y"] += -5
if zDistance < 5:
    IKHAs[0]["z"] += 5
    IKHAs[1]["z"] += -5


# Engele 20 birim mesafeden az kaldığı zaman kaçma hareketi yapıcak
if IKHAs[0]["e-x"] < 20 and IKHAs[0]["e-x"] != 0:
   IKHAs[0]["y"] += 20

if IKHAs[0]["e-y"] < 20 and IKHAs[0]["e-y"] != 0:
   IKHAs[0]["y"] += 20