# İHA boyutlarını 2*2*2 şeklinde alıyorum.
# Engel, İHA, İKA konumları ROS aracılığıyla sensörlerden alınacak.
# ROS'dan MongoDB veritabanına aktarılıp güncel veriler buraya çekilebilir.

import models.iha1Model as iha1Model
import models.iha2Model as iha2Model

İHA1 = iha1Model.İHA1
İHA2 = iha2Model.İHA2

# Mesafe hesaplamaları
xDistance = abs(İHA1["x"] - İHA2["x"])
yDistance = abs(İHA1["y"] - İHA2["y"])
zDistance = abs(İHA1["z"] - İHA2["z"])

print(xDistance)

# Eğer çarpışma durumu riski olmazsa bunları uygulayacak.
if xDistance > 5:
    İHA1["x"] += 10
    İHA2["x"] += 10
    print("10 birim ileri")
if zDistance > 5:
    İHA1["y"] += 10
    İHA2["y"] += 10
    print("10 birim çapraz")

# Eğer çarpışma riski olursa bunları uygulayacak.
if xDistance < 5:
    İHA1["x"] += 5
    İHA2["x"] += -5  # Aradaki mesafeyi açmak için ters yöne yönlendiritoruz.
if yDistance < 5:
    İHA1["y"] += 5
    İHA2["y"] += -5
if zDistance < 5:
    İHA1["z"] += 5
    İHA2["z"] += -5


# Engele 20 birim mesafeden az kaldığı zaman kaçma hareketi yapıcak
if İHA1["e-x"] < 20 and İHA1["e-x"] != 0:
   İHA1["y"] += 20

if İHA1["e-y"] < 20 and İHA1["e-y"] != 0:
   İHA1["y"] += 20
