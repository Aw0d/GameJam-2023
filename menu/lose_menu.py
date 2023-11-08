import pygame as pg
from menu.menu_components import Button, Text

class LoseMenu():
    def __init__(self, screen : pg.Surface):
        self.screen = screen

        size = (500, 600)

        lose_text = Text("You lose!", (screen.get_width()/2, 150), 36, (0, 0, 0))

        retry_button = Button((screen.get_width()/2, 325), "Retry", lambda:"retry")
        menu_button = Button((screen.get_width()/2, 450), "Menu", lambda:"menu", "red")

        self.list_buttons = [retry_button, menu_button]

        self.all = pg.sprite.RenderUpdates()

        self.all.add(lose_text)
        self.all.add(retry_button)
        self.all.add(menu_button)

        self.background = pg.Surface(size)
        self.background.set_alpha(0)

    def update(self, events):
        # Détection des hovers et des clicks sur les boutons
        pos = pg.mouse.get_pos()
        for button in self.list_buttons:
            if button.rect.collidepoint(pos):
                button.hover(True)
                for event in events:
                    match event.type:
                        case pg.MOUSEBUTTONUP:
                            if event.button == pg.BUTTON_LEFT:
                                return button.func()                    
            else:
                button.hover(False)

    def show(self):
        self.screen.blit(self.background, (self.screen.get_width()/2 - 500/2, self.screen.get_height()/2 - 600/2))

        dirty = self.all.draw(self.screen)

        for button in self.list_buttons:
            button.draw_text(self.screen)
        pg.display.update(dirty)