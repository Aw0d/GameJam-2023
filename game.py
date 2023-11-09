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

from components.level import Level

from menu.hud import HUD
from menu.pause_menu import PauseMenu
from menu.lose_menu import LoseMenu
from menu.win_menu import WinMenu

class Game:
    def __init__(self, screen: pg.Surface, level: Level):
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
        self.ground = Ground((0, self.screen.get_height()), (50000, 80))

        # Objet sous groupe pour avoir la liste des sprites et automatiser la mise à jour par update()
        # Automatise aussi l'affichage : draw() par défaut affiche dans l'écran image à la position rect
        self.all = pg.sprite.RenderUpdates()

        self.all.add(self.background)
        self.all.add(self.ground)
        self.endGame = None

        self.load_level(level)
        
        # On sépare les objets sans hitboxe des objets avec hitboxe
        self.objects_with_hitbox = pg.sprite.Group()
        for sprite in self.all.spritedict:
            if not isinstance(sprite, (Background, Player)):
                self.objects_with_hitbox.add(sprite) 

        self.player = Player()
        self.all.add(self.player)
        
        # Musique de fond
        pg.mixer.music.load("ressources/music/8bit-Cruising-Down.mp3")
        pg.mixer.music.play(-1)

        # Vrai si le jeu est fini
        self.isEnded = False
        self.isPaused = False
        self.isLosed = False
        self.isWin = False
        self.retry = False

        self.current_end_pause_time = 0

    def load_level(self, level : Level):        
        for _ in level.all:
            object, info = _
            print(info)
            match object:
                case "Chair":
                    self.all.add(Chair(info))

                case "Table":
                    self.all.add(Table(info))

                case "Spike":
                    self.all.add(Spike(info))
                
                case "Ground":
                    self.all.add(Ground(info[0], info[1]))

                case "Bonus":
                    self.all.add(Bonus(info))
                
                case "Malus":
                    self.all.add(Malus(info))

                case "EndGame":
                    self.endGame = EndGame(info)
                    self.all.add(self.endGame)


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
                            pg.mixer.music.unpause()


        if self.isWin or self.isLosed or self.isPaused or self.isEnded:
                self.player.channel.pause()

        if self.isPaused:
            self.menu_pause.show()
            action = self.menu_pause.update(events)
            # Mettre la musique en pause
            pg.mixer.music.pause()

            if action == "continue":
                self.isPaused = False
                pg.mixer.music.unpause()
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
        elif self.endGame.isEnded:
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
                    if self.player.rect.bottom > sprite.rect.top + 30 and self.player.rect.top < sprite.rect.bottom - 45:
                        self.isLosed = True
                        pg.mixer.Sound("ressources/sounds/game-over.mp3").play()
                        pg.mixer.music.stop()
                elif isinstance(sprite, Ground):
                    # Si on n'est pas au dessus
                    if self.player.rect.bottom > sprite.rect.top + 30:
                        self.isLosed = True
                        pg.mixer.Sound("ressources/sounds/game-over.mp3").play()
                elif isinstance(sprite, Spike):
                    if self.player.rect.clipline(sprite.rect.bottomleft, sprite.rect.midtop) or self.player.rect.clipline(sprite.rect.bottomright, sprite.rect.midtop):
                        self.isLosed = True
                        pg.mixer.Sound("ressources/sounds/game-over.mp3").play()
                        pg.mixer.music.stop()
                elif isinstance(sprite, Bonus):
                    sprite.collect()
                    self.all.remove(sprite)
                    self.objects_with_hitbox.remove(sprite)
                    self.bonus += 1
                    self.hud.update_score(self.bonus)
                elif isinstance(sprite, Malus):
                    sprite.collect()
                    self.all.remove(sprite)
                    self.objects_with_hitbox.remove(sprite)
                    self.bonus -= 1
                    self.hud.update_score(self.bonus)
                elif isinstance(sprite, EndGame):
                    self.isWin = True

            if not self.isLosed and not self.endGame.isEnded:
                if self.isWin:
                    # On arrête la musique
                    pg.mixer.music.stop()
                    self.all.remove(self.player)
                    self.speed = 0

                    self.endGame.player_ended()

                    pause_time = 500
                    self.current_end_pause_time += dt 
                    if self.current_end_pause_time > pause_time:
                        self.endGame.isEnded = True

                # Vide l'écran en replacant le background
                self.all.clear(self.screen, self.clear_background)
                # Dessine tous les sprites dans la surface de l'écran
                self.background.draw(self.screen)
                dirty = self.all.draw(self.screen)
                self.player.particles.draw(self.screen)
                self.hud.draw(self.screen)
                # Remplace le background des zones modifiées par le mouvement des sprites
                pg.display.update(dirty)
