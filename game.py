from config import Config
from snake import Snake
from apple import Apple
import pygame
import sys


class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(
            (Config.WINDOW_WIDTH, Config.WINDOWS_HEIGHT))
        self.clock = pygame.time.Clock()
        self.BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
        pygame.display.set_caption('Wormy')
        self.apple = Apple()
        self.snake = Snake()

    def draw(self):
        self.screen.fill(Config.BG_COLOR)
        # In here we'll draw our Snake, Apple, Grid and Score
        pygame.display.update()
        self.clock.tick(Config.FPS)

    def handleKeyEvents(self, event):
        if event.key == pygame.K_ESCAPE:
            pygame.quit()

    def run(self):
        run=True
        while run:  # main game loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run=False
                elif event.type == pygame.KEYDOWN:
                    self.handleKeyEvents(event)

            self.draw()

            # sys.exit()
            # elif event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_ESCAPE:
            #         pygame.quit()
            #         sys.exit()

        self.screen.fill((255, 255, 255))
        pygame.display.update()
        self.clock.tick(60)
