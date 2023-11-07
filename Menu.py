import pygame as pg


GRIS = (211,211,211)




class Button(pg.sprite.Sprite):
    def __init__(self, x , y, image):
        super().__init__()
        #self.image = pg.Surface((100, 50))
        self.image = pg.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
    

class Menu_principale():

    def __init__(self, screen : pg.Surface ):
        self.screen = screen
        start_button = Button(512, 300, 'img/menu_button.png' )
        menu_button = Button(512, 425, 'img/menu_button.png')
        inspect_button = Button(512, 550, 'img/menu_button.png')
        exit_button = Button(512, 675, 'img/menu_button.png')
        
        self.buttons = pg.sprite.RenderUpdates()

        self.buttons.add(start_button)
        self.buttons.add(menu_button)
        self.buttons.add(inspect_button)
        self.buttons.add(exit_button)

        self.clear_background = pg.Surface(self.screen.get_size())
        self.clear_background.fill((202,228,241))

        self.screen.blit(self.clear_background,(0,0))
        
        
        

    def run(self):
        self.clear_background = pg.Surface(self.screen.get_size())
        self.clear_background.fill((202,228,241))
        self.screen.blit(self.clear_background,(0,0))
        dirty = self.buttons.draw(self.screen)
        pg.display.update(dirty)
            
        



            
if __name__ == "__main__":
    pg.init()
    pg.font.init()
    pg.display.set_caption("Menu de démarrage")
    screenSize = (1024,768)
    screen = pg.display.set_mode(screenSize)
    clock = pg.time.Clock()
    menu = Menu_principale(screen)
    
    running = True
    
    while running: 
        clock.tick(60)
        menu.run()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        pg.display.flip()
        
    pg.quit()