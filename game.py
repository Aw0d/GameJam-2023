import pygame as pg
from components.player import Player
from components.ground import Ground
from components.spike import Spike
from components.table import Table
from components.chair import Chair
from components.book import Book



class Game:
    def __init__(self, screen: pg.Surface):
        # Conserve le lien vers l'objet surface ecran du jeux
        self.screen = screen

        # Crée une surface pour le fond du jeu de même taille que la fenêtre
        self.background = pg.Surface(self.screen.get_size())
        self.background.fill("white")

        # Dessine le font d'écran une première fois
        self.screen.blit(self.background,(0,0))

        # Création du sol
        self.ground = Ground(screen)

        # Définition de la vitesse du jeu
        self.speed = 0.4
        # Compteur du nombre de bonus
        self.bonus = 0
       
        # Objet sous groupe pour avoir la liste des sprites et automatiser la mise à jour par update()
        # Automatise aussi l'affichage : draw() par défaut affiche dans l'écran image à la position rect
        self.all = pg.sprite.RenderUpdates()
        
        self.all.add(Book(800, self.ground.rect.top - 70))
        self.all.add(Chair(800, self.ground.rect.top))
        self.all.add(Table(1000, self.ground.rect.top))
        self.all.add(Chair(1200, self.ground.rect.top))
        self.all.add(Table(1400, self.ground.rect.top))
        self.all.add(Table(1600, self.ground.rect.top))
        self.all.add(Table(1800, self.ground.rect.top))
        self.all.add(Spike(2000, self.ground.rect.top))
        self.all.add(Spike(2200, self.ground.rect.top))
        self.all.add(Spike(2400, self.ground.rect.top))
        self.all.add(Spike(2600, self.ground.rect.top))
        self.all.add(Spike(2800, self.ground.rect.top))
        self.all.add(self.ground)

        self.player = Player()
        self.all.add(self.player)

        # Vrai si le jeu est fini
        self.isEnded = False

    def isRunning(self):
        if self.isEnded:
            return False
        for event in pg.event.get():
            match event.type:
                case pg.QUIT:
                    # On ferme la fenêtre
                    return False
        return True
    
    def update(self, dt : int):
        """
        Met à jour l'état du jeux en fonction du temps dt écoulé 
        """
        # Collision entre le joueur et les autres objets
        hits = pg.sprite.spritecollide(self.player, self.all, False)

        # Récupération des touches appuyées
        pressed_keys = pg.key.get_pressed()

        if pressed_keys[pg.K_UP]:
            self.player.jump(hits)
        if pressed_keys[pg.K_DOWN]:
            self.player.slide()

        # Met à jours tous les sprites
        self.all.update(dt, self.speed)
        self.player._update(dt, hits)

        # Test de la collision entre le Player et les autres elements
        for sprite in hits:
            if type(sprite).__name__ == "Table" or type(sprite).__name__ == "Chair":
                # Si on n'est pas au dessus
                if self.player.rect.bottom - abs(self.player.vel_y * dt) - 1 > sprite.rect.top:
                    self.isEnded = True
            elif type(sprite).__name__ == "Spike":
                self.isEnded = True
            elif type(sprite).__name__ == "Book":
                self.all.remove(sprite)
                self.bonus += 1

        # Vide l'écran en replacant le background
        self.all.clear(self.screen, self.background)
        # Dessine tous les sprites dans la surface de l'écran
        dirty = self.all.draw(self.screen)
        # Remplace le background des zones modifiées par le mouvement des sprites
        pg.display.update(dirty)