import pygame
from sys import exit
from classes import *

class Game:
    def __init__(self, width, height, title):
        pygame.init()

        self.SCREEN = pygame.display.set_mode((width, height))
        self.SCREEN_BG = 'black'

        pygame.display.set_caption(title)

        self.CLOCk = MyClock(60)
    
    def quit(self):
        pygame.quit()
        exit()
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
            
            self.SCREEN.fill(self.SCREEN_BG)

            pygame.display.update()
            self.CLOCk.tick()

if __name__ == '__main__':
    game = Game(800, 600, 'Flower Coloring')
    game.run()