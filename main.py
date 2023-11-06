import pygame as pg
from Game import Game

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

    # Création d'une instance du jeu
    game = Game(screen)

    # Boucle de jeu
    while game.isRunning():

        # Limite la vitesse à 6O images max par secondes
        # Calcule le temps réel entre deux images en millisecondes
        dt = clock.tick(60)

        # Met à jour le jeu sachant que dt millisecondes se sont écoulées
        game.update()

        # Affiche le nouvel état de l'écran
        pg.display.flip()

    # Fin utilisation de pygame
    pg.quit()


# Appel automatiquement la fonction main si pas utilisé comme module
if __name__ == "__main__":
    main()