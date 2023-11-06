import pygame as pg
from components.Player import Player
from components.Ground import Ground

class Game:
    
    def __init__(self, screen: pg.Surface):
        self.screen = screen

        # Crée une surface pour le fond du jeu de même taille que la fenêtre
        self.background = pg.Surface(self.screen.get_size())
        self.background.fill("white")

        # Dessine le font d'écran une première fois
        self.screen.blit(self.background,(0,0))

        # Création du sol
        ground = Ground(screen)
        self.ground_group = pg.sprite.Group()
        self.ground_group.add(ground)

        # Objet sous groupe pour avoir la liste des sprites et automatiser la mise à jour par update()
        # Automatise aussi l'affichage : draw() par défaut affiche dans l'écran image à la position rect
        self.all = pg.sprite.RenderUpdates()

        self.player = Player(self.ground_group)
        self.all.add(self.player)

        # Vrai si le jeu est fini
        self.isEnded = False

    def isRunning(self):
        if self.isEnded:
            return False
        for event in pg.event.get():
            match event.type:
                case pg.QUIT:
                    # On ferme la fenêtre
                    return False
        return True
    
    def update(self,dt : int):
        """
        Met à jour l'état du jeux en fonction du temps dt écoulé 
        """
        # Met à jours tous les sprites
        self.all.update(dt)

        # Vide l'écran en replacant le background
        self.all.clear(self.screen, self.background)

        self.player.move()

        self.ground_group.draw(self.screen)
        # Dessine tous les sprites dans la surface de l'écran
        dirty = self.all.draw(self.screen)
        # Remplace le background des zones modifiées par le mouvement des sprites
        pg.display.update(dirty)