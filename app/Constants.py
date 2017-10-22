'''
David Fuller

Constants file - File contains application constants.

10-5-2017
'''

from collections import namedtuple

point = namedtuple('point', ['x', 'y'])
resolution = namedtuple('resolution', ['width', 'height'])
color = namedtuple('color', ['r', 'g', 'b'])

black = color(r = 0, b = 0, g = 0)
white = color(r = 255, b = 255, g = 255)
purple = color(r = 128, g = 0, b = 128)

screen_resolution = resolution(width = 600, height = 600)

title = "Recursion Challenge"
fps = 60
