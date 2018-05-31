"""
Word
Creates the characters in the sentence that is to be matched.
"""

from tkinter import *
from Chinese import chineseVerbs
from Korean import koreanVerbs
import random

class Word(object):
    
    # Function that returns random integer between 70 and 205
    r = lambda: random.randint(70,205)
    
    def __init__(self, language):
        self.coord = list()
        self.sentence = ""
        self.sent = list()
        self.picked = list()
        self.english = ""
        self.stringColor = "white"
    
    # Either sets verbs list to Chinese list or Korean list depending on lang
    def setLanguage(self, data):
        if data.lang == "Chinese":
            data.defaultList = chineseVerbs
        else:
            data.defaultList = koreanVerbs
        data.defaultAndCustomList = data.defaultList

    # Take out trailing punctuation not to be included on the game board
    def removePunc(s):
        if s[-1] == "." or "。" or "!":
            return s[:-1]
        return s

    # Word init
    def createWords(self, data):
        # Practice missed word
        l = len(list(data.wDict.keys()))
        if random.randint(0, 4) == 0:
            try:
                i = random.choice(list(data.wDict.keys()))
                r = Word.findIndex(self, data, i)
                self.word = data.defaultList[r % len(data.defaultList)][1]
                self.sentence = data.defaultList[r % len(data.defaultList)][2]
                self.sentence = Word.removePunc(self.sentence)
                self.sent = list(self.sentence)
                self.english = data.defaultList[r % len(data.defaultList)][4]
            except:
                r = random.randint(0, len(data.defaultAndCustomList))
                self.word = data.defaultAndCustomList[r % len(data.defaultAndCustomList)][1]
                self.sentence = data.defaultAndCustomList[r % len(data.defaultAndCustomList)][2]
                self.sentence = Word.removePunc(self.sentence)
                self.sent = list(self.sentence)
                self.english = data.defaultAndCustomList[r % len(data.defaultAndCustomList)][4]
        # Practice random word
        else:
            r = random.randint(0, len(data.defaultAndCustomList))
            self.word = data.defaultAndCustomList[r % len(data.defaultAndCustomList)][1]
            self.sentence = data.defaultAndCustomList[r % len(data.defaultAndCustomList)][2]
            self.sentence = Word.removePunc(self.sentence)
            self.sent = list(self.sentence)
            self.english = data.defaultAndCustomList[r % len(data.defaultAndCustomList)][4]
        self.picked = list()
        # Pick random starting position for each word
        for word in self.sent:
            if not word == "." and not word == " ":
                x = 66 + random.randint(1, 10) * data.diff 
                y = 66 + random.randint(1, 10) * data.diff 
                d = random.randint(0, 3)
                self.coord.append((x, y, d, word, 
                                '#%02X%02X%02X' % (Word.r(),Word.r(),Word.r())))
                data.allW.append(word)
    
    def draw(self, canvas, data):
        # Draw all words in the sentence
        for i in range(len(self.coord)):
            x, y, d, txt, wC = self.coord[i]
            canvas.create_text(x + 0.5 * data.size, 
                            y + 0.5 * data.size, 
                            anchor = "center", text = txt, 
                            fill = wC, font="Calibri 27 bold")
        english = "".join(self.english)
        picked = "".join(self.picked)
        
        # Play
        if data.play:
            # Display English sentence
            canvas.create_text(data.width * 3 / 4 - 100, data.height * 3 / 20, 
                                anchor = "center", text = "Translate me:", 
                                fill = "white", font="Calibri 25 bold")
            canvas.create_text(data.width * 3 / 4 - 100, data.height * 4 / 20, 
                                anchor = "center", text = english, 
                                fill = "white", font="Calibri 25 bold")
        
        # If checked and wrong, display correct answer
        if data.wrong:
            canvas.create_text(data.width * 3 / 4 - 100, data.height * 9 / 20, 
                                anchor = "center", text = "Correct Answer:", 
                                fill = "tomato", font="Calibri 25 bold")
            canvas.create_text(data.width * 3 / 4 - 100, data.height * 10 / 20, 
                                anchor = "center", text = self.sentence, 
                                fill = "tomato", font="Calibri 25 bold")
        # If checked and correct, say good job!
        if data.correct:
            canvas.create_text(data.width * 3 / 4 - 100, data.height * 9 / 20, 
                                anchor = "center", text = "Good job!", 
                                fill = "springgreen", font="Calibri 25 bold")
    
    # Check for collision
    def collide(self, data):
        i = 0
        while i < len(self.coord):
            x, y, d, txt, wC = self.coord[i]
            if (x <= data.player.x <= x + data.size \
                or x <= data.player.x + data.size <= x + data.size) \
                and (y <= data.player.y <= y + data.size \
                or y <= data.player.y  + data.size <= y + data.size):
                    x, y, d, txt, wC = self.coord.pop(i)
                    self.picked.append(txt)
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
                Word.isValid(self, data, 0, -2, i):
                y -= 2
            elif d == 1 and x + 2 < data.width // 2 - data.offset \
                - data.border - data.size and Word.isValid(self, data, 2, 0, i):
                x += 2
            elif d == 2 and x - 2 > data.offset + data.border and \
                Word.isValid(self, data, -2, 0, i):
                x -= 2
            elif d == 3 and y + 2 < data.height - data.offset \
                - data.border - data.size and Word.isValid(self, data, 0, 2, i):
                y += 2
            else:
                newD = random.randint(0, 3)
            if newD == None:
                self.coord[i] = x, y, d, txt, wC
            else:
                self.coord[i] = x, y, newD, txt, wC

    # Check player created answer
    def checkAnswer(self, data):
        picked = "".join(data.allPicked)
        self.sentence = self.sentence.replace(' ', '')
        try:
        # Add to aDict whether right or wrong
            if self.word in data.aDict:
                data.aDict[self.word] = data.aDict[self.word] + 1
            else:
                data.aDict[self.word] = 1
        except:
            print("CUSTOM PRACTICE")
        # Case when correct
        if picked == self.sentence:
            try:
                if self.word in data.cDict:
                    data.cDict[self.word] = data.cDict[self.word] + 1
                else:
                    data.cDict[self.word] = 1
            except:
                print("CUSTOM PRACTICE")
            data.correct = True
            data.stringColor = "springgreen"
            data.currXP += 5
            return True
        # Case when wrong
        else:
            try: 
                if self.word in data.wDict:
                    data.wDict[self.word] = data.wDict[self.word] + 1
                else:
                    data.wDict[self.word] = 1
            except:
                print("CUSTOM PRACTICE")
            data.wrong = True
            data.stringColor = "tomato"
            return False
    
    # Check if move is valid
    def isValid(self, data, moveX, moveY, i):
        x, y, d, txt, wC = self.coord[i] 
        afterX = x + moveX 
        afterY = y + moveY 
        for (j, k, l, m) in data.all:
            if ((x + data.size <= j and afterX + data.size > j and \
                k <= (2 * y + data.size) / 2 <= m) \
                or (x >= l and afterX < l and k <= (2 * y + data.size) / 2 <= m) \
                or (y + data.size <= k and afterY + data.size > k and \
                j <= (2 * x + data.size) / 2 <= l) \
                or (y >= m and afterY < m and j <= (2 * x + data.size) / 2 <= l)):
                newD = random.randint(0, 3)
                self.coord[i] = x, y, newD, txt, wC
                return False
        return True
    
    # Returns word, sentence, pronounciation, english in a tuple
    def getVocabWord(self, data):
        try:
            newWord, oldWord, newSent, pronounciation, english = random.choice(data.defaultAndCustomList)
        except:
            newWord, oldWord, newSent, pronounciation, english = random.choice(data.defaultList)
        return (newWord, oldWord, newSent, pronounciation, english)
    
    # Takes off most recently added character to the player's string
    def delete(self, data):
        x = 66 + random.randint(1, 10) * data.diff 
        y = 66 + random.randint(1, 10) * data.diff 
        d = random.randint(0, 3)
        try:
            txt = data.allPicked.pop()
            self.coord.append((x, y, d, txt,
                            '#%02X%02X%02X' % (Word.r(),Word.r(),Word.r())))
        except: 
            print("LIST IS EMPTY")
        
    # Returns index of a specific player and count
    def findIndex(self, data, i):
        for j in range(len(data.defaultList)):
            if data.defaultList[j][1] == i:
                return j