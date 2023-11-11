import pygame
import sys

def gestion_hover(texte, texte_rect, screen):
    rouge = (255, 0, 0)
    blanc = (255, 255, 255)

    hover = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if texte_rect.collidepoint(event.pos):
                print(f"{texte} cliqué!")
                # Ajouter ici le code que vous souhaitez exécuter lorsque le texte est cliqué.

    mouse_x, mouse_y = pygame.mouse.get_pos()
    hover = texte_rect.collidepoint((mouse_x, mouse_y))

    if hover:
        texte = pygame.font.Font(None, 72).render(texte, True, rouge)
    else:
        texte = pygame.font.Font(None, 72).render(texte, True, blanc)

    screen.blit(texte, texte_rect)

    return hover