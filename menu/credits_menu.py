import pygame as pg
from menu.menu_components import Button, Text, Image

class CreditsMenu():
    def __init__(self, screen : pg.Surface):
        self.screen = screen

        logo = Image((500, 174), (512, 100), "images/logo.png")

        credits_text = Text("credits", (screen.get_width()/2, 350), 24, (0, 0, 0), None)

        back_button = Button((screen.get_width() - 216/2 - 15, screen.get_height() - 70/2 - 15), "Back", lambda: "back", "small_green")

        self.list_buttons = [back_button]

        self.all = pg.sprite.RenderUpdates()

        self.all.add(logo)
        self.all.add(credits_text)
        self.all.add(back_button)

        self.background = pg.image.load("images/menu/fond.png")

    def update(self):
        # Détection des hovers et des clicks sur les boutons
        pos = pg.mouse.get_pos()
        for button in self.list_buttons:
            if button.rect.collidepoint(pos):
                button.hover(True)
                if pg.mouse.get_pressed()[0] == 1 and button.state == False:
                    button.state = True
                    return button.func()
            else:
                button.hover(False)
                    
            if pg.mouse.get_pressed()[0] == 0:
                button.state = False

    def show(self):
        self.screen.blit(self.background,(0,0))

        dirty = self.all.draw(self.screen)

        for button in self.list_buttons:
            button.draw_text(self.screen)
        pg.display.update(dirty)
