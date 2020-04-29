import Engine #umetanje Engine, napravio ga je Leonardo
import pygame #umetanje pygamea
import time #umetanje time
import sys
pygame.init()
white=(255, 255, 255) #odredivanje boje za pozadinu
#odredivanje velicine ekrana
X = 1140 
Y = 540
dis=pygame.display.set_mode((X, Y ))
dis.fill(white)
begtime=time.time()
#umetanje slika
red=pygame.image.load('red.jpg')
image0 = pygame.image.load('flower.jpg') 
image1 = pygame.image.load('sun.jpg')
image2 = pygame.image.load('flower2.jpg')
image3 = pygame.image.load('flower3.jpg')
#random mjesanje slika
l=[image0, image1, image2, image3, image0, image1, image2, image3]
import random
li=[]
for i in range(8):
    li.append(random.choice(l))
    l.remove(li[i])

show=[True,True,True,True,True,True,True,True]
disabled=False
open_card=False
forever_yeet=[True,True,True,True,True,True,True,True]
card1=0
def otvori(broj_kartice):
    global open_card, disabled, begtime, card1
    if open_card:
        open_card=False
        if li[broj_kartice]==li[card1]:
            forever_yeet[broj_kartice]=False
            forever_yeet[card1]=False
        else:
            disabled=True
            begtime=time.time()
    else:
        open_card=True
        card1=broj_kartice
    show[broj_kartice]=False
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
def kartice():
    global show
    if show[0] and forever_yeet[0]:
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

#programa
while True:
    if begtime+3<time.time() and not open_card:
        disabled=False
        show=[True,True,True,True,True,True,True,True]
    dis.fill(white) #bjela pozadina
    #postavljanje slika na pozicije
    slike_display()
    #postavljanje druge strane 'kartice' preko slika tako da ih igrac ne vidi
    kartice()
    pygame.display.update()
    for event in pygame.event.get() :
        if event.type==pygame.QUIT:
            pygame.display.quit()
            sys.exit()




 
