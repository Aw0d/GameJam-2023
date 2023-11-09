import pygame as pg
from menu.menu_components import Button, Text

class WinMenu():
    def __init__(self, screen : pg.Surface):
        self.screen = screen

        size = (500, 600)

        win_text = Text("Well played !", (screen.get_width()/2, 150), 36, (0, 0, 0))
        self.score_text = Text("Your score is XXX.", (screen.get_width()/2, 220), 24, (0, 0, 0))

        retry_button = Button((screen.get_width()/2, 325), "Retry", lambda:"retry")
        menu_button = Button((screen.get_width()/2, 450), "Menu", lambda:"menu", "red")

        self.list_buttons = [retry_button, menu_button]

        self.all = pg.sprite.RenderUpdates()

        self.all.add(win_text)
        self.all.add(self.score_text)
        self.all.add(retry_button)
        self.all.add(menu_button)

        self.background = pg.Surface(size)
        self.background.set_alpha(0)

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

    def show(self, score):
        self.score_text.update_text("Your score is " + str(score) + ".")

        self.screen.blit(self.background, (self.screen.get_width()/2 - 500/2, self.screen.get_height()/2 - 600/2))

        dirty = self.all.draw(self.screen)

        for button in self.list_buttons:
            button.draw_text(self.screen)
        pg.display.update(dirty)