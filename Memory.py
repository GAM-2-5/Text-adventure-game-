
import pygame 
pygame.init() 
white = (255, 255, 255) 
X = 1000
Y = 600
display_surface = pygame.display.set_mode((X, Y )) 
pygame.display.set_caption('Image') 
image = pygame.image.load(r'C:\Users\User\Downloads\Programiranje\Memory\flower.jpg') 
image1 = pygame.image.load(r'C:\Users\User\Downloads\Programiranje\Memory\flower.jpg')
while True : 
    display_surface.fill(white) 
    display_surface.blit(image, (0, 0))
    display_surface.blit(image1, (300, 0))
    for event in pygame.event.get() : 
        if event.type == pygame.QUIT : 
            pygame.quit() 
            quit()
        pygame.display.update()
 
