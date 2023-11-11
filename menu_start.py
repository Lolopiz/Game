import pygame
import sys

def afficher_menu_start(screen):
    blanc = (255, 255, 255)
    rouge = (255, 0, 0)

    font_size = 65
    font = pygame.font.Font(None, font_size)
    font_hover = pygame.font.Font(None, font_size)

    texte_start = font.render("Start", True, blanc)
    texte_parametre = font.render("Parametre", True, blanc)
    texte_credit = font.render("Credit", True, blanc)

    texte_start_rect = texte_start.get_rect()
    texte_parametre_rect = texte_parametre.get_rect()
    texte_credit_rect = texte_credit.get_rect()

    texte_start_rect.midtop = (screen.get_width() // 2, screen.get_height() // 2)
    texte_parametre_rect.midtop = (
        screen.get_width() // 2,
        texte_start_rect.bottom + 20,
    )
    texte_credit_rect.midtop = (
        screen.get_width() // 2,
        texte_parametre_rect.bottom + 20,
    )

    game_name_image = pygame.image.load('asset/game_name.png')
    game_name_rect = game_name_image.get_rect()
    game_name_rect.midtop = (screen.get_width() // 2, 10)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Vérifier si la souris survole les textes
            hover_start = texte_start_rect.collidepoint(pygame.mouse.get_pos())
            hover_parametre = texte_parametre_rect.collidepoint(pygame.mouse.get_pos())
            hover_credit = texte_credit_rect.collidepoint(pygame.mouse.get_pos())

            # Changer le style de police pour le survol
            texte_start = (
                font_hover.render("Start", True, rouge)
                if hover_start
                else font.render("Start", True, blanc)
            )
            texte_parametre = (
                font_hover.render("Parametre", True, rouge)
                if hover_parametre
                else font.render("Parametre", True, blanc)
            )
            texte_credit = (
                font_hover.render("Credit", True, rouge)
                if hover_credit
                else font.render("Credit", True, blanc)
            )

            # Si le clic gauche de la souris est enfoncé
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Afficher un message différent pour chaque texte
                if hover_start:
                    print("Start cliqué!")
                elif hover_parametre:
                    print("Parametre cliqué!")
                elif hover_credit:
                    print("Credit cliqué!")

        # Appliquer l'arrière-plan
        screen.fill((0, 0, 0))

        # Afficher l'image du nom du jeu
        screen.blit(game_name_image, game_name_rect)

        # Afficher les textes
        screen.blit(texte_start, texte_start_rect)
        screen.blit(texte_parametre, texte_parametre_rect)
        screen.blit(texte_credit, texte_credit_rect)

        # Afficher une flèche à côté du texte survolé
        if hover_start:
            pygame.draw.polygon(
                screen,
                blanc,
                [
                    (texte_start_rect.right + 10, texte_start_rect.centery),
                    (texte_start_rect.right + 30, texte_start_rect.centery - 10),
                    (texte_start_rect.right + 30, texte_start_rect.centery + 10),
                ],
            )
        elif hover_parametre:
            pygame.draw.polygon(
                screen,
                blanc,
                [
                    (texte_parametre_rect.right + 10, texte_parametre_rect.centery),
                    (
                        texte_parametre_rect.right + 30,
                        texte_parametre_rect.centery - 10,
                    ),
                    (
                        texte_parametre_rect.right + 30,
                        texte_parametre_rect.centery + 10,
                    ),
                ],
            )
        elif hover_credit:
            pygame.draw.polygon(
                screen,
                blanc,
                [
                    (texte_credit_rect.right + 10, texte_credit_rect.centery),
                    (texte_credit_rect.right + 30, texte_credit_rect.centery - 10),
                    (texte_credit_rect.right + 30, texte_credit_rect.centery + 10),
                ],
            )

        # Mettre à jour la fenêtre
        pygame.display.flip()

# Exemple d'utilisation
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Menu Start')
afficher_menu_start(screen)
