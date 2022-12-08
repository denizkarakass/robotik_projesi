
from data import IHAs
from data import IKAs




# Aktif AGENT SAYISI BULMA START
aktifIHA = 1
aktifIKA = 1
for i in range(0, 9):
  if(IHAs[i]["status"] == "1"):
      aktifIHA += 1      
for i in range(0, 2):
  if(IKAs[i]["status"] == "1"):
      aktifIKA += 1
# Aktif AGENT SAYISI BULMA END

for i in range(0, aktifIHA + 1):
  IHAs[i]["y"]  += 20   
     
# Agent sayısına göre formasyon alma
if(aktifIHA == 9 and aktifIKA == 3):
    from formController.triangleStarForm import triangleStarForm

if(aktifIHA == 10 and aktifIKA == 1):
    from formController.futbolteamForm import futbolteamForm    

if(aktifIHA == 8 and aktifIKA == 1):
    from formController.denizForm import denizForm   

if(aktifIHA == 8 and aktifIKA == 2):
    from formController.emreForm import emreForm     

if(aktifIHA == 8 and aktifIKA == 3):
    from formController.squareForm import squareForm        

if(aktifIHA == 7 and aktifIKA == 1):
    from formController.furkanForm import furkanForm  

if(aktifIHA == 7 and aktifIKA == 2):
    from formController.chairtableForm import chairtableForm    

if(aktifIHA == 7 and aktifIKA == 3):
    from formController.newmoonFrom import newmoonFrom    
    
if(aktifIHA == 6 and aktifIKA == 3):
    from formController.hexagonForm import hexagonForm      
 
if(aktifIHA == 6 and aktifIKA == 2):
    from formController.houseForm import houseForm  

if(aktifIHA == 6 and aktifIKA == 1):
    from formController.manisarobotikForm import manisarobotikForm  

if(aktifIHA == 5 and aktifIKA == 2):
    from formController.treeForm import treeForm      

if(aktifIHA == 5 and aktifIKA == 1):
    from formController.triangleForm import triangleForm 

if(aktifIHA == 5 and aktifIKA == 3):
    from formController.vForm import vForm 
    
if(aktifIHA == 4 and aktifIKA == 1):
    from formController.pentagonForm import pentagonForm  
    
    
    
    
from rotationControllers.IHArotation import IHArotation    
from rotationControllers.IKArotation import IKArotation    

for i in range(0, 9):
 if(aktifIHA == 9 and aktifIKA == 3):
  


# Yangın görevi için panelden gelen ilgili konumlara yönlendirme yapıacak formasyon olmadan
# Rotasyon ile formasyon arasında ilişki kurulacak.  