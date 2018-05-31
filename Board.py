"""
Board
Creates the board that the play mode is based on.
"""

from tkinter import *
import random

class Board(object):
    
    def __init__(self):
        self.border = True
    
    def draw(self, canvas, data, width, height):
        # Left border
        canvas.create_rectangle(data.offset + data.border, 
                                data.offset + data.border, 
                                data.offset + 2 * data.border, 
                                height - data.offset, 
                                fill = "lightsalmon")
        # Right border
        canvas.create_rectangle(width - data.offset - data.border, 
                                data.offset + data.border,  
                                width - data.offset, 
                                height - data.offset,
                                fill = "lightgreen")
        # Top border
        canvas.create_rectangle(data.offset + data.border, 
                                data.offset + data.border,  
                                width - data.offset - data.border, 
                                data.offset + 2 * data.border,
                                fill = "deepskyblue")
        # Bot border
        canvas.create_rectangle(data.offset + data.border, 
                                height - data.offset,  
                                width - data.offset - data.border, 
                                height - data.offset - data.border,
                                fill = "gold")