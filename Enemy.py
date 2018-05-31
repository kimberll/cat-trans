"""
Enemy
Creates the characters that are not correct but place on the board
to challenge the player.
"""

from tkinter import *
from Chinese import chineseChar
from Korean import koreanChar
import random

class Enemy(object):
    
    # Function that returns random integer between 70 and 205
    r = lambda: random.randint(70,205)
  
    def __init__(self, num, language):
        self.coord = list()
        self.num = num
        self.wrong = list()
        if language == "Chinese":
            self.char = chineseChar
        else:
            self.char = koreanChar

    # Enemy init
    def createEnemies(self, data):
        # Pick random starting position for each enemy
        for i in range(self.num):
            r = random.choice(self.char)
            while r in data.allW:
                r = random.choice(self.char)
            x = 66 + random.randint(1, 10) * data.diff 
            y = 66 + random.randint(1, 10) * data.diff 
            d = random.randint(0, 3)
            self.coord.append((x, y, d, r, 
                            '#%02X%02X%02X' % (Enemy.r(),Enemy.r(),Enemy.r())))
            data.allW.append(r)
    
    def draw(self, canvas, data):
        # Draw all words chosen
        for i in range(len(self.coord)):
            x, y, d, txt, wC = self.coord[i]
            canvas.create_text(x + 0.5 * data.size, 
                            y + 0.5 * data.size, 
                            anchor = "center", text = txt, 
                            fill = wC, font="Calibri 27 bold")
        wrong = "".join(self.wrong)
    
    # Check for collison
    def collide(self, data):
        i = 0
        while i < len(self.coord):
            x, y, d, txt, wC = self.coord[i]
            if (x <= data.player.x <= x + data.size \
                or x <= data.player.x + data.size <= x + data.size) \
                and (y <= data.player.y <= y + data.size \
                or y <= data.player.y  + data.size <= y + data.size):
                    x, y, d, txt, wC = self.coord.pop(i)
                    self.wrong.append(txt)
                    data.allPicked.append(txt)
                    return True
            i += 1
        return False
    
    # Move the word
    def move(self, data):
        for i in range(len(self.coord)):
            newD = None
            x, y, d, txt, wC = self.coord[i]
            if data.timer % 100 == 0:
                r = random.randint(0, 15)
                if r == 0:
                    d = random.randint(0, 3)
            if d == 0 and y - 2 > data.offset + data.border and \
            Enemy.isValid(self, data, 0, -2, i):
                y -= 2
            elif d == 1 and x + 2 < data.width // 2 - data.offset - data.border\
             - data.size and Enemy.isValid(self, data, 2, 0, i):
                x += 2
            elif d == 2 and x - 2 > data.offset + data.border and \
            Enemy.isValid(self, data, -2, 0, i):
                x -= 2
            elif d == 3 and y + 2 < data.height - data.offset - data.border \
            - data.size and Enemy.isValid(self, data, 0, 2, i):
                y += 2
            else:
                newD = random.randint(0, 3)
            if newD == None:
                self.coord[i] = x, y, d, txt, wC
            else:
                self.coord[i] = x, y, newD, txt, wC
    
    # Check if move is valid
    def isValid(self, data, moveX, moveY, i):
        x, y, d, txt, wC = self.coord[i] 
        afterX = x + moveX 
        afterY = y + moveY 
        for (j, k, l, m) in data.all:
            if ((x + data.size <= j and afterX + data.size > j and \
                    k <= (2 * y + data.size) / 2 <= m) \
                or (x >= l and afterX < l and \
                    k <= (2 * y + data.size) / 2 <= m) \
                or (y + data.size <= k and \
                    afterY + data.size > k and \
                    j <= (2 * x + data.size) / 2 <= l) \
                or (y >= m and afterY < m and \
                    j <= (2 * x + data.size) / 2 <= l)):
                newD = random.randint(0, 3)
                self.coord[i] = x, y, newD, txt, wC
                return False
        return True