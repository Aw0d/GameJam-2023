import pygame as pg
from menu.menu_components import Text, Image

pg.mixer.init()

class ElementButton(pg.sprite.Sprite):
    component_button = [pg.image.load("ressources/images/editor/component_button.png"), pg.image.load("ressources/images/editor/component_button_hover.png")]
    def __init__(self, name, func, pos, img: str):
        super().__init__()
        self.image = ElementButton.component_button[0]
        self.image.set_alpha(150)
        self.rect = self.image.get_rect()
        
        self.pos = pg.math.Vector2(pos)
        self.rect.topleft = self.pos

        self.func = func

        self.objetImage = Image((40,40),(0,0) ,img)
        self.objetImage.rect.topleft = (self.rect.left + 10, self.rect.top + self.rect.height/2 - self.objetImage.rect.height/2)
        #Nom de l'élément
        self.name = Text(name, (0,0), font_size=18)
        self.name.rect.topleft = self.rect.left + self.objetImage.rect.width + 50, self.rect.top + self.rect.height/2 - self.objetImage.rect.height/2
        
        
        self.all = pg.sprite.RenderUpdates()
        self.all.add(self.name)
        self.all.add(self.objetImage)

        

        # Si l'objet est un ground, alors il sera possible de modifier sa taille plus tard.
        if img.find("ground") != -1:
            self.width = True
        else:
            self.width = False

        self.hover = False
        self.isClicked = False
    
    
    def clicked(self):
        self.isClicked = True
        return self.func()
    
    
    def hoverOrClick(self):
        if self.hover or self.isClicked:
            self.image = ElementButton.component_button[1]
        else:
            self.image = ElementButton.component_button[0]

    def isSelected(self):
        return self.isClicked == True
    def isHover(self):
        return self.hover == True
    
    def setHover(self, b):
        self.hover = b

    def setSelected(self, b):
        self.isClicked = b
    
    
    def _draw(self, screen: pg.Surface):
        self.all.draw(screen)