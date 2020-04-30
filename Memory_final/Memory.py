import Engine #umetanje Engine, napravio ga je Leonardo
import pygame #umetanje pygamea
import time #umetanje time
import sys #umetanje sysa
import random #umetanje random

pygame.init()

white=(250,250,250) #odredivanje kordinata bjele boje u rgb-u
#odredivanje velicine ekrana
X = 1140 
Y = 540
dis=pygame.display.set_mode((X, Y ))
dis.fill(white) #umetanje boje pozadine
begtime=time.time() #vrijeme kada je program poceo

#umetanje slike za karticu za pokrivanje
red=pygame.image.load('red.jpg')
#umetanje slika
image0 = pygame.image.load('flower.jpg') 
image1 = pygame.image.load('sun.jpg')
image2 = pygame.image.load('flower2.jpg')
image3 = pygame.image.load('flower3.jpg')
#random mjesanje slika
l=[image0, image1, image2, image3, image0, image1, image2, image3]
li=[]
for i in range(8):
    li.append(random.choice(l))
    l.remove(li[i])

show=[True,True,True,True,True,True,True,True] #Pokazuju li se kartice
disabled=False #moze li se kartica okrenuti
open_card=False #je li kartica otvorena
forever_yeet=[True,True,True,True,True,True,True,True] #Hoce li kartica ostati otverena
card1=0 #broj kartice koju smo prvu okrenuli ce doci ovdje

def otvori(broj_kartice): #glavni program za otvanje kartice te provjeravanje jesu li kartice iste
    global open_card, disabled, begtime, card1 
    if open_card: 
        open_card=False #oznacavanje da je kartica otvorena
        if li[broj_kartice]==li[card1]: #provjeravanje jesu li kartice iste
            #micanje gornjih kartice
            forever_yeet[broj_kartice]=False  
            forever_yeet[card1]=False 
        else:
            disabled=True 
            begtime=time.time()
    else:
        open_card=True
        card1=broj_kartice
    show[broj_kartice]=False

#definiranje pozicije buttona i sto radi   
def fun():
    Engine.button(dis, 10, 10, red.get_width(), red.get_height(),otvori,0,'',disabled, red)
def fun1():
    Engine.button(dis, 10, 300,red.get_width(), red.get_height(),otvori,1,'',disabled, red)
def fun2():
    Engine.button(dis,300, 10,red.get_width(), red.get_height(),otvori,2,'',disabled, red)
def fun3():
    Engine.button(dis,600, 10,red.get_width(), red.get_height(),otvori,3,'',disabled, red)
def fun4():
    Engine.button(dis,300, 300,red.get_width(), red.get_height(),otvori,4,'',disabled, red)
def fun5():
    Engine.button(dis,600, 300,red.get_width(), red.get_height(),otvori,5,'',disabled, red)
def fun6():
    Engine.button(dis,900, 10,red.get_width(), red.get_height(),otvori,6,'',disabled, red)
def fun7():
    Engine.button(dis,900, 300,red.get_width(), red.get_height(),otvori,7,'',disabled, red)

def slike_display(): #postavljanje izmjesanih slika na pozicije
    dis.blit(li[0], (10, 10))
    dis.blit(li[1], (10, 300))
    dis.blit(li[2], (300, 10))
    dis.blit(li[3], (600, 10))
    dis.blit(li[4], (300, 300))
    dis.blit(li[5], (600, 300))
    dis.blit(li[6], (900, 10))
    dis.blit(li[7], (900, 300))

def kartice(): #umetanje kartica i provjeravanje jesu li upaljene 
    global show
    if show[0] and forever_yeet[0]:#svaka kartica provjerava je li vec otvorena ili bacena
        fun()
    if show[1] and forever_yeet[1]:   
        fun1()
    if show[2] and forever_yeet[2]:   
        fun2()
    if show[3] and forever_yeet[3]:   
        fun3()
    if show[4] and forever_yeet[4]: 
        fun4()
    if show[5] and forever_yeet[5]:   
        fun5()
    if show[6] and forever_yeet[6]:   
        fun6()
    if show[7] and forever_yeet[7]:  
        fun7()

def music(): #dodavanje glazbe jer zasto ne, da bude bar malo manje basic
    pygame.mixer.music.load('music_just_for_fun.mp3')#neznam zasto bas ova glazba, samo mi se svidjela
    pygame.mixer.music.play()#glazba se pusta samo jednom ali ima 15 minuta, ako nekom treba 15 min za ovo rijesi nezasluzuje nikakvu glazbu

#programa

music() #pustanje muzike da ljudi ne umru od dosade

while True:
    if begtime+1<time.time() and not open_card: #kartice ako nisu zauvjek yeetane se vrate nakon 1 sek
        disabled=False #opet mozes otvoriti karticu yay!!!
        show=[True,True,True,True,True,True,True,True]
    dis.fill(white) #bjela pozadina
    #postavljanje slika na pozicije
    slike_display()
    #postavljanje druge strane 'kartice' preko slika tako da ih igrac ne vidi
    kartice()
    pygame.display.update()
    for event in pygame.event.get() :  
        if event.type==pygame.QUIT: #izlazak iz prozora igre kada stisnemo crveni x
            pygame.display.quit()
            sys.exit()




 
