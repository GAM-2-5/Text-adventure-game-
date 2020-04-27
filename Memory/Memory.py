import Engine #umetanje Engine, napravio ga je Leonardo
import pygame #umetanje pygamea
pygame.init()
white=(255, 255, 255) #odredivanje boje za pozadinu
#odredivanje velicine ekrana
X = 1200 
Y = 600
dis=pygame.display.set_mode((X, Y ))
dis.fill(white)
#umetanje slika
red=pygame.image.load(r'C:\Users\User\Downloads\Programiranje\Memory\red.jpg')
image0 = pygame.image.load(r'C:\Users\User\Downloads\Programiranje\Memory\flower.jpg') 
image1 = pygame.image.load(r'C:\Users\User\Downloads\Programiranje\Memory\sun.jpg')
image2 = pygame.image.load(r'C:\Users\User\Downloads\Programiranje\Memory\flower2.jpg')
image3 = pygame.image.load(r'C:\Users\User\Downloads\Programiranje\Memory\flower3.jpg')
#random mjesanje slika
l=[image0, image1, image2, image3, image0, image1, image2, image3]
import random
n=random.choice(l)
l.remove(n)
a=random.choice(l)
l.remove(a)
b=random.choice(l)
l.remove(b)
c=random.choice(l)
l.remove(c)
d=random.choice(l)
l.remove(d)
e=random.choice(l)
l.remove(e)
f=random.choice(l)
l.remove(f)
g=random.choice(l)
l.remove(g)
def fun():
    print('nom')

#postavljanje drge strane 'kartice' preko slika tako da ih igrac ne vidi

#programa
while True:
    for event in pygame.event.get() :
            dis.fill(white) #bijela pozadina
            #postavljanje slika na pozicije
            dis.blit(n, (10, 10))
            dis.blit(a, (10, 300))
            dis.blit(b, (300, 10))
            dis.blit(c, (600, 10))
            dis.blit(d, (300, 300))
            dis.blit(e, (600, 300))
            dis.blit(f, (900, 10))
            dis.blit(g, (900, 300))
            #postavljanje drge strane 'kartice' preko slika tako da ih igrac ne vidi
            Engine.buttonDrawImage(dis, 10, 10, red)
            Engine.buttonDrawImage(dis, 10, 300, red)
            Engine.buttonDrawImage(dis, 300, 10, red)
            Engine.buttonDrawImage(dis, 600, 10, red)
            Engine.buttonDrawImage(dis, 300, 300, red)
            Engine.buttonDrawImage(dis, 600, 300, red)
            Engine.buttonDrawImage(dis, 900, 10, red)
            Engine.buttonDrawImage(dis, 900, 300, red)
            Engine.button(event,10,10,250,250,fun,button=1)
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()



 
