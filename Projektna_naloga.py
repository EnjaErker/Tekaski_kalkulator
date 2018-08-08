# graficni vmesnik

from tkinter import *

okno = Tk()
okno.title("Moj program")
Label(okno, text='PROGRAM ZA IZRAČUN NAJBOLJŠIH ČASOV\n NA 5 KM, 10 KM, 21 KM IN 42 KM', bg='#a1dbcd', font='Helvetica 16 bold').pack()
okno.configure(background='#a1dbcd')


resultStr= StringVar()
resultStr.set("Vpišite svoje rezultate in kliknite IZRAČUNAJ.")
Uth = Label ( text="Uth-Sorensen-Overgaard-Pedersen približek (HR min in HR max):", bg='#a1dbcd')
Uth.pack()
vnos_Uth1 = Entry()
vnos_Uth1.pack()
vnos_Uth2 = Entry()
vnos_Uth2.pack() 

Cooper = Label ( text="Cooperjev test (dolžina(m) v 12 min):", bg='#a1dbcd')
Cooper.pack()
vnos_Cooper = Entry()
vnos_Cooper.pack()

Balke = Label (text="Balkejev test (dolžina(m) v 15 min):", bg='#a1dbcd')
Balke.pack()
vnos_Balke = Entry()
vnos_Balke.pack()

resultLabel = Label(textvariable=resultStr)
resultLabel.pack()

#funkcija za izracun

from scipy.optimize import fsolve
import pylab
import numpy as np
from numpy import array

def izracunaj():
    
    min_hr_Uth = int(vnos_Uth1.get()) 
    max_hr_Uth = int(vnos_Uth2.get()) 
    razdalja_Cooper = int(vnos_Cooper.get()) 
    razdalja_Balke = int(vnos_Balke.get()) 
    
    
    prvi = (15.3*max_hr_Uth)/(min_hr_Uth)
    drugi = (razdalja_Cooper -504.9)/(44.73)
    tretji = (((razdalja_Balke /15)-133)*0.172)+33.3
    vo2 = (prvi + drugi + tretji)/3
    izboljsan = vo2 + (1/10)*vo2
    povprecni_VO2 = round(izboljsan,2) 
    
    vsi_rezultati = []
    
    for s in [5000,10000,21000,42000]:
        
        funkcija = lambda t : (0.182258*(s/t)+0.000104*((s/t)**2)-4.60)/(0.2989558*(2.7**(-0.1932605*t))+0.1894393*(2.7**(-0.012778*t))+0.8) - povprecni_VO2
        zacetni_rezultat = fsolve(funkcija,1)
        koncni_rezultat = round(float(zacetni_rezultat),2)
        vsi_rezultati.append(koncni_rezultat)
    
    resultStr.set( "Rezultati so "+ str(vsi_rezultati[0]) +", "+ str(vsi_rezultati[1]) +", "+ str(vsi_rezultati[2]) +", "+ str(vsi_rezultati[3])+" v minutah.")
    
izračunaj = Button(text="IZRAČUNAJ", command=izracunaj, fg='#a1dbcd', bg ='#383a39 ')
izračunaj.pack()

okno.mainloop()
