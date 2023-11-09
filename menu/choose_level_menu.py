import pygame as pg
import os
from menu.menu_components import Button, Text, Image

class ChooseLevelMenu():
    def __init__(self, screen : pg.Surface):
        self.screen = screen

        repertoire_levels = "levels"

        nb_levels = len([f for f in os.listdir(repertoire_levels) if os.path.isfile(os.path.join(repertoire_levels, f))])

        current_width = 24
        current_height = 
        for _ in range(nb_levels):
            button = Button()
            current_width = (current_width + 309 + 24)
            if current_width > screen.get_width():
                current_width = 24

        start_button = Button((512, 300), "Play", lambda: "play")
        menu_button = Button((512, 425), "Settings", lambda:"settings")
        inspect_button = Button((512, 550), "Level Editor", lambda:print("MODE INSPECTION"))
        exit_button = Button((512, 675), "Exit", lambda: "quit", "red")
        credits_button = Button((screen.get_width() - 216/2 - 15, screen.get_height() - 70/2 - 15), "Credits", lambda: "credits", "small_green")
        
        self.list_buttons = [start_button, menu_button, exit_button, inspect_button, credits_button]
        
        self.all = pg.sprite.RenderUpdates()

        self.all.add(start_button)
        self.all.add(menu_button)
        self.all.add(inspect_button)
        self.all.add(exit_button)
        self.all.add(credits_button)

        self.background = pg.image.load("images/menu/fond.png")
    
    def update(self, events):
        # Détection des hovers et des clicks sur les boutons
        pos = pg.mouse.get_pos()
        for button in self.list_buttons:
            if button.rect.collidepoint(pos):
                if not button.isHover:
                    button.hover(True)
                for event in events:
                    match event.type:
                        case pg.MOUSEBUTTONUP:
                            if event.button == pg.BUTTON_LEFT:
                                return button.clicked()                    
            else:
                if button.isHover:
                    button.hover(False)
    
    def show(self):
        self.screen.blit(self.background,(0,0))

        dirty = self.all.draw(self.screen)

        for button in self.list_buttons:
            button.draw_text(self.screen)
        pg.display.update(dirty)
        