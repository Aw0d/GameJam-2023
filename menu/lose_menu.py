import pygame as pg
from menu.menu_components import Button, Text

class LoseMenu():
    def __init__(self, screen : pg.Surface):
        self.screen = screen

        size = (500, 600)

        lose_text = Text("Perdu !", (screen.get_width()/2, 150), 56, (0, 0, 0))

        retry_button = Button((screen.get_width()/2, 325), 'img/menu_button.png', lambda:"retry")
        menu_button = Button((screen.get_width()/2, 450), 'img/menu_button.png', lambda:"menu")

        self.list_buttons = [retry_button, menu_button]

        self.all = pg.sprite.RenderUpdates()

        self.all.add(lose_text)
        self.all.add(retry_button)
        self.all.add(menu_button)

        self.background = pg.Surface(size)
        self.background.fill("white")

    def update(self):
        pos = pg.mouse.get_pos()
        for button in self.list_buttons:
            if button.rect.collidepoint(pos):
                if pg.mouse.get_pressed()[0] == 1 and button.state == False:
                    button.state = True
                    return button.func()
                    
            if pg.mouse.get_pressed()[0] == 0:
                button.state = False

    def show(self):
        self.screen.blit(self.background, (self.screen.get_width()/2 - 500/2, self.screen.get_height()/2 - 600/2))

        dirty = self.all.draw(self.screen)
        pg.display.update(dirty)