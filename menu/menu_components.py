import pygame as pg

class Button(pg.sprite.Sprite):
    btn_image_green = [pg.image.load("images/menu/green_button.png"), pg.image.load("images/menu/green_button_hover.png")]
    btn_image_red = [pg.image.load("images/menu/red_button.png"), pg.image.load("images/menu/red_button_hover.png")]

    def __init__(self, pos, text, func, btn_color = "green"):
        super().__init__()

        if btn_color == "red":
            self.images = Button.btn_image_red
        else:
            self.images = Button.btn_image_green
        

        self.image = self.images[0]
        self.rect = self.image.get_rect()

        self.text = Text(text, pos)
        print("text ", text, " self.rect.center ", pos)

        self.pos = pg.math.Vector2(pos)

        self.rect.center = self.pos

        #on enregistre l'Etat du button(True si il est clicked, FALSE sinon)
        self.state = False
        self.func = func

    def draw_text(self, screen):
        screen.blit(self.text.image, (self.text.pos.x - self.text.image.get_width()/2, self.text.pos.y - self.text.image.get_height()/2))  # Dessinez le texte sur le bouton

    def hover(self, isHover):
        if isHover:
            self.image = self.images[1]
        else:
            self.image = self.images[0]

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