import pygame as pg
pg.mixer.init()
from components.background import Background
from components.ground import Ground
from components.malus import Malus
from components.bonus import Bonus
from components.spike import Spike
from components.table import Table
from components.chair import Chair
from components.end import EndGame
from menu.level_editor_pause_menu import LevelEditorPauseMenu
from menu.menu_contents import MenuContents
import pickle
from components.level import Level
from menu.menu_components import TextBox, Text
        

class LevelCreator:
    def __init__(self, screen: pg.Surface):
        pg.init()
        self.screen = screen

        self.buttons = []

        self.menu_pause = LevelEditorPauseMenu(self.screen)

        self.background_color = (255,255,255)

        self.menu_contents = MenuContents(self.screen.get_size())

        self.all = pg.sprite.RenderUpdates()

        # Crée une surface pour le fond du jeu de même taille que la fenêtre pour effacer le contenu affiché
        self.clear_background = pg.Surface(self.screen.get_size())
        self.clear_background.fill("white")

        # Dessine le font d'écran une première fois
        self.screen.blit(self.clear_background,(0,0))

        #création background et ground
        self.background = Background(self.screen.get_size())
        self.ground = Ground((0, self.screen.get_height()), (50000, 80))

        #vitesse de déplacement dans l'éditeur de niveau
        self.speed = 0.8

        #Ajout du background et du ground à la liste des sprites 
        self.all.add(self.ground)

        self.name = None
        self.textBox = TextBox((screen.get_width()/2, screen.get_height()/2), 600, 100)
        self.textBoxRU = pg.sprite.RenderUpdates()
        self.textBoxRU.add(self.textBox)
        self.textBoxRU.add(Text("Choose a level name:", (screen.get_width()/2, screen.get_height()/2 - 100), 36, (68,114,179)))

        self.isEnded = False
        self.isPaused = False

        self.click1 = None
        self.click2 = None

    def state(self):
        if self.isEnded:
            return "end"


    def update(self, dt : int, events):
        """
        Met à jour l'état du jeux en fonction du temps dt écoulé 
        """
        for event in events:
            # Si on ferme la fenêtre, on arrête la boucle
            match event.type:
                case pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        if not self.textBox.active:
                            if self.isPaused:
                                self.isPaused = not self.isPaused
                            else:
                                self.isPaused = not self.isPaused
                case pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        posMouse = pg.mouse.get_pos()
                        if (posMouse[0] > 390 or posMouse[1] > 675):
                            if posMouse[1] > 688:
                                posMouse = (posMouse[0], 688) 
                            if self.menu_contents.getSelection() == 1:
                                if not self.click1:
                                    self.click1 = posMouse
                                elif not self.click2:
                                    self.click2 = posMouse
                                    posx = min(self.click1[0], self.click2[0])
                                    posy = max(self.click1[1], self.click2[1])
                                    self.all.add(Ground((posx, posy), (abs(self.click2[0] - self.click1[0]), abs(self.click2[1] - self.click1[1]))))
                                    self.click1 = None
                                    self.click2 = None
                            elif self.menu_contents.getSelection() == 2:
                                self.all.add(Malus(posMouse))
                            elif self.menu_contents.getSelection() == 3:
                                self.all.add(Bonus(posMouse))
                            elif self.menu_contents.getSelection() == 4:
                                self.all.add(Spike(posMouse))
                            elif self.menu_contents.getSelection() == 5:
                                self.all.add(Table(posMouse))
                            elif self.menu_contents.getSelection() == 6:
                                self.all.add(Chair(posMouse))
                            elif self.menu_contents.getSelection() == 7:
                                self.all.add(EndGame(posMouse))
                            elif self.menu_contents.getSelection() == 8:
                                if (posMouse[1] < 688):
                                    for sprite in self.all:
                                        if sprite.rect.collidepoint(posMouse):
                                            self.all.remove(sprite)
                        
        if self.menu_contents.getSelection() == 9:
            self.textBox.active = True
            if self.name == False:
                self.textBox.active = False
                self.name = None
                self.menu_contents.setSelection(1)
            elif self.name == None:
                self.name = self.textBox.handle_event(events)
            else:
                level = Level(self.name)
                correction = -self.ground.rect.left
                for element in self.all.spritedict:
                    if isinstance(element, Ground):
                        level.all.append([element.__class__.__name__, [(element.rect.left + correction, element.rect.bottom), element.size]])
                    else:
                        level.all.append([element.__class__.__name__, (element.rect.centerx + correction ,element.rect.bottom)])
                
                with open(f"levels/{self.name}", "wb") as f1:
                    pickle.dump(level, f1)
                f1.close()
                self.isEnded = True

        if self.isPaused:
            self.menu_pause.show()
            action = self.menu_pause.update(events)
            if action == "continue":
                self.isPaused = False
            elif action == "retry":
                self.retry = True
            elif action == "menu":
                self.isEnded = True
        else:
            # Récupération des touches appuyées
            pressed_keys = pg.key.get_pressed()
            if pressed_keys[pg.K_RIGHT] and self.ground.rect.right > 1024:
                self.all.update(dt, self.speed)
            elif pressed_keys[pg.K_LEFT] and self.ground.rect.left < 0:
                self.all.update(dt, -self.speed)
            # Vide l'écran en replacant le background
            self.all.clear(self.screen, self.clear_background)
            # Dessine tous les sprites dans la surface de l'écran
            self.screen.blit(self.clear_background,(0,0))
            dirty = self.all.draw(self.screen)
            if self.textBox.active:
                self.textBoxRU.draw(self.screen)
                self.textBoxRU.update(self.screen)
            else:
                self.menu_contents.update(events)
                self.menu_contents.draw(self.screen)
            # Remplace le background des zones modifiées par le mouvement des sprites
            pg.display.update(dirty)
            
