from modelController import İKHAs

# Mesafe hesaplamaları
xDistance = abs(İKHAs[0]["x"] - İKHAs[1]["x"])
yDistance = abs(İKHAs[0]["y"] - İKHAs[1]["y"])
zDistance = abs(İKHAs[0]["z"] - İKHAs[1]["z"])

print(xDistance)

# Eğer çarpışma durumu riski olmazsa bunları uygulayacak.
if xDistance > 5:
    İKHAs[0]["x"] += 10
    İKHAs[1]["x"] += 10
    print("10 birim ileri")
if zDistance > 5:
    İKHAs[0]["y"] += 10
    İKHAs[1]["y"] += 10
    print("10 birim çapraz")

# Eğer çarpışma riski olursa bunları uygulayacak.
if xDistance < 5:
    İKHAs[0]["x"] += 5
    İKHAs[1]["x"] += -5  # Aradaki mesafeyi açmak için ters yöne yönlendiritoruz.
if yDistance < 5:
    İKHAs[0]["y"] += 5
    İKHAs[1]["y"] += -5
if zDistance < 5:
    İKHAs[0]["z"] += 5
    İKHAs[1]["z"] += -5


# Engele 20 birim mesafeden az kaldığı zaman kaçma hareketi yapıcak
if İKHAs[0]["e-x"] < 20 and İKHAs[0]["e-x"] != 0:
   İKHAs[0]["y"] += 20

if İKHAs[0]["e-y"] < 20 and İKHAs[0]["e-y"] != 0:
   İKHAs[0]["y"] += 20