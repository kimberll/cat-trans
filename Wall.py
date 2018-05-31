"""
Wall
Creates the walls on the board.
"""

from tkinter import *
import random

class Wall(object):
    
    def __init__(self):
        self.vertWalls = list()
        self.horizWalls = list()
        
    def createWalls(self, data):
        # Create vertical walls at random positions
        for i in range(1, 11):
            for j in range(1, 11):
                rI = random.randint(0, 2)
                rJ = random.randint(0, 2)
                if rI > 1 and rJ > 1:
                    self.vertWalls.append((data.offset + data.border + \
                                            i*(data.size + data.border), 
                                            data.offset + 2 * data.border + \
                                            j*(data.size + data.border)))
        # Create horizontal walls at random positions
        for i in range(1, 11):
            for j in range(1, 11):
                rI = random.randint(0, 2)
                rJ = random.randint(0, 2)
                if rI > 1 and rJ > 1:
                    self.horizWalls.append((data.offset + 2 * data.border + \
                                            i*(data.size + data.border), 
                                            data.offset + data.border + \
                                            j*(data.size + data.border)))

    def draw(self, canvas, data, width, height):
        # Draw vertical walls
        for (i, j) in self.vertWalls:
            canvas.create_rectangle(i, j, i + data.border, j + data.size, 
                                    fill = "white")
        # Draw horizontal walls
        for (i, j) in self.horizWalls:
            canvas.create_rectangle(i, j, i + data.size, j + data.border,
                                    fill = "white")
    
    # Return a list of all vertical and horizonal walls
    def getWalls(self, data):
        all = list()
        for (i, j) in self.vertWalls:
            all.append((i, j, i + data.border, j + data.size))
        for (i, j) in self.horizWalls:
            all.append((i, j, i + data.size, j + data.border))
        return all