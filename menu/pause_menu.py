import pygame as pg
from menu.menu_components import Button, Text

class PauseMenu():
    def __init__(self, screen : pg.Surface):
        self.screen = screen

        size = (500, 600)

        pause_text = Text("Game paused!", (screen.get_width()/2, 150), 36, (0, 0, 0))

        continue_button = Button((screen.get_width()/2, 300), "Continue", lambda:"continue")
        retry_button = Button((screen.get_width()/2, 425), "Retry", lambda:"retry")
        menu_button = Button((screen.get_width()/2, 550), "Menu", lambda:"menu", "red")

        self.list_buttons = [continue_button, retry_button, menu_button]

        self.all = pg.sprite.RenderUpdates()

        self.all.add(pause_text)
        self.all.add(continue_button)
        self.all.add(retry_button)
        self.all.add(menu_button)

        self.background = pg.Surface(size)
        self.background.set_alpha(0)

    def update(self):
        pos = pg.mouse.get_pos()
        for button in self.list_buttons:
            if button.rect.collidepoint(pos):
                button.hover(True)
                if pg.mouse.get_pressed()[0] == 1 and button.state == False:
                    button.state = True
                    return button.func()
            else:
                button.hover(False)

    def show(self):
        self.screen.blit(self.background, (self.screen.get_width()/2 - 500/2, self.screen.get_height()/2 - 600/2))

        dirty = self.all.draw(self.screen)

        for button in self.list_buttons:
            button.draw_text(self.screen)
        pg.display.update(dirty)