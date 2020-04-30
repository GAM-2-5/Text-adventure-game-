import pygame #unosimo pygame
__name__="Engine" #dajmo mu ime
#napravljeno by Leonardo, komentirano by Lucija :P

def button(display, x, y, width, height, funkcija,varijable, background_color="", disabled=False,  image="", title="", title_size=20, title_color=[255,255,255], text="", font_size=20, text_color=[0,0,0], border=0, border_color=[0,0,0], button=0): #sta sve mozemo dodati u nas button, mozemo dodati svasta ali meni je trebo manji dio, u svakom slucaju shoutout Leonardu, programic je super i skratio mi je posao
    if pygame.mouse.get_pressed()[button]: #sta se desi ako stisnemo gumb na misu
        mpos=pygame.mouse.get_pos()#pozicija koju je mis kliknuo
        if mpos[0]>=x and mpos[0]<=x+width and mpos[1]>=y and mpos[1]<=y+height and not disabled: #kada button djeluje
            funkcija(varijable)
    if background_color!="": #ako zelimo nacrtati button
        pygame.draw.rect(display, border_color, [x-border, y-border, width+2*border, height+2*border])
        pygame.draw.rect(display, background_color, [x, y, width, height])
    if image!="": #ako zelimo da je slika gumb
        display.blit(image, [x,y]) #odredivanje slike i njene kordinate
    #welp to je za svojstva za text ako ga se koristi
    font = pygame.font.Font('freesansbold.ttf', font_size) 
    text=font.render(text, True, text_color)
    textRect = text.get_rect()
    textRect.center = [x+width/2, y+height/2]
    display.blit(text, textRect)
    font = pygame.font.Font('freesansbold.ttf', title_size)
    text=font.render(title, True, title_color)
    textRect=text.get_rect()
    textRect.center=[x+width/2, y+height+textRect.height]
    display.blit(text, textRect)
