# bulle_dialog.py
import pygame
import sys
import time

def afficher_bulle_dialogue(message, screen):
    blanc = (255, 255, 255)
    noir = (0, 0, 0)
    font = pygame.font.Font(None, 36)

    largeur_bulle = 400
    hauteur_bulle = 100
    x_bulle = (screen.get_width() - largeur_bulle) // 2
    y_bulle = screen.get_height() - hauteur_bulle - 20

    bulle_rect = pygame.Rect(x_bulle, y_bulle, largeur_bulle, hauteur_bulle)
    pygame.draw.rect(screen, blanc, bulle_rect)

    marge_texte = 20

    texte = ""
    for lettre in message:
        texte += lettre

        # Effacez l'ancien texte en remplissant la bulle avec la couleur d'arrière-plan
        pygame.draw.rect(screen, blanc, bulle_rect)

        texte_surface = font.render(texte, True, noir)
        texte_rect = texte_surface.get_rect(center=(x_bulle + largeur_bulle // 2, y_bulle + hauteur_bulle // 2))
        screen.blit(texte_surface, texte_rect)

        pygame.display.flip()
        pygame.time.wait(50)  # Attendre un court instant entre chaque lettre

    # Attendez jusqu'à ce que l'utilisateur clique pour passer au message suivant
    waiting_for_click = True
    while waiting_for_click:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                waiting_for_click = False
