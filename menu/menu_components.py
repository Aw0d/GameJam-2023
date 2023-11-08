import pygame as pg

class Button(pg.sprite.Sprite):
    def __init__(self, x , y, image, func):
        super().__init__()
        #self.image = pg.Surface((100, 50))
        self.image = pg.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        #on enregistre l'Etat du button(True si il est clicked, FALSE sinon)
        self.state = False
        self.func = func

class Text(pg.sprite.Sprite):
    def __init__(self, text, pos, font_size=36, color=(255, 255, 255), font_name=None):
        super().__init__()

        self.text = text
        self.pos = pg.math.Vector2(pos)
        self.color = color
        self.font_size = font_size
        self.font_name = font_name
        self.font = pg.font.Font(font_name, font_size) if font_name else pg.font.Font(None, font_size)
        self.image = self.render_text()
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def render_text(self):
        return self.font.render(self.text, True, self.color)

    def update_text(self, text):
        self.text = text
        self.image = self.render_text()