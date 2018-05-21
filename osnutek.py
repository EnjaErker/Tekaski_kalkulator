


#izracun:

def dodatek(starost,st_delovnih_let,letna_vlozena_vsota,ponudnik):
    starost = x
    st_delovnih_let = n
    letna_vlozena_vsota = r
    obrestna_mera(ponudnik) = i
    denar_ob_zakljucku_dela = round((r * ((1 + i)**n -1))/i , 2)
    rezultat = round(denar_ob_zakljucku_dela / st_let_v_penziji(x),2)
    return rezultat + '€'

#def st_let_v_penziji(x):

def obrestna_mera(ponudnik):
    slovar = {Pokojninska druzba A : 1.80,
              Skupna pokojninska družba : 1.03 ,
              Moja naložba : 1.15 ,
              Zavarovalnica Triglav : ,
              Adriatic Slovenica : ,
              Zavarovalnica Generali : ,
              Banka Koper : ,}
    return slovar.get(ponudnik)



#vmesnik:

import tkinter as tk

okno = tk.Tk()

tk.Label(text='PROGRAM ZA NAČRTOVANJE VARČEVANJA').grid(row=0)
tk.Button(text='VSTOPI', command=odpri_novo_okno).grid(row=1)


okno.mainloop()

def odpri_novo_okno():
    okno2 = tk.Tk()

    zgoraj = tk.Frame(okno2)
    spodaj = tk.Frame(okno2)
    zgoraj.grid(row=0)
    spodaj.grid(row=1)
    
    tk.Label(zgoraj, text='Uvodni tekst').pack()
    
    tk.Label(spodaj, text='Starost: ').grid(row=0, column=1)
    tk.Entry(spodaj).grid(row=0, column=2)

    tk.Label(spodaj, text='Število delovnih let: ').grid(row=1, column=1)
    tk.Entry(spodaj).grid(row=1, column=2)
    
    tk.Label(spodaj, text='Letna vložena vsota v €: ').grid(row=2, column=1)
    tk.Entry(spodaj).grid(row=2, column=2)

    tk.Label(spodaj, text='Ponudnik: ').grid(row=3, column=1)
    root = Tk()
    tkvar = StringVar(root)
    izbire = {'Pokojninska druzba A',
              'Skupna pokojninska družba',
              'Moja naložba',
              'Zavarovalnica Triglav',
              'Adriatic Slovenica',
              'Zavarovalnica Generali',
              'Banka Koper'}
    tkvar.set('Pokojninska družba A')
    popupMenu = OptionMenu(spodaj, tkvar, *izbire)
    popupMenu.grid(row=3, column=2)

    tk.Button(spodaj, text='IZRAČUNAJ', command=izracunaj).grid(row=4)
    
    okno2.mainloop()
    
def izracunaj():
    starost
    st_delovnih_let
    letna_vlozena_vsota
    ponudniki
    return 'Tekom vaše delovne dobe boste z zgornjim načinom privarčevali' +
            denar_ob_zakljucku_dela + '€, kar pomeni, da si boste lahko na leto v upokojitvi privoščili' +
            dodatek(starost,st_delovnih_let,letna_vlozena_vsota,ponudnik) + '€'
    

# uvodni tekst
#Pozdravljeni,
#naslednji program je namenjen vsem mladim, ki jih vsaj malo skrbi višina pokojnine.
#Če si tudi vi želite preveri, kam bi bilo najbolje vlagati svoj denar tekom delovne dobe,
#da bi bila vaša stara leta brezskrbna, samo izpolnite okenca spodaj.
#V prvi okvirček vtipkajte vašo trenutno starost v letih, v drugega pa število let delovne dobe,
#ki jih imate pred seboj. Tretji okvirček je namenjen vsoti denarja v €, ki ste jo na leto sposobni
#privarčevati. V četrtem okvirčku pa izberete svojega ponudnika. Nato le še pritisnite izračunaj.
