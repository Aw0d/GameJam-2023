import pygame as pg
from menu.menu_components import Button, Text, Image



class Settings():
    def __init__(self, screen: pg.Surface):
        self.screen = screen
        
        
        logo = Image((384, 145), (512, 100), "images/logo.png")
        
        
        self.mute_button = Button((300, 364), "Mute Music", lambda : "Music")
        self.sound_effect_button = Button((750, 364), "Disable SFX", lambda: "SFX")
        self.back_button = Button((screen.get_width() - 216/2 - 15, screen.get_height() - 70/2 - 15), "Back", lambda: "back", "small_green")
        
        
        
        
        self.all = pg.sprite.RenderUpdates()
        
        
        self.music_on = True
        self.sfx_on = True
        
        self.all.add(logo)
        self.all.add(self.mute_button)
        self.all.add(self.sound_effect_button)
        self.all.add(self.back_button)
        
        self.background = pg.image.load("images/menu/fond.png")
        
    def update(self, events):
        # Détection des hovers et des clicks sur les boutons
        pos = pg.mouse.get_pos()
        if self.mute_button.rect.collidepoint(pos):
            if not self.mute_button.isHover:
                self.mute_button.hover(True)
            for event in events:
                match event.type:
                    case pg.MOUSEBUTTONUP:
                        if event.button == pg.BUTTON_LEFT:
                            if self.music_on:
                                self.mute_button.text.update_text("Unmute Music")
                                self.mute_button.change_color("red")
                            else:
                                self.mute_button.text.update_text("Mute Music")
                                self.mute_button.change_color("green")
                            self.music_on = not self.music_on
                            return self.mute_button.clicked()                    
        else:
            if self.mute_button.isHover:
               self.mute_button.hover(False)
               
        if self.sound_effect_button.rect.collidepoint(pos):
            if not self.sound_effect_button.isHover:
                self.sound_effect_button.hover(True)
            for event in events:
                match event.type:
                    case pg.MOUSEBUTTONUP:
                        if event.button == pg.BUTTON_LEFT:
                            if self.sfx_on:
                                self.sound_effect_button.text.update_text("Enable SFX")
                                self.sound_effect_button.change_color("red")
                            else:
                                self.sound_effect_button.text.update_text("Disable SFX")
                                self.sound_effect_button.change_color("green")
                            self.sfx_on = not self.sfx_on
                            return self.sound_effect_button.clicked()                    
        else:
            if self.sound_effect_button.isHover:
               self.sound_effect_button.hover(False)
               
        if self.back_button.rect.collidepoint(pos):
            if not self.back_button.isHover:
                self.back_button.hover(True)
            for event in events:
                match event.type:
                    case pg.MOUSEBUTTONUP:
                        if event.button == pg.BUTTON_LEFT:
                            return self.back_button.clicked()                    
        else:
            if self.back_button.isHover:
               self.back_button.hover(False)
           
    
    def show(self):
        self.screen.blit(self.background,(0,0))

        dirty = self.all.draw(self.screen)

        self.mute_button.draw_text(self.screen)
        self.sound_effect_button.draw_text(self.screen)
        self.back_button.draw_text(self.screen)
        pg.display.update(dirty)
        

        
        