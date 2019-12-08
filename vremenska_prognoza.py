import json
import requests
from tkinter import *


#Preuzimanje podataka za odredeni grad
def provjera_temp():
    grad = unos1.get()
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=06bbe28e4fe853b15b6b855c676744f1&units=metric".format(grad)
    request = requests.get(url)
    data = request.json()

    temperatura = int(data['main']['temp'])
    brzina_vjetra = data['wind']['speed']
    vlaga = data['main']['humidity']
    maks_temp = int(data['main']['temp_max'])
    min_temp = int(data['main']['temp_min'])
    celzijus = "°C"
    postotak = "%"
    brzina = "km/h"

    if(["cod"] !='404'):
        temperaturaR.configure(text=temperatura)
        vlagaR.configure(text=vlaga)
        brzinavjetraR.configure(text=brzina_vjetra)
        maksTempR.configure(text=maks_temp)
        minTempR.configure(text=min_temp)
        celzijus1.configure(text=celzijus)
        vlagaPosto.configure(text=postotak)
        celzijus2.configure(text=celzijus)
        brzina1.configure(text=brzina)
        celzijus3.configure(text=celzijus)

    else:
        temperaturaR.configure(text="Pogreska")
        vlagaR.configure(text="Pogreska")
        brzinavjetraR.configure(text="Pogreska")
        maksTempR.configure(text="Pogreska")
        minTempR.configure(text="Pogreska")


#Dizajn 
root = Tk()
root.title("Vremenska Prognoza")
root.geometry("350x450")
root.resizable(False, False)
root.iconbitmap("ikona.ico")

#Naslovi
naziv = Label(root, text="Vremenska Prognoza",font=("Arial",20,))
naziv.pack()
naziv.place(x=47,y=40)

naziv2 = Label(root,text="Napravio Renato Kaurić, 4.E", font=("Arial",12))
naziv2.pack()
naziv2.place(x=77,y=75)

#Input prozor
ime_grada = StringVar()
unos1 = Entry(root,textvariable=ime_grada)
unos1.place(x=75,y=410)

#Label kod unosa

naziv3 = Label(root,text="Unesi ime grada za provjeru.",font=("Arial",10))
naziv3.pack()
naziv3.place(x=80,y=380)

#Gumb za provjeru

gumb = Button(root,text="Provjeri",command=provjera_temp)
gumb.pack()
gumb.place(x=212,y=407)

#Labeli za pojedinu stavku

temperaturaF = Label(root,text="Temperatura :", font =("Arial",12))
temperaturaF.pack()
temperaturaF.place(x=40,y=130)

vlagaF = Label(root, text="Vlaga u zraku :", font=("Arial",12))
vlagaF.pack()
vlagaF.place(x=40,y=154)

brzinavjetraF = Label(root, text="Brzina vjetra :", font=("Arial",12))
brzinavjetraF.pack()
brzinavjetraF.place(x=40,y=178)

maksTempF = Label(root, text="Maksimalna temperatura :",font=("Arial",12))
maksTempF.pack()
maksTempF.place(x=40,y=178+24)

minTempF = Label(root, text="Minimalna temperatura :",font=("Arial",12))
minTempF.pack()
minTempF.place(x=40,y=178+24+24)

#Labeli za ispisane podatke

temperaturaR = Label(root, text="", font=("Arial",12))
temperaturaR.pack()
temperaturaR.place(x=160,y=130)

vlagaR = Label(root, text="", font=("Arial",12))
vlagaR.pack()
vlagaR.place(x=160,y=154)

brzinavjetraR = Label(root, text="", font=("Arial",12))
brzinavjetraR.pack()
brzinavjetraR.place(x=160,y=178)

maksTempR = Label(root, text="",font=("Arial",12))
maksTempR.pack()
maksTempR.place(x=230,y=178+24)

minTempR = Label(root, text="",font=("Arial",12))
minTempR.pack()
minTempR.place(x=215,y=178+24+24)

celzijus1 = Label(root, text="", font=("Arial,12"))
celzijus1.pack()
celzijus1.place(x=180,y=130)

vlagaPosto = Label(root,text="", font=("Arial,12"))
vlagaPosto.pack()
vlagaPosto.place(x=180,y=154)

celzijus2 = Label(root, text="", font=("Arial,12"))
celzijus2.pack()
celzijus2.place(x=250,y=178+24)

brzina1 = Label(root, text="", font=("Arial,12"))
brzina1.pack()
brzina1.place(x=185,y=178)

celzijus3 = Label(root, text="", font=("Arial,12"))
celzijus3.pack()
celzijus3.place(x=236,y=178+24+24)

root.mainloop()
