import pygame as pg

class Level:
    def __init__(self, name):
        self.name = name
        #liste des positions des éléments d'une map
        self.contents = []

    def setName(self, name):
        self.name  = name
    
    def addContent(self, content):
        self.contents.append(content)


