from tkinter import *
import random
import time

prozor = Tk()

platno = Canvas(prozor,width=500,height=500,bg="lightblue")
platno.pack()


targetX = 100
targetY = 100

target_slika = PhotoImage(file="target_64x64.png")

target = platno.create_image(100,100,image=target_slika)


scope_slika = PhotoImage(file="scope.png")
scope = platno.create_image(250,250,image=scope_slika)


vreme_tekst = platno.create_text(125,30,text="Vreme: 1800",font="Times 20")

poeni_tekst = platno.create_text(375,30,text="Poeni: 0",font="Times 20")

vreme = 1800
poeni = 0



def umanji_vreme():
    global vreme
    vreme -= 1
    platno.itemconfig(vreme_tekst,text="Vreme: "+str(vreme))

def uvecaj_poene():
    global poeni
    poeni += 1
    platno.itemconfig(poeni_tekst,text="Poeni: "+str(poeni))

def glavna_petlja():
    while True:
        
        umanji_vreme()
        
        if vreme == 0:
            
            platno.delete(target)
            
            break
        time.sleep(0.01)
        prozor.update()


def pomeraj_nisan(e):
    platno.coords(scope,e.x,e.y)


def pucaj(e):
    global targetX, targetY, poeni
   
    t_levo = targetX - 32
    t_desno = targetX + 32
    
    t_gore = targetY - 32
    t_dole = targetY + 32
    
    if e.x > t_levo and e.x < t_desno and e.y > t_gore and e.y < t_dole:
        
        targetX = random.randrange(32,468)
        targetY = random.randrange(32,468)
        platno.coords(target,targetX,targetY)
        
        uvecaj_poene()

prozor.bind("<Motion>",pomeraj_nisan)

prozor.bind("<Button-1>",pucaj)


glavna_petlja()
