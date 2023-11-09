import pygame as pg
import os
from menu.menu_components import Button, Text, Image

class ChooseLevelMenu():
    def __init__(self, screen : pg.Surface):
        self.screen = screen

        self.titre = Text("Select a level", (screen.get_width()/2, 40))

        repertoire_levels = "levels"

        level_files = [f for f in os.listdir(repertoire_levels) if os.path.isfile(os.path.join(repertoire_levels, f))]

        self.list_buttons = []
        self.all = pg.sprite.RenderUpdates()
        self.all.add(self.titre)

        current_width = 24 + 309/2
        current_height = 120 + 100/2
        for level in level_files:
            button = Button((current_width, current_height), level, lambda level=level: level)
            
            self.list_buttons.append(button)
            self.all.add(button)

            current_width = (current_width + 309 + 24)
            if current_width > screen.get_width():
                current_width = 24 + 309/2
                current_height += 100 + 24

        back_button = Button((screen.get_width() - 216/2 - 15, screen.get_height() - 70/2 - 15), "Back", lambda: "back", "small_green")

        self.list_buttons.append(back_button)
        self.all.add(back_button)

        self.background = pg.image.load("ressources/images/menu/fond.png")
    
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
        