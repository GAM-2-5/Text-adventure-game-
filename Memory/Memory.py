import engine #umetanje engine, napravio ga je Leonardo
import pygame #umetanje pygamea
pygame.init() 
white=(255, 255, 255) #odredivanje boje za pozadinu
#odredivanje velicine ekrana
X = 1200 
Y = 600
dis = pygame.display.set_mode((X, Y ))
#umetanje slika
pygame.display.set_caption('Image')
red=pygame.image.load(r'C:\Users\User\Downloads\Programiranje\Memory\red.jpg')
image0 = pygame.image.load(r'C:\Users\User\Downloads\Programiranje\Memory\flower.jpg') 
image1 = pygame.image.load(r'C:\Users\User\Downloads\Programiranje\Memory\sun.jpg')
image2 = pygame.image.load(r'C:\Users\User\Downloads\Programiranje\Memory\flower2.jpg')
image3 = pygame.image.load(r'C:\Users\User\Downloads\Programiranje\Memory\flower3.jpg')
#random mjesanje slika
l=[image0, image1, image2, image3, image0, image1, image2, image3]
display_surface.fill(white)
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
#postavljanje slika na pozicije
display_surface.blit(n, (10, 10))
display_surface.blit(a, (10, 300))
display_surface.blit(b, (300, 10))
display_surface.blit(c, (600, 10))
display_surface.blit(d, (300, 300))
display_surface.blit(e, (600, 300))
display_surface.blit(f, (900, 10))
display_surface.blit(g, (900, 300))
#postavljanje drge strane 'kartice' preko slika tako da ih igrac ne vidi

engine.buttonDrawImage(dis, 10, 10, red)
engine.buttonDrawImage(dis, 10, 300, red)
engine.buttonDrawImage(dis, 300, 10, red)
engine.buttonDrawImage(dis, 600, 10, red)
engine.buttonDrawImage(dis, 300, 300, red)
engine.buttonDrawImage(dis, 600, 300, red)
engine.buttonDrawImage(dis, 900, 10, red)
engine.buttonDrawImage(dis, 900, 300, red)

#izlazak iz programa
for event in pygame.event.get() : 
    if event.type == pygame.QUIT :
        pygame.quit()
        quit()
    pygame.display.update()



 
