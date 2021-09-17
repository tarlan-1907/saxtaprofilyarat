from tkinter import *
import tkinter
from tkinter.ttk import Combobox
from projeclass import *
from PIL import Image, ImageTk
from tkhtmlview import HTMLLabel



pencere = Tk()
pencere.geometry("800x250")
pencere.minsize(800,250)
pencere.maxsize(800,250)

yazimelumat = Label(pencere)
yazimelumat.configure(text="Qeyd: Random məlumatlar yaratmaq üçün secimlərə Random yazın.")
yazimelumat2 = Label(pencere)
yazimelumat2.configure(text="    Digər hallarda Ad, Soyad, Doğum tarixi, Cins, yazın və ya seçin")
yazimelumat.place(x=10,y=200)
yazimelumat2.place(x=10,y=220)

#Creat cins combox

yazicins = Label(pencere)
yazicins.config(text = "Cins:",font=("Vertena",12))
yazicins.place(x=0,y=87)
deyer = ["Kişi","Qadın","Random"]
cins1 = Combobox(
    master=pencere,
    values=deyer,
)
cins1.place(x=55,y=89)
cins1.insert(0,"Random")



#Creat ad entry
yaziad = Label(pencere)
yaziad.config(text="Ad:",font=("Vertena",12))
yaziad.place(x=0,y=15)
ad1 = Entry(pencere)
ad1.place(x=55,y=17)
ad1.insert(0,"Random")


#Creat soyad entry
yazisoyad = Label(pencere)
yazisoyad.config(text = "Soyad:",font=("Vertena",12))
yazisoyad.place(x=0,y=38)
soyad1 = Entry(pencere)
soyad1.place(x=55,y=41)
soyad1.insert(0,"Random")

    

#Creat yas label
yaziyas1 = Label(pencere)
yaziyas1.config(text = "Doğum Tarixi:",font=("Vertena",10))
yaziyas1.place(x=0,y=63)

il = datetime.now()
il = il.year


deyer1 = [i for i in range(1970,il+1)]
yas1 = Combobox(
    master=pencere,
    values=deyer1,
)
yas1.place(x=90,y=65)
yas1.insert(0,"Random")

    
    
    
  
def yarat():
    
    #AD Soyad
    yaziad1 = Label(pencere)
    return1 = adsoyad.ad_soyad(cins=cins1.get(),ad=ad1.get(),soyad=soyad1.get())
    adsoyad1 = return1[0]
    cins = return1[1]
    text = "Ad və Soyad: {}".format(adsoyad1)
    
    if len(text)<35:
        text = text + (35-len(text)) * " "
    else:
        pass
    yaziad1.config(text = text,bg="blue")
    yaziad1.place(x=400,y=15)
    
    
    #Cins
    yazicins1 = Label(pencere)
    if cins1.get() == "Random":
        cins = cins
    else:
        cins = cins1.get()
    if cins == "Kişi":
        yazicins1.config(text = "Cins: {}".format(cins) + "     ",bg="blue")
    else:
        yazicins1.config(text = "Cins: {}".format(cins),bg="blue")
    yazicins1.place(x=400,y=50)
    
    
    
    #Yaş
    yas3 = adsoyad.yas(yas=yas1.get())
    yas3 = str(yas3)
    yaziyas2 = Label(pencere)
    if int(yas3)<10:
        yaziyas2.config(text = "Yaş: {}".format(yas3) + "  ",bg= "blue")
    else:
        yaziyas2.config(text = "Yaş: {}".format(yas3),bg= "blue")
 
    yaziyas2.place(x = 400, y=85)
    
    
    #Şəkil
    adsoyad.sekilal(cins=cins,yas=yas3)
    image1 = Image.open("0-128.jpg")
    
    test = ImageTk.PhotoImage(image1)
    sekil = tkinter.Label(image = test)
    sekil.image = test
    sekil.place(x=650,y=15)
    
    
    
    #Email
    yaziemail1 = Label(pencere)
    yaziemail1.config(text="E-poçt: ",bg="blue")
    yaziemail1.place(x=400,y=150)
    yaziemail = HTMLLabel(pencere,html='<a href = "https://www.1secmail.com" color="black" style ="color:DodgerBlue; font-size: 10px;" > E-poçt Aktiv Et </a>')
    yaziemail.place(x=450,y=145)
    
    
    
    
    
    
    
def buton():
    buton1 = Button(pencere)
    buton1.config(text="Yarat", bg="yellow", fg="black", command=yarat,)
    buton1.place(x=10,y=120)



buton()


mainloop()