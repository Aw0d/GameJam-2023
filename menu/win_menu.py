import pygame as pg
from menu.menu_components import Button, Text

class WinMenu():
    def __init__(self, screen : pg.Surface):
        self.screen = screen

        size = (500, 600)

        win_text = Text("Bravo, vous êtes arrivé au bout !", (screen.get_width()/2, 150), 42, (0, 0, 0))
        self.score_text = Text("Votre score est de XXX.", (screen.get_width()/2, 220), 36, (0, 0, 0))

        retry_button = Button((screen.get_width()/2, 325), "Retry", lambda:"retry")
        menu_button = Button((screen.get_width()/2, 450), "Menu", lambda:"menu", "red")

        self.list_buttons = [retry_button, menu_button]

        self.all = pg.sprite.RenderUpdates()

        self.all.add(win_text)
        self.all.add(self.score_text)
        self.all.add(retry_button)
        self.all.add(menu_button)

        self.background = pg.Surface(size)
        self.background.fill("white")

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

    def show(self, score):
        self.score_text.update_text("Votre score est de " + str(score) + ".")

        self.screen.blit(self.background, (self.screen.get_width()/2 - 500/2, self.screen.get_height()/2 - 600/2))

        dirty = self.all.draw(self.screen)

        for button in self.list_buttons:
            button.draw_text(self.screen)
        pg.display.update(dirty)