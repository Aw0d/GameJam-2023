import pygame as pg
import pickle
pg.mixer.init()
from game import Game
from menu.main_menu import MainMenu
from menu.choose_level_menu import ChooseLevelMenu
from menu.credits_menu import CreditsMenu
from menu.settings_menu import Settings

# Fonction principale : pas de varaibles globales
def main():
    # Initialisation de pygame
    pg.init()
    # Initalisation du module de gestion des fonts
    pg.font.init()
    # Donne un nom à la fenêtre 
    pg.display.set_caption("UniversityRush")
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
    #   2: Menu settings
    #   3: Editeur de niveaux
    #   4: Crédits
    state = 0

    # Variable contenant le menu principal
    main_menu = MainMenu(screen)

    # Variable contenant le menu de choix de niveau
    choose_level_menu = ChooseLevelMenu(screen)
    
    #variable contenant le menu des settings
    settings = Settings(screen)
    
    #Variables des parametres des settings
    music_on = True
    sfx_on = True
    
    # Variable contenant le jeu
    game = None

    credits_menu = CreditsMenu(screen)

    # Boucle de jeu
    running = True
    while running:
        events = pg.event.get()
        for event in events:
            # Si on ferme la fenêtre, on arrête la boucle
            match event.type:
                case pg.QUIT:
                    # On ferme la fenêtre
                    running = False

        # Limite la vitesse à 6O images max par secondes
        # Calcule le temps réel entre deux images en millisecondes
        dt = clock.tick(60)

        if state == 0: # Menu principal
            game = None
            main_menu.show()

            # Met à jour le jeu sachant que dt millisecondes se sont écoulées
            menu_state = main_menu.update(events)
            if menu_state == "play":
                state = 5
            elif menu_state == "settings":
                state = 2
            elif menu_state == "quit":
                running = False
            elif menu_state == "credits":
                state = 4

            # Affiche le nouvel état de l'écran
            pg.display.flip()

        elif state == 1: # Jeu
            action = game.state()
            if action == "end":
                state = 0
            elif action == "retry":
                game = Game(screen)

            # Met à jour le jeu sachant que dt millisecondes se sont écoulées
            game.update(dt, events)

            # Affiche le nouvel état de l'écran
            pg.display.flip()

        elif state == 2: # Menu settings 
            settings.show()
             
            action = settings.update(events)
            if action == "back":
                state = 0
            elif action == "Music":
                music_on = not music_on
                if music_on:
                    pg.mixer_music.set_volume(100)
                else:
                    pg.mixer_music.set_volume(0)
            elif action == "SFX":
                sfx_on = not sfx_on
                if sfx_on:
                    for _ in range(pg.mixer.get_num_channels()):
                        pg.mixer.Channel(_).set_volume(100)
                else:
                    for _ in range(pg.mixer.get_num_channels()):
                        pg.mixer.Channel(_).set_volume(0)
                
            pg.display.flip()
        elif state == 3: # Editeur de niveaux
            pass
        elif state == 4: # Crédits
            credits_menu.show()

            action = credits_menu.update(events)
            if action == "back":
                state = 0

            pg.display.flip()
        elif state == 5: # Menu de choix de niveau
            choose_level_menu.show()

            action = choose_level_menu.update(events)
            if action == "back":
                state = 0
            elif action != None:
                with open("levels/" + action, 'rb') as fichier:
                    level = pickle.load(fichier)
                game = Game(screen, level)
                state = 1

            pg.display.flip()
    # Fin utilisation de pygame
    pg.quit()


# Appel automatiquement la fonction main si pas utilisé comme module
if __name__ == "__main__":
    main()