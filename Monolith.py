import os
import pygame
from pygame.color import Color
from pygame import FULLSCREEN, SCALED
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE

def file_resource(*names):
    # return an os-independent filename inside data path
    return os.path.join('data', *names)

class Monolith:
    def __init__(self):
        pygame.init()
        screen_x, screen_y = 1920, 1080
        self.border_size = 16
        self.font_size = 16
        self.mono_font = pygame.font.Font(file_resource(
                         'Roboto_Mono', 'static', 'RobotoMono-Regular.ttf'), self.font_size)
        self.screen = pygame.display.set_mode((screen_x, screen_y), FULLSCREEN | SCALED)
        self.columns = int((screen_x - (self.border_size * 2)) / self.font_size)
        self.rows = int((screen_y - (self.border_size * 2)) / self.font_size)
        self.running = True

    def run(self):
        clock = pygame.time.Clock()
        fps = 60
        while self.running:
            self.screen.fill(Color('cornflowerblue'))
            self.print_at('Hello, World!', (0, 0))
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

    def print_at(self, text, position):
        graphical_pos = (self.border_size + (position[0] * self.font_size),
                         self.border_size + (position[1] * self.font_size))
        self.screen.blit(self.render_text(text, Color('white')), graphical_pos)

    def render_text(self, text, colour):
        return self.mono_font.render(text, True, colour)

if __name__ == '__main__':
    Monolith().run()
