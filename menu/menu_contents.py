import pygame as pg
from menu.element_button import ElementButton
from menu.element_button import Text
import pickle



class MenuContents():
    def __init__(self, screen: pg.Surface):
        self.screen = screen
        
        self.all = pg.sprite.RenderUpdates()
        
        self.buttons = []

        self.selection = 1

        # Selection :
        # Ground = 1
        # Malus = 2
        # Bonus = 3
        # Spike = 4
        # Table = 5
        # Chair = 6
        # End = 7
        # Delete = 8
        # Create Level = 9

        groundButton = ElementButton("Add Ground", lambda: self.setSelection(1), (5,0), "ressources/images/editor/ground_bloc.png")
        malusButton = ElementButton("Add Malus", lambda: self.setSelection(2), (5,75), "ressources/images/malus/alarm.png")
        bonusButton = ElementButton("Add Bonus", lambda: self.setSelection(3), (5,150), "ressources/images/bonus/lesson.png")
        spikeButton = ElementButton("Add Spike", lambda: self.setSelection(4), (5,225), "ressources/images/malus/pencil.png")
        tableButton = ElementButton("Add Table", lambda: self.setSelection(5), (5,300), "ressources/images/background/table.png")
        chairButton = ElementButton("Add Chair", lambda: self.setSelection(6), (5,375), "ressources/images/background/chair.png")
        endButton = ElementButton("Add End", lambda: self.setSelection(7), (5,450), "ressources/images/end/end_without_player.png")
        deleteButton = ElementButton("Delete", lambda: self.setSelection(8), (5,525), "ressources/images/editor/del_content.png")
        createLevel = ElementButton("Create Level", lambda: self.setSelection(9), (5,600), "ressources/images/editor/confirm_level.png")
        
        self.buttons.append(groundButton)
        self.buttons.append(malusButton)
        self.buttons.append(bonusButton)
        self.buttons.append(spikeButton)
        self.buttons.append(tableButton)
        self.buttons.append(chairButton)
        self.buttons.append(endButton)
        self.buttons.append(deleteButton)
        self.buttons.append(createLevel)

        for button in self.buttons:    
            self.all.add(button)
    

    def setSelection(self, nbSelect):
        self.selection = nbSelect

    def getSelection(self):
        return self.selection

    def update(self, events):
        pos = pg.mouse.get_pos()
        for button in self.buttons:
            if button.rect.collidepoint(pos):
                button.setHover(True)
                if pg.mouse.get_pressed()[0]:
                    for otherButton in self.buttons:
                        otherButton.setSelected(False)
                    button.setSelected(True)
                for event in events:
                    match event.type:
                        case pg.MOUSEBUTTONUP:
                            if event.button == pg.BUTTON_LEFT:
                                button.clicked()
            else:
                button.setHover(False)
            button.hoverOrClick()

    def getY(self):
        return self.contents_text.rect.bottom + 10

    def draw(self, screen: pg.Surface):
        self.all.draw(screen)
        for element in self.buttons:
            element._draw(screen)
        