'''
David Fuller

Food class - Handles the Food object.

10-18-2017
'''

import pygame

from .Constants import black, fill

class Processing(object):
    '''
    Sets up a Processing class
    '''
    
    def __init__(self, screen):
        '''
        Processing's init method.

        initializes Processing variables: stroke, fill, and color
 
        Args:
            screen (pygame.display): Screen object to draw Food on.
        '''
        
        self.screen = screen
        self.boolStroke = True
        self.strokecolour = black
        self.boolFill = True
        self.fillcolour = black
        self.strokeweight = 1

    def strokeWeight(self, weight):
        '''
        Sets stroke weight to given value
 
        Args:
            weight (int): value to set stroke weight to.
        '''
        
        self.strokeweight = weight

    def noStroke(self):
        '''
        Sets app to not use a stroke on shapes drawn.
        '''
        
        self.boolStroke = False

    def stroke(self, color):
        '''
        Sets app to use a stroke on shapes drawn, and the color to use for the
        stroke.

        Args:
            color (color object): RGB value of stroke color
        '''
        
        self.boolStroke = True
        self.strokecolour = color

    def noFill(self):
        '''
        Sets app to not use a fill on shapes drawn.
        '''
        
        self.boolFill = False

    def fill(self, color):
        '''
        Sets app to use a fill on shapes drawn, and the color to use for the
        fill.

        Args:
            color (color object): RGB value of fill color
        '''
        
        self.boolFill = True
        self.fillcolour = color

    def line(self, sx, sy, ex, ey):
        '''
        Method draws a line to and from the given points.

        Args:
            sx (int): x coordinate of line starting position
            sy (int): y coordinate of line starting position
            ex (int): x coordinate of line ending position
            ey (int): y coordinate of line ending position
        '''
        if self.boolStroke:
            start = (sx, sy)
            end = (ex, ey)
            pygame.draw.line(self.screen, \
                             self.strokecolour, \
                             start, end, self.strokeweight)

    def rect(self, x, y, width, height):
        '''
        Method draws a rectangle with the given arguments.

        Args:
            x (int): x coordinate of rectangle position
            y (int): y coordinate of rectangle position
            width (int): width of rectangle
            height (int): height of rectangle
        '''
        
        rectangle = (x, y, width, height)

        # Fill and Stroke
        if self.boolFill and self.boolStroke:
            # Stroke
            stroke_rectangle = (x - self.strokeweight, \
                                y - self.strokeweight, \
                                width + self.strokeweight * 2, \
                                height + self.strokeweight * 2)
            pygame.draw.rect(self.screen, \
                               self.strokecolour, \
                               stroke_rectangle, \
                               fill)
            
            # Fill
            pygame.draw.rect(self.screen, \
                             self.fillcolour, \
                             rectangle, \
                             fill)

        # Fill, no Stroke
        elif self.boolFill and not self.boolStroke:
            pygame.draw.rect(self.screen, \
                             self.fillcolour, \
                             rectangle, \
                             fill)

        # Stroke, no Fill
        elif not self.boolFill and self.boolStroke:
            pygame.draw.rect(self.screen, \
                             self.strokecolour, \
                             rectangle, \
                             self.strokeweight)

        # no Stroke, no Fill does nothing

    def ellipse(self, x, y, width, height):
        '''
        Method draws a ellipse with the given arguments.

        Args:
            x (int): x coordinate of ellipse center position
            y (int): y coordinate of ellipse center position
            width (int): width of rectangle containing ellipse
            height (int): height of rectangle containing ellipse
        '''
        
        x = x - width / 2
        y = y - height / 2
        rectangle = (x, y, width, height)
        
        if width > self.strokeweight * 2 and height > self.strokeweight * 2:
            # Fill and Stroke
            if self.boolFill and self.boolStroke:
                # Stroke
                stroke_rectangle = (x - self.strokeweight, \
                                    y - self.strokeweight, \
                                    width + self.strokeweight * 2, \
                                    height + self.strokeweight * 2)
                pygame.draw.ellipse(self.screen, \
                                   self.strokecolour, \
                                   stroke_rectangle, \
                                   fill)
                
                # Fill
                pygame.draw.ellipse(self.screen, \
                                   self.fillcolour, \
                                   rectangle, \
                                   fill)            

            # Fill, no Stroke
            elif self.boolFill and not self.boolStroke:
                pygame.draw.ellipse(self.screen, \
                                   self.fillcolour, \
                                   rectangle, \
                                   fill)

            # Stroke, no Fill
            elif not self.boolFill and self.boolStroke:
                pygame.draw.ellipse(self.screen, \
                                    self.strokecolour, \
                                    rectangle, \
                                    self.strokeweight)

            # no Stroke, no Fill does nothing
        
