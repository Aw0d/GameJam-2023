import pygame as pg
from menu.menu_components import Button, Text

GRIS = (211,211,211)

class MainMenu():
    def __init__(self, screen : pg.Surface):
        self.screen = screen
        titre_text = Text(512, 100, 'img/titre.jpeg')
        start_button = Button(512, 300, 'img/menu_button.png', lambda: 1)               #   1: Jeu
        menu_button = Button(512, 425, 'img/menu_button.png',lambda:print("OPTIONS"))
        inspect_button = Button(512, 550, 'img/menu_button.png',lambda:print("MODE INSPECTION"))
        exit_button = Button(512, 675, 'img/menu_button.png',lambda:print("EXIT"))
        
        self.list_buttons = [start_button, menu_button, exit_button, inspect_button]
        
        self.buttons = pg.sprite.RenderUpdates()

        self.buttons.add(titre_text)
        self.buttons.add(start_button)
        self.buttons.add(menu_button)
        self.buttons.add(inspect_button)
        self.buttons.add(exit_button)

        self.clear_background = pg.Surface(self.screen.get_size())
        self.clear_background.fill((202,228,241))

        self.screen.blit(self.clear_background,(0,0))
    
    def update(self):
        self.clear_background = pg.Surface(self.screen.get_size())
        self.clear_background.fill((202,228,241))
        self.screen.blit(self.clear_background,(0,0))
        dirty = self.buttons.draw(self.screen)
        pg.display.update(dirty)
        pos = pg.mouse.get_pos()
        for button in self.list_buttons:
            if button.rect.collidepoint(pos):
                if pg.mouse.get_pressed()[0] == 1 and button.state == False:
                    button.state = True
                    return button.func()
                    
            if pg.mouse.get_pressed()[0] == 0:
                button.state = False
        
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