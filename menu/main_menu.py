import pygame as pg
from menu.menu_components import Button, Text, Image

GRIS = (211,211,211)

class MainMenu():
    def __init__(self, screen : pg.Surface):
        self.screen = screen

        logo = Image((384, 145), (512, 100), "images/logo.png")

        start_button = Button((512, 300), "Play", lambda: "play")
        menu_button = Button((512, 425), "Settings", lambda:print("OPTIONS"))
        inspect_button = Button((512, 550), "Level Editor", lambda:print("MODE INSPECTION"))
        exit_button = Button((512, 675), "Exit", lambda: "quit", "red")
        
        self.list_buttons = [start_button, menu_button, exit_button, inspect_button]
        
        self.all = pg.sprite.RenderUpdates()

        self.all.add(logo)
        self.all.add(start_button)
        self.all.add(menu_button)
        self.all.add(inspect_button)
        self.all.add(exit_button)

        self.background = pg.Surface(self.screen.get_size())
        self.background.fill((202,228,241))
        self.background.set_alpha(190)
    
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
        
if __name__ == "__main__":
    pg.init()
    pg.font.init()
    pg.display.set_caption("Menu de démarrage")
    screenSize = (1024,768)
    screen = pg.display.set_mode(screenSize)
    clock = pg.time.Clock()
    menu = MainMenu(screen)
    
    running = True
    
    while running: 
        clock.tick(60)
        menu.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        pg.display.flip()
        
    pg.quit()