import pygame
from pygame.color import Color
from pygame import FULLSCREEN, SCALED
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE

class Monolith:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1920, 1080), FULLSCREEN | SCALED)
        self.running = True

    def run(self):
        clock = pygame.time.Clock()
        fps = 60
        while self.running:
            self.screen.fill(Color('cornflowerblue'))
            self.handle_events()            
            pygame.display.flip()
            clock.tick(fps)
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False

if __name__ == '__main__':
    Monolith().run()
