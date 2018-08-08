# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 13:09:02 2018

@author: Enja
"""

# graficni vmesnik

from tkinter import *

top = Tk()
top.title("Moj program")
Label(top, text='PROGRAM ZA IZRAČUN NAJBOLJŠIH ČASOV\n NA 5 KM, 10 KM, 21 KM IN 42 KM',bg='white').pack()

resultStr= StringVar()
resultStr.set("Vpišite svoje rezultate in kliknite IZRAČUNAJ.")
number1Label = Label (text="Uth-Sorensen-Overgaard-Pedersen približek (HR min in HR max):")
number1Label.pack()
number1Box = Entry()
number1Box.pack()
number2Box = Entry()
number2Box.pack()

number3Label = Label (text="Cooperjev test (dolžina(m) v 12 min):")
number3Label.pack()
number3Box = Entry()
number3Box.pack()

number4Label = Label (text="Balkejev test (dolžina(m) v 15 min):")
number4Label.pack()
number4Box = Entry()
number4Box.pack()

resultLabel = Label(textvariable=resultStr)
resultLabel.pack()

#funkcija za izracun

from scipy.optimize import fsolve
import pylab
import numpy as np
from numpy import array

def izracunaj():
    
    va = int(number1Box.get()) 
    vb = int(number2Box.get()) 
    vc = int(number3Box.get()) 
    vd = int(number4Box.get()) 
    
    
    prvi = (15.3*vb)/(va)
    drugi = (vc-504.9)/(44.73)
    tretji = (((vd/15)-133)*0.172)+33.3
    vo2 = (prvi + drugi + tretji)/3
    izboljsan = vo2 + (1/10)*vo2
    povprecni_VO2 = round(izboljsan,2) 
    
    funkcija5 = lambda t : (0.182258*(5000/t)+0.000104*((5000/t)**2)-4.60)/(0.2989558*(2.7**(-0.1932605*t))+0.1894393*(2.7**(-0.012778*t))+0.8) - povprecni_VO2
    result5 = fsolve(funkcija5,1)
    a = result5
    b = float(a)
    petka = round(b,2)
    
    funkcija10 = lambda t : (0.182258*(10000/t)+0.000104*((10000/t)**2)-4.60)/(0.2989558*(2.7**(-0.1932605*t))+0.1894393*(2.7**(-0.012778*t))+0.8) - povprecni_VO2
    result10 = fsolve(funkcija10,1)
    c = result10
    d = float(c)
    desetka = round(d,2)

    funkcija21 = lambda t : (0.182258*(21000/t)+0.000104*((21000/t)**2)-4.60)/(0.2989558*(2.7**(-0.1932605*t))+0.1894393*(2.7**(-0.012778*t))+0.8) - povprecni_VO2
    result21 = fsolve(funkcija21,1)
    e = result21
    f = float(e)
    enaindva = round(f,2)

    funkcija42 = lambda t : (0.182258*(42000/t)+0.000104*((42000/t)**2)-4.60)/(0.2989558*(2.7**(-0.1932605*t))+0.1894393*(2.7**(-0.012778*t))+0.8) - povprecni_VO2
    result42 = fsolve(funkcija42,1)
    g = result42
    h = float(g)
    dvainstiri = round(h,2)

    resultStr.set( "Rezultati so "+str(petka)+", "+str(desetka)+", "+str(enaindva)+", "+str(dvainstiri)+" v minutah.")
    

    
but = Button(text="IZRAČUNAJ", command=izracunaj)
but.pack()

top.mainloop()
