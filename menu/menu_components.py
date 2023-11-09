import pygame as pg

class Button(pg.sprite.Sprite):
    btn_image_green = [pg.image.load("ressources/images/menu/green_button.png"), pg.image.load("ressources/images/menu/green_button_hover.png")]
    btn_image_small_green = [pg.image.load("ressources/images/menu/small_green_button.png"), pg.image.load("ressources/images/menu/small_green_button_hover.png")]
    btn_image_red = [pg.image.load("ressources/images/menu/red_button.png"), pg.image.load("ressources/images/menu/red_button_hover.png")]

    btn_clicked_sound = pg.mixer.Sound("ressources/sounds/button_clicked.mp3")
    btn_hover_sound = pg.mixer.Sound("ressources/sounds/button_hover.mp3")
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
                Button.channel.play(Button.btn_hover_sound)
        elif not isHover:
            self.isHover = False
            self.image = self.images[0]

    def change_color(self, color = "green"):
        if color == "red":
            self.images = Button.btn_image_red
        else:
            self.images = Button.btn_image_green

    def clicked(self):
        Button.channel.play(Button.btn_clicked_sound)
        self.isHover = False
        return self.func()

import pygame as pg

class Text(pg.sprite.Sprite):
    def __init__(self, text, pos, font_size=24, color=(255, 255, 255), font_name="ressources/fonts/TypefaceMarioWorldPixelFilledRegular-rgVMx.ttf", max_width=None):
        super().__init__()

        self.text = text
        self.pos = pg.math.Vector2(pos)
        self.color = color
        self.font_size = font_size
        self.font_name = font_name
        self.max_width = max_width
        self.font = pg.font.Font(font_name, font_size)
        self.image = self.render_text()
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def render_text(self):
        if self.max_width:
            lines = self.split_text_lines(self.text, self.max_width)
            rendered_lines = [self.font.render(line, True, self.color) for line in lines]
            total_height = sum(line.get_height() for line in rendered_lines)
            surface = pg.Surface((self.max_width, total_height), pg.SRCALPHA)
            y_offset = 0
            for line in rendered_lines:
                surface.blit(line, (0, y_offset))
                y_offset += line.get_height()
            return surface
        else:
            return self.font.render(self.text, True, self.color)

    def split_text_lines(self, text, max_width):
        words = text.split(' ')
        lines = []
        current_line = ''
        
        for word in words:
            if word != "\n":
                test_line = current_line + ' ' + word if current_line else word
                width, _ = self.font.size(test_line)
                
                if width <= max_width:
                    current_line = test_line
                else:
                    lines.append(current_line)
                    current_line = word
            else:
                lines.append(current_line)
                current_line = ''
        
        lines.append(current_line)
        return lines

    def update_text(self, text):
        self.text = text
        self.image = self.render_text()
        self.rect = self.image.get_rect()
        self.rect.center = self.pos


class Image(pg.sprite.Sprite):
    def __init__(self, size, pos, image):
        super().__init__()

        self.image = pg.image.load(image)
        if size:
            self.image = pg.transform.smoothscale(self.image, size)

        self.rect = self.image.get_rect()

        self.pos = pg.math.Vector2(pos)

        self.rect.center = self.pos