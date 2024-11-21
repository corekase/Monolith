import os
import pygame
from pygame.color import Color
from pygame import FULLSCREEN, SCALED
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE

def file_resource(*names):
    # return an os-independent filename inside data path
    return os.path.join('data', *names)

def centre(bigger, smaller):
    # helper function that returns a centred position
    return int((bigger / 2) - (smaller / 2))

class Monolith:
    def __init__(self):
        pygame.init()
        self.mono_font = pygame.font.Font(file_resource(
                         'Roboto_Mono', 'static', 'RobotoMono-Regular.ttf'), 16)
        self.banner = self.render_text('Hello, World!', Color('white'))
        self.screen = pygame.display.set_mode((1920, 1080), FULLSCREEN | SCALED)
        self.running = True

    def run(self):
        clock = pygame.time.Clock()
        fps = 60
        x = centre(1920, self.banner.get_width())
        y = centre(1080, self.banner.get_height())
        while self.running:
            self.screen.fill(Color('cornflowerblue'))
            self.screen.blit(self.banner, (x, y))
            self.handle_events()            
            clock.tick(fps)
            pygame.display.flip()
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False

    def render_text(self, text, colour):
        return self.mono_font.render(text, True, colour)

if __name__ == '__main__':
    Monolith().run()
