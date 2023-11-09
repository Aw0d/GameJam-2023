import pygame as pg

class Button(pg.sprite.Sprite):
    btn_image_green = [pg.image.load("images/menu/green_button.png"), pg.image.load("images/menu/green_button_hover.png")]
    btn_image_small_green = [pg.image.load("images/menu/small_green_button.png"), pg.image.load("images/menu/small_green_button_hover.png")]
    btn_image_red = [pg.image.load("images/menu/red_button.png"), pg.image.load("images/menu/red_button_hover.png")]

    btn_clicked_sound = pg.mixer.Sound("sounds/button_clicked.mp3")
    btn_hover_sound = pg.mixer.Sound("sounds/button_hover.mp3")
    channel = pg.mixer.Channel(2)

    def __init__(self, pos, text, func, btn_color = "green"):
        super().__init__()

        font_size = 24
        if btn_color == "red":
            self.images = Button.btn_image_red
        elif btn_color == "small_green":
            self.images = Button.btn_image_small_green
            font_size = 18
        else:
            self.images = Button.btn_image_green
        

        self.image = self.images[0]
        self.rect = self.image.get_rect()

        self.text = Text(text, pos, font_size)

        self.pos = pg.math.Vector2(pos)

        self.rect.center = self.pos

        self.func = func
        self.isHover = False        

    def draw_text(self, screen):
        screen.blit(self.text.image, (self.text.pos.x - self.text.image.get_width()/2, self.text.pos.y - self.text.image.get_height()/2))  # Dessinez le texte sur le bouton

    def hover(self, isHover):
        if isHover and not self.isHover:
            self.isHover = True
            self.image = self.images[1]
            if not Button.channel.get_busy():
                print("btn hover")
                Button.channel.play(Button.btn_hover_sound)
        elif not isHover:
            self.isHover = False
            self.image = self.images[0]

    def clicked(self):
        Button.channel.play(Button.btn_clicked_sound)
        self.isHover = False
        return self.func()

class Text(pg.sprite.Sprite):
    def __init__(self, text, pos, font_size=24, color=(255, 255, 255), font_name="fonts/TypefaceMarioWorldPixelFilledRegular-rgVMx.ttf"):
        super().__init__()

        self.text = text
        self.pos = pg.math.Vector2(pos)
        self.color = color
        self.font_size = font_size
        self.font_name = font_name
        self.font = pg.font.Font(font_name, font_size)
        self.image = self.render_text()
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def render_text(self):
        return self.font.render(self.text, True, self.color)

    def update_text(self, text):
        self.text = text
        self.image = self.render_text()

class Image(pg.sprite.Sprite):
    def __init__(self, size, pos, image):
        super().__init__()

        self.image = pg.image.load(image)
        self.image = pg.transform.smoothscale(self.image, size)

        self.rect = self.image.get_rect()

        self.pos = pg.math.Vector2(pos)

        self.rect.center = self.pos