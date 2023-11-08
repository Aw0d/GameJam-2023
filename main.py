import pygame as pg
from game import Game
from menu.main_menu import MainMenu

# Fonction principale : pas de varaibles globales
def main():
    # Initialisation de pygame
    pg.init()
    # Initalisation du module de gestion des fonts
    pg.font.init()
    # Donne un nom à la fenêtre 
    pg.display.set_caption("GAME")
    # Taille de l'écran imposée
    screenSize = (1024,768)
    # Crée la surface qui va servir de surface de jeu
    screen = pg.display.set_mode(screenSize)
    # Creé un objet horloge pour gerer le temps entre deux images
    clock = pg.time.Clock()
    # Nombre de millisecondes entre deux images 
    dt = 0
    # Etat du jeu:
    #   0: Menu principal
    #   1: Jeu
    #   2: Pause en jeu
    #   3: Menu settings
    #   4: Editeur de niveaux
    #   ...
    state = 0

    # Variable contenant le menu principal
    main_menu = None
    # Variable contenant le jeu
    game = None

    # Boucle de jeu
    previous_esc_state = False  # Variable pour garder en mémoire l'état précédent de la touche "échap"
    running = True
    while running:
        for event in pg.event.get():
            # Si on ferme la fenêtre, on arrête la boucle
            match event.type:
                case pg.QUIT:
                    # On ferme la fenêtre
                    running = False
                case pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        # Vérifie si la touche "échap" est actuellement enfoncée
                        if not previous_esc_state:
                            if state == 1:
                                state = 2
                            elif state == 2:
                                state = 1
                        previous_esc_state = True  # Mémoriser l'état actuel de la touche "échap"
                case pg.KEYUP:
                    if event.key == pg.K_ESCAPE:
                        previous_esc_state = False  # La touche "échap" est maintenant relâchée


        if state == 0: # Menu principal
            game = None
            if main_menu == None:
                main_menu = MainMenu(screen)

            # Limite la vitesse à 6O images max par secondes
            # Calcule le temps réel entre deux images en millisecondes
            dt = clock.tick(60)

            # Met à jour le jeu sachant que dt millisecondes se sont écoulées
            menu_state = main_menu.update()
            if menu_state:
                state = menu_state

            # Affiche le nouvel état de l'écran
            pg.display.flip()

        elif state == 1: # Jeu
            # Si le jeu n'est pas créé, on en crée un
            if game == None:
                game = Game(screen)

            state = game.isRunning()

            # Limite la vitesse à 6O images max par secondes
            # Calcule le temps réel entre deux images en millisecondes
            dt = clock.tick(60)

            # Met à jour le jeu sachant que dt millisecondes se sont écoulées
            game.update(dt)

            # Affiche le nouvel état de l'écran
            pg.display.flip()

        elif state == 2: # Pause en jeu
            dt = clock.tick(60)
        elif state == 3: # Menu settings
            pass
        elif state == 4: # Editeur de niveaux
            pass

    # Fin utilisation de pygame
    pg.quit()


# Appel automatiquement la fonction main si pas utilisé comme module
if __name__ == "__main__":
    main()