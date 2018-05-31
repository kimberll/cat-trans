"""
Player
Creates the player on the board.
"""

from tkinter import *
import random
import time

class Player(object):
    
    def __init__(self, data):
        self.x = data.offset + 2 * data.border
        self.y = data.offset + 2 * data.border
        self.indexX, self.indexY = 0, 0
        self.playerColor = "gray"
        self.step = data.size + data.border
    
    # Start the player at the top left square again
    def reset(self, data):
        Player.__init__(self, data)
    
    def draw(self, canvas, data):
        canvas.create_rectangle(self.x, self.y, 
                                self.x + data.size, 
                                self.y + data.size, 
                                fill = self.playerColor)
    
    def move(self, move, data):
        # Every time player moves by a fixed step
        posMove = self.step + data.size
        # Up
        if move == "Up" and self.y - data.size > data.offset and \
            Player.isValid(self, data, 0, -1):
            self.y -= self.step 
            self.indexY -= 1
        # Right
        elif move == "Right" and self.x + posMove < data.width // 2 - 20 and \
            Player.isValid(self, data, 1, 0):
            self.x += self.step
            self.indexX += 1
        # Left
        elif move == "Left" and self.x - data.size >  data.offset and \
            Player.isValid(self, data, -1, 0):
            self.x -= self.step
            self.indexX -= 1
        # Down
        elif move == "Down" and self.y + posMove < data.height - 20 and \
            Player.isValid(self, data, 0, 1):
            self.y += self.step
            self.indexY += 1

    # Check if move is valid
    def isValid(self, data, moveX, moveY):
        afterX = self.x + moveX * self.step
        afterY = self.y + moveY * self.step
        for (j, k, l, m) in data.all:
            if ((self.x + data.size <= j and afterX + data.size > j and \
                k <= (2 * self.y + data.size) / 2 <= m) \
                or (self.x >= l and afterX < l and \
                k <= (2 * self.y + data.size) / 2 <= m) \
                or (self.y + data.size <= k and afterY + data.size > k and \
                j <= (2 * self.x + data.size) / 2 <= l) \
                or (self.y >= m and afterY < m and \
                j <= (2 * self.x + data.size) / 2 <= l)):
                return False
        return True