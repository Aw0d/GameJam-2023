import pygame as pg
from components.player import Player
from components.background import Background
from components.ground import Ground
from components.spike import Spike
from components.table import Table
from components.chair import Chair
from components.bonus import Bonus
from components.malus import Malus
from components.end import EndGame

from menu.hud import HUD
from menu.pause_menu import PauseMenu
from menu.lose_menu import LoseMenu
from menu.win_menu import WinMenu

class Game:
    def __init__(self, screen: pg.Surface):
        # Conserve le lien vers l'objet surface ecran du jeux
        self.screen = screen

        # Définition de la vitesse du jeu
        self.speed = 0.4
        # Compteur du nombre de bonus
        self.bonus = 0

        # Création du HUD
        self.hud = HUD(self.screen.get_size())
        # Création du menu pause
        self.menu_pause = PauseMenu(screen)
        # Création du menu win
        self.menu_win = WinMenu(screen)
        # Création du menu lose
        self.menu_lose = LoseMenu(screen)

        # Crée une surface pour le fond du jeu de même taille que la fenêtre pour effacer le contenu affiché
        self.clear_background = pg.Surface(self.screen.get_size())
        self.clear_background.fill("white")
        # Dessine le font d'écran une première fois
        self.screen.blit(self.clear_background,(0,0))

        # Crée une surface pour le fond du jeu de même taille que la fenêtre
        self.background = Background(self.screen.get_size())
        # Création du sol
        self.ground = Ground((10000, 80), (0, self.screen.get_height()))

        # Objet sous groupe pour avoir la liste des sprites et automatiser la mise à jour par update()
        # Automatise aussi l'affichage : draw() par défaut affiche dans l'écran image à la position rect
        self.all = pg.sprite.RenderUpdates()

        self.all.add(self.background)
        self.all.add(self.ground)

        self.all.add(Chair(500, self.ground.rect.top))
        self.all.add(Chair(540, self.ground.rect.top))
        self.all.add(Chair(580, self.ground.rect.top))
        self.all.add(Chair(620, self.ground.rect.top))
        self.all.add(Chair(660, self.ground.rect.top))
        self.all.add(Chair(700, self.ground.rect.top))

        self.all.add(Spike(1000, self.ground.rect.top))

        self.all.add(Spike(2000, self.ground.rect.top))
        self.all.add(Spike(2030, self.ground.rect.top))

        self.all.add(Malus((2500, self.ground.rect.top - 10)))

        self.all.add(Spike(3000, self.ground.rect.top))
        self.all.add(Spike(3030, self.ground.rect.top))
        self.all.add(Ground((50, 50), (3070, self.ground.rect.top)))
        self.all.add(Spike(3130, self.ground.rect.top))
        self.all.add(Spike(3160, self.ground.rect.top))
        self.all.add(Ground((50, 100), (3200, self.ground.rect.top)))
        self.all.add(Spike(3260, self.ground.rect.top))
        self.all.add(Spike(3290, self.ground.rect.top))
        self.all.add(Ground((50, 150), (3320, self.ground.rect.top)))
        self.all.add(Bonus((3320, self.ground.rect.top - 160)))

        self.all.add(EndGame(8800, self.ground.rect.top))
        
        # On sépare les objets sans hitboxe des objets avec hitboxe
        self.objects_with_hitbox = pg.sprite.Group()
        for sprite in self.all.spritedict:
            if not isinstance(sprite, (Background, Player)):
                self.objects_with_hitbox.add(sprite) 

        self.player = Player()
        self.all.add(self.player)

        # Vrai si le jeu est fini
        self.isEnded = False
        self.isPaused = False
        self.isLosed = False
        self.isWin = False
        self.retry = False

    def state(self):
        if self.isEnded:
            return "end" # Menu Principal
        if self.retry:
            return "retry"
    
    def update(self, dt : int, events):
        """
        Met à jour l'état du jeux en fonction du temps dt écoulé 
        """
        for event in events:
            # Si on ferme la fenêtre, on arrête la boucle
            match event.type:
                case pg.KEYUP:
                    if event.key == pg.K_ESCAPE:
                        if not self.isLosed and not self.isWin:
                            self.isPaused = not self.isPaused


        if self.isWin or self.isLosed or self.isPaused or self.isEnded:
                self.player.channel.pause()

        if self.isPaused:
            self.menu_pause.show()
            action = self.menu_pause.update(events)
            if action == "continue":
                self.isPaused = False
            elif action == "retry":
                self.retry = True
            elif action == "menu":
                self.isEnded = True
        elif self.isLosed:
            self.menu_lose.show()
            action = self.menu_lose.update(events)
            if action == "retry":
                self.retry = True
            elif action == "menu":
                self.isEnded = True
        elif self.isWin:
            self.menu_win.show(self.bonus)
            action = self.menu_win.update(events)
            if action == "retry":
                self.retry = True
            elif action == "menu":
                self.isEnded = True
        else:
            # Collision entre le joueur et les autres objets
            hits = pg.sprite.spritecollide(self.player, self.objects_with_hitbox, False)

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
                if isinstance(sprite, (Table)):
                    # Si on n'est pas au dessus ou en dessous
                    if self.player.rect.bottom > sprite.rect.top + 30 and self.player.rect.top < sprite.rect.bottom - 50:
                        self.isLosed = True
                elif isinstance(sprite, Chair):
                    # Si on n'est pas au dessus
                    if self.player.rect.bottom > sprite.rect.top + 30 +28:
                        self.isLosed = True
                elif isinstance(sprite, Ground):
                    # Si on n'est pas au dessus
                    if self.player.rect.bottom > sprite.rect.top + 30:
                        self.isLosed = True
                elif isinstance(sprite, Spike):
                    if self.player.rect.clipline(sprite.rect.bottomleft, sprite.rect.midtop) or self.player.rect.clipline(sprite.rect.bottomright, sprite.rect.midtop):
                        self.isLosed = True
                elif isinstance(sprite, Bonus):
                    self.all.remove(sprite)
                    self.objects_with_hitbox.remove(sprite)
                    self.bonus += 1
                    self.hud.update_score(self.bonus)
                elif isinstance(sprite, Malus):
                    self.all.remove(sprite)
                    self.objects_with_hitbox.remove(sprite)
                    self.bonus -= 1
                    self.hud.update_score(self.bonus)
                elif isinstance(sprite, EndGame):
                    self.isWin = True

            if not self.isLosed and not self.isWin:
                # Vide l'écran en replacant le background
                self.all.clear(self.screen, self.clear_background)
                # Dessine tous les sprites dans la surface de l'écran
                self.background.draw(self.screen)
                dirty = self.all.draw(self.screen)
                self.player.particles.draw(self.screen)
                self.hud.draw(self.screen)
                # Remplace le background des zones modifiées par le mouvement des sprites
                pg.display.update(dirty)
            
