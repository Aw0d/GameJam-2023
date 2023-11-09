import pygame as pg
from menu.menu_components import Button, Text, Image

class CreditsMenu():
    def __init__(self, screen : pg.Surface):
        self.screen = screen

        logo = Image((500, 174), (512, 100), "images/logo.png")

        titre1 = Text("Sounds", (screen.get_width()/1.6, 420), 20, (0, 0, 0), "fonts/MarioWorldPixelColor-3zBwX.ttf", 800)
        titre2 = Text("Developer", (screen.get_width()/1.6, 220), 20, (0, 0, 0), "fonts/MarioWorldPixelColor-3zBwX.ttf", 800)
        titre3 = Text("Designer", (screen.get_width()/1.02, 220), 20, (0, 0, 0), "fonts/MarioWorldPixelColor-3zBwX.ttf", 800)
        titre4 = Text("Image", (screen.get_width()/1.02, 420), 20, (0, 0, 0), "fonts/MarioWorldPixelColor-3zBwX.ttf", 800)
        titre5 = Text("Font", (screen.get_width()/1.6, 620), 20, (0, 0, 0), "fonts/MarioWorldPixelColor-3zBwX.ttf", 800)
        titre6 = Text("Credit", (screen.get_width()/1.02, 620), 20, (0, 0, 0), "fonts/MarioWorldPixelColor-3zBwX.ttf", 800)

        text1 = Text("https://pixabay.com/", (screen.get_width()/1.6, 460), 15, (0, 0, 0), "fonts/TypefaceMarioWorldPixelFilledRegular-rgVMx.ttf", 800)
        text2 = Text("CAMUS Mathieu \n KALIC Benjamin \n ARCHILA Cesar \n KAZI-TANI Sami", (screen.get_width()/1.6, 305), 15, (0, 0, 0), "fonts/TypefaceMarioWorldPixelFilledRegular-rgVMx.ttf", 800)
        text3 = Text("KAZI-TANI Sami", (screen.get_width()/1.02, 260), 15, (0, 0, 0), "fonts/TypefaceMarioWorldPixelFilledRegular-rgVMx.ttf", 800)
        text4 = Text("https://giventofly.github.io/pixelit \n https://getemoji.com/ \n https://www.pngwing.com/", (screen.get_width()/1.02, 485), 15, (0, 0, 0), "fonts/TypefaceMarioWorldPixelFilledRegular-rgVMx.ttf", 800)
        text5 = Text("https://www.fontspace.com/", (screen.get_width()/1.6, 655), 15, (0, 0, 0), "fonts/TypefaceMarioWorldPixelFilledRegular-rgVMx.ttf", 800)
        text6 = Text("LOSER POV", (screen.get_width()/1.02, 655), 15, (0, 0, 0), "fonts/TypefaceMarioWorldPixelFilledRegular-rgVMx.ttf", 800)

        back_button = Button((screen.get_width() - 216/2 - 15, screen.get_height() - 70/2 - 15), "Back", lambda: "back", "small_green")

        self.list_buttons = [back_button]

        self.all = pg.sprite.RenderUpdates()

        self.all.add(logo)
        self.all.add(titre1)
        self.all.add(titre2)
        self.all.add(titre3)
        self.all.add(titre4)
        self.all.add(titre5)
        self.all.add(titre6)
        self.all.add(text2)
        self.all.add(text3)
        self.all.add(text1)
        self.all.add(text4)
        self.all.add(text5)
        self.all.add(text6)
        self.all.add(back_button)

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
