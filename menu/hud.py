import pygame as pg
from menu.menu_components import Text

class HUD():
    def __init__(self, screen_size):
        self.all = pg.sprite.RenderUpdates()

        self.screen_size = screen_size

        self.score_text = Text("Score: 0", (0, 0), 22, (68,114,179))
        self.score_text.rect.topright = (self.screen_size[0] - 20, 20)
        self.all.add(self.score_text)
        
        self.score_background = pg.Surface((self.score_text.rect.width + 30, self.score_text.rect.height + 30))
        self.score_background.fill((253, 196, 49))
        self.score_background.set_alpha(190)

    def update_score(self, score):
        txt = "Score : " + str(score)
        self.score_text.update_text(txt)
        self.score_text.rect.topright = (self.screen_size[0] - 20, 20)

        self.score_background = pg.Surface((self.score_text.rect.width + 30, self.score_text.rect.height + 30))
        self.score_background.fill((253, 196, 49))
        self.score_background.set_alpha(190)

    def draw(self, screen: pg.Surface):
        screen.blit(self.score_background, (self.score_text.rect.left - 15, self.score_text.rect.top - 15))
        self.all.draw(screen)