import pygame as pg

class Level:
    def __init__(self, name , background="../images/background2.png"):
        self.name = name
        self.background = background
        #liste des positions des éléments d'une map
        self.contents = []

    def setName(self, name):
        self.name  = name
    
    def setBackground(self, background):
        self.background = background
    
    def addContent(self, content):
        self.contents.append(content)

    def deleteContent(self, content):
        self.contents.remove(content)
    