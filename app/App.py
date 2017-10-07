################################################################################
#                                                                              #
# David Fuller                                                                 #
#                                                                              #
# App class: App initializer                                                   #
#                                                                              #
# Created on 2016-12-29                                                        #
#                                                                              #
################################################################################

################################################################################
#                                                                              #
#                              IMPORT STATEMENTS                               #
#                                                                              #
################################################################################

from   .Constants  import *            # Constants file
from   .processing import Processing   # Processing style package
import pygame                          # For GUI
import random

################################################################################
#                                                                              #
#                                   APP CLASS                                  #
#                                                                              #
################################################################################

class App(object):

    ############################################################################
    #                                                                          #
    #                               CONSTRUCTOR                                #
    #                                                                          #
    ############################################################################
    
    def __init__(self, appDirectory: str) -> None:
        self.appDirectory = appDirectory

        self.generated = False

        # Set up GUI
        self.setupGUI()

        # Run app
        self.runApp()

    ############################################################################
    #                                                                          #
    #                                 METHODS                                  #
    #                                                                          #
    ############################################################################

    # Mehtod sets up GUI
    def setupGUI(self) -> None:
        # Screen attributes
        pygame.init()
        self.screen = pygame.display.set_mode(screen_resolution)
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()

        self.processing = Processing(self.screen)

    # Method generates and returns a random color
    def random_color(self) -> color:
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return color(r = r, g = g, b = b)

    # Recursive method draws a bunch of circles
    def drawCircle(self, x, y, radius) -> None:
        self.processing.ellipse(x, y, radius, radius)
        if radius > self.processing.strokeweight * 2:            
            self.drawCircle(x + radius * 0.5, y, radius * 0.5)
            self.drawCircle(x - radius * 0.5, y, radius * 0.5)
            if random.random() < 0.5:
                self.drawCircle(x, y - radius * 0.5, radius * 0.5)            
            if random.random() < 0.5:
                self.drawCircle(x, y + radius * 0.5, radius * 0.5)
        self.generated = True

    # Method runs app
    def runApp(self) -> None:
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
                self.drawCircle(300, 300, 300)

            # Update Screen
            pygame.display.update()
            self.clock.tick(fps)            

        # Close app cleanly
        pygame.quit()
