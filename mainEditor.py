import pygame as pg
pg.mixer.init()
from menu.element_button import ElementButton
from levelCreator import GameEditor



if __name__ == "__main__":
    screenSize = (1024,768)
    screen = pg.display.set_mode(screenSize)
    game = GameEditor(screen)
    def test():
        return 1
    
    clock = pg.time.Clock()
    while not game.isEnded:
        dt = clock.tick(60)
        events = pg.event.get()
        for event in events:
            # Si on ferme la fenêtre, on arrête la boucle
            match event.type:
                case pg.QUIT:
                    # On ferme la fenêtre
                    running = False
        game.update(dt, events)
        pg.display.flip()