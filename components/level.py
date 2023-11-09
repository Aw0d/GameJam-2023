import pygame as pg

class Level:
    def __init__(self, name):
        self.name = name
        # liste des positions des éléments d'une map
        # La clé correspond à l'objet
        # La valeur est un tuple contenant les coordonnées
        # Pour un Ground, c'est une liste contenant deux tuples, la position et la taille
        # exemple : {
        #   ["Chair", (10, 10)],
        #   ["Table", (60, 10)],
        #   ["Ground", [(100, 10), (50, 50)]]
        # }
        self.all = []

    def setName(self, name):
        self.name  = name


