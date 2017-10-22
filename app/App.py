'''
David Fuller

App class: Initializes application

10-15-2017
'''

import pygame
import random

from .Constants import *
from .processing import Processing


class App(object):
    '''
    Sets up and runs a Pygame application.
    '''
    
    def __init__(self, app_directory):
        '''
        App's init method.

        Stores application directory. Sets up the graphical user interface.
        Runs the applicaiton.

        Args:
            app_directory (str): Representation of application directory.
        '''
        
        self.app_directory = app_directory

        self.generated = False

        self.setup_GUI()

        self.run_app()

    def setup_GUI(self):
        '''
        Method sets up the graphical user interface.

        Initializes Pygame. Sets up the window size and title. Stores Pygame
        clock variable for setting frames per second.
        '''
        
        pygame.init()
        self.screen = pygame.display.set_mode(screen_resolution)
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()

        self.processing = Processing(self.screen)

    def random_color(self):
        '''
        Method chooses a random color.

        Returns:
            color object.
        '''
        
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return color(r = r, g = g, b = b)

    def draw_circle(self, x, y, radius):
        '''
        Method draws a series of circles recusrively.

        Args:
            x (int): x coordinate of circle.
            y (int): y coordinate of circle.
            radius (int): radius of circle.
        '''
        
        self.processing.ellipse(x, y, radius, radius)
        if radius > self.processing.strokeweight * 2:            
            self.draw_circle(x + radius * 0.5, y, radius * 0.5)
            self.draw_circle(x - radius * 0.5, y, radius * 0.5)
            if random.random() < 0.5:
                self.draw_circle(x, y - radius * 0.5, radius * 0.5)            
            if random.random() < 0.5:
                self.draw_circle(x, y + radius * 0.5, radius * 0.5)
        self.generated = True

    def run_app(self):
        '''
        Runs Pygame application.
        '''
        
        running = True
        while running:
            for event in pygame.event.get():
                
                # Handle quit event
                if event.type == pygame.QUIT:
                    running = False

                # Handle keyboard input
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_F5:
                        self.generated = False

            # Recursion stuff
            if not self.generated:
                self.screen.fill(black)
                self.processing.stroke(self.random_color())
                self.processing.noFill()            
                self.draw_circle(300, 300, 300)

            # Update Screen
            pygame.display.update()
            self.clock.tick(fps)            

        # Close app cleanly
        pygame.quit()
