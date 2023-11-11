import pygame
import sys
from menu_start import afficher_menu_start

pygame.init()

# Définir la nouvelle taille souhaitée
nouvelle_largeur = 1200  # Remplacez par la largeur souhaitée
nouvelle_hauteur = 800  # Remplacez par la hauteur souhaitée

# Générer la première fenêtre avec les dimensions redimensionnées
screen = pygame.display.set_mode((nouvelle_largeur, nouvelle_hauteur))
pygame.display.set_caption("Jeu de test")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

       # Vérifier les événements clavier
        if event.type == pygame.KEYDOWN:
            # Vérifier si la touche CTRL est enfoncée
            if event.mod & pygame.KMOD_CTRL:
                # Vérifier si la touche W (minuscule ou majuscule) est enfoncée
                if event.key == pygame.K_w or event.key == pygame.K_W:
                    running = False
                    pygame.quit()
                    sys.exit()

    # Afficher le menu de démarrage
    afficher_menu_start(screen)

    pygame.display.flip()
