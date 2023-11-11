import pygame
pygame.init

#Génerer la premeire fenetre
pygame.display.set_caption('Jeu de test')
screen = pygame.display.set_mode((1080 , 700))


#background menu start
menu_start = pygame.image.load('asset\menu_start.jpg')
running = True


#Boucle du jeu
while running :

    #apppliquer l'arrrier plan
    screen.blit(menu_start, (0,0))

    #mettre a jour la fenetre
    pygame.display.flip()
    
    #condition de sortie (joueur ferme la fenetre)
    for event in pygame.event.get():
        #évènement = fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
