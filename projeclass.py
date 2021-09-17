
import random
from datetime import datetime



def sekil1(cins,yas):
    import requests
    api1 = open("api.txt","r",encoding="utf8")
    api1 = api1.readline()
    api_key = api1

    url = "https://api.generated.photos/api/v1/faces?api_key=" + api_key

    page = 1
    # Maximum: 100, Default: 10
    per_page = 1
    # male, female
    gender = cins
    # joy, neutral, surprise
    emotion = "neutral"
    # infant, child, young-adult, adult, elderly
    age = yas

    url = "{}&page={}&per_page={}&gender={}&emotion={}&age={}".format(url, page, per_page,gender, emotion, age)
    r = requests.get(url=url)
    data = r.json()

    
    for i, v in enumerate(data["faces"]):
        for j in v["urls"]:
            for key in j:
                
                if key == '128':
                    r = requests.get(url=j[key])
                
                
                    if r.status_code == 200:
                        # write the image
                        with open(str(i) + "-"+ key +".jpg", 'wb') as f:
                            f.write(r.content)
                        

def adsoyadkisi(ad,soyad):
    if ad == "Random" and soyad == "Random":
                
        try:
            adlar = open("adlar.txt","r",encoding="utf8")
            soyadlar = open("soyadlar.txt","r",encoding="utf8")
                
            ad_liste = adlar.readlines()
            soyadlar_liste = soyadlar.readlines()
                    
            ad_soyad = random.choice(ad_liste).replace("\n","") + " " + random.choice(soyadlar_liste).replace("\n","")
        except IOError:
            print("Xeta")
                
                
            
    elif ad != "Random" and soyad == "Random":
        try:
                    
            soyadlar = open("soyadlar.txt","r",encoding="utf8")
                
            soyadlar_liste = soyadlar.readlines()
                    
            ad_soyad = ad + " " + random.choice(soyadlar_liste).replace("\n","")
        except IOError:
            print("Xeta")
                
                
                    
    elif ad == "Random" and soyad != "Random":
        try:
            adlar = open("adlar.txt","r",encoding="utf8")
                    
            ad_liste = adlar.readlines()
                    
                    
            ad_soyad = random.choice(ad_liste).replace("\n","") + " " + soyad
        except IOError:
            print("Xeta")
                
                
                   
    else:
        ad_soyad = ad +" "+ soyad
            
    return ad_soyad
    
def adsoyadqadin(ad,soyad):
    if ad == "Random" and soyad == "Random":
                
        try:
            adlar = open("adlarqadin.txt","r",encoding="utf8")
            soyadlar = open("soyadlarqadin.txt","r",encoding="utf8")
                
            ad_liste = adlar.readlines()
            soyadlar_liste = soyadlar.readlines()
                    
            ad_soyad = random.choice(ad_liste).replace("\n","") + " " + random.choice(soyadlar_liste).replace("\n","")
        except IOError:
            print("Xeta")
                
                
                    
            
    elif ad != "Random" and soyad == "Random":
        try:
                    
            soyadlar = open("soyadlarqadin.txt","r",encoding="utf8")
                
            soyadlar_liste = soyadlar.readlines()
                    
            ad_soyad = ad + " " + random.choice(soyadlar_liste).replace("\n","")
        except IOError:
            print("Xeta")
                
                
                    
                    
    elif ad == "Random" and soyad != "Random":
        try:
            adlar = open("adlarqadin.txt","r",encoding="utf8")
                    
                
            ad_liste = adlar.readlines()
                    
            ad_soyad = random.choice(ad_liste).replace("\n","") + " " + soyad
        except IOError:
            print("Xeta")
                
                
            
    else:
        ad_soyad = ad +" "+ soyad
        
    return ad_soyad
    



class adsoyad():
    
    def __init__(self,ad,soyad):
        self.ad = ad
        self.soyad = soyad
        
    def ad_soyad(ad = "Random",soyad = "Random",cins = "Random"):
        
        
        
        if cins == "Kişi":
            ad_soyad = adsoyadkisi(ad,soyad)
        
       
       
       
        elif cins == "Qadın":
            ad_soyad = adsoyadqadin(ad,soyad)
           
            
        
        
        
        else: 
            liste = ["Kişi","Qadın"]
            
            cins = random.choice(liste)
            cins.replace("\n","")
            
            if cins == "Kişi":
                ad_soyad = adsoyadkisi(ad,soyad)
            
            else:
            
                ad_soyad = adsoyadqadin(ad,soyad)
                  
                
            
        return [ad_soyad,cins]
    
    
    
            
    
    
    def yas(yas = "Random"):
        
    

        il2 =datetime.now()
        il2 = il2.year
        if yas == "Random":
            
            age1 = random.randint(1970,il2)
            age1 = il2 - age1
        else:
            age1 = il2 - int(yas)
        
        return age1
        
        
    def sekilal(cins = "Random",yas = "Random"):
        gender = ["male","female"]
        
        if cins == "Random":
            cins = random.choice(gender)
            cins.replace("\n","")
            print(cins)
        else:
            if cins == "Kişi":
                cins ="male"
            elif cins == "Qadın":
                cins ="female"
            else:
                print("Xeta")

        il2 =datetime.now()
        il2 = il2.year
        
        aged = int(yas)
        if aged<=5:
            age = "infant"
        elif aged>5 and aged<=18:
            age = "child"
        elif aged>18 and aged<=44:
            age = "young-adult"
        elif aged>44 and aged<=65:
            age = "adult"
        elif aged>65:
            age =  "elderly"
            
        sekil1(cins,age) 

        


