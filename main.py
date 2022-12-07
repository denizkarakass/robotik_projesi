
from data import IHAs
from data import IKAs

# Aktif iha sayısı
aktifIHA = 1
aktifIKA = 1

for i in range(0, 9):
  if(IHAs[i]["status"] == "1"):
      aktifIHA += 1

# Aktif ika sayısı
aktifIKA = 1
for i in range(0, 2):
  if(IKAs[i]["status"] == "1"):
      aktifIKA += 1
      
print(aktifIKA)

# Agent sayısına göre formasyon alma
if(aktifIHA == 10 and aktifIKA == 3):
    from formController.triangleStarForm import triangleStarForm