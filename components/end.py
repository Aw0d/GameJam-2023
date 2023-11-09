from time import sleep
import pygame as pg

class EndGame(pg.sprite.Sprite):
    imgs_end = [pg.image.load("images/end/end_without_player.png"), pg.image.load("images/end/end_with_player.png")]

    def __init__(self, x, y):
        super().__init__()

        self.image = EndGame.imgs_end[0]
        self.rect = self.image.get_rect()

        self.pos = pg.math.Vector2((x, y))
        # Positionner le rectangle aux coordonnées spécifiées (x, y)
        self.rect.bottomleft = self.pos

        self.isEnded = False

        self.channel = pg.mixer.Channel(3)

    def update(self, dt, speed):
        self.pos.x -= speed * dt
        self.rect.bottomleft = self.pos

    def player_ended(self):
        self.image = EndGame.imgs_end[1]
        
        if not self.channel.get_busy():
            self.channel.play(pg.mixer.Sound("sounds/victory.mp3"))
