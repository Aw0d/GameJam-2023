import pygame as pg
from menu.menu_components import Text

class HUD():
    def __init__(self, screen_size):
        self.all = pg.sprite.RenderUpdates()

        self.score_text = Text("Score : 0", (0, 0), 56, (0,255,0))
        self.score_text.rect.topright = (screen_size[0] - 20, 20)
        self.all.add(self.score_text)

    def update_score(self, score):
        txt = "Score : " + str(score)
        self.score_text.update_text(txt)

    def draw(self, screen: pg.Surface):
        self.all.draw(screen)