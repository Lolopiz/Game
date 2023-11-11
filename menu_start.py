import pygame
import sys
from bulle_dialog import afficher_bulle_dialogue

def afficher_menu_start(screen):
    blanc = (255, 255, 255)
    rouge = (255, 0, 0)

    font_size = 65
    font = pygame.font.Font(None, font_size)
    font_hover = pygame.font.Font(None, font_size)

    texte_start = font.render("Start", True, blanc)
    texte_start_rect = texte_start.get_rect(midtop=(screen.get_width() // 2, 300))

    texte_parametre = font.render("Parametre", True, blanc)
    texte_parametre_rect = texte_parametre.get_rect(midtop=(screen.get_width() // 2, 400))

    texte_credit = font.render("Credit", True, blanc)
    texte_credit_rect = texte_credit.get_rect(midtop=(screen.get_width() // 2, 500))

    game_name_image = pygame.image.load('asset/game_name.png')
    game_name_rect = game_name_image.get_rect(midtop=(screen.get_width() // 2, 10))
    
    hover_start = False
    hover_parametre = False
    hover_credit = False

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
                    afficher_page_bulles(screen)
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
        

          
# Fonction pour afficher une page avec des bulles de dialogue
def afficher_page_bulles(screen):
    messages = ["Hello!", "How are you?", "This is another message.", "Goodbye!"]
    current_message_index = 0

    # Définissez le rectangle du bouton ici
    button_rect = pygame.Rect(screen.get_width() - 100, screen.get_height() - 50, 80, 40)
    rayon_corners = 10
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if button_rect.collidepoint(event.pos):
                    if current_message_index < len(messages):
                        afficher_bulle_dialogue(messages[current_message_index], screen)
                        current_message_index += 1

        # Remplacez le contenu de la boucle par le remplissage de l'écran avec une couleur noire
        screen.fill((0, 0, 0))

        pygame.draw.rect(screen, (255, 0, 0), button_rect, 2)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Menu Start')
    afficher_menu_start(screen)
