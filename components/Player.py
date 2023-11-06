import pygame as pg

class Player(pg.sprite.Sprite):

    def __init__(self, *groups):

        pg.sprite.Sprite.__init__(self, *groups)
        self.image = pg.Surface((20, 20))
        self.rect = self.image.get_rect()
        # Donne une couleur
        self.image.fill("blue")

        self.x = 10
        self.y = self.image.get_height
        self.setLoc(self.x, self.y)

        self.isJumping = False
        self.isSliding = False

    def setLoc(self, x, y):
        """ Definit les positions horizontale en x """
        # Change la position horizontal du rectangle qui définit la position
        self.rect.move_ip((x, y))
        self.x, self.y = (x, y)

    def jump(self):
        if (not self.isJumping):
            self.setLoc()
    
    def slide(self):
        pass