"""
Game
Launches the game and is the center of all features.
"""

from tkinter import *
from Board import *
from Enemy import *
from Leaderboard import *
from Player import *
from Progress import *
from Wall import *
from Word import *
from Chinese import chineseVerbs
from Korean import koreanVerbs
from googletrans import Translator # https://pypi.python.org/pypi/googletrans
import ast
import os
import random
import re
import time

def init(data):
    # Board specs init
    data.size = data.width // 30
    data.border = data.size * 0.15
    data.offset = 51
    data.diff = 57.5
    
    # Player and board init
    data.player = Player(data)
    data.board = Board()
    
    # Walls init
    data.walls = Wall()
    data.walls.createWalls(data)
    data.all = data.walls.getWalls(data)
    
    # Leaderboard init
    data.leader = Leaderboard()
    
    # Start init
    data.timer = 0
    data.allPicked = list()
    data.boxText = "Check answer"
    data.stringColor = "white"
        
    # Bools init
    data.language = True
    data.home = False
    data.play = False
    data.learn = False
    data.custom = False
    data.progress = False
    data.leaderboard = False
    data.about = False
    data.correct = False
    data.wrong = False
    data.next = False
    data.saved = False
    data.showEnglish = False
    data.showPronounciation = False
    
    # Player stored info init
    data.cDict = dict()
    data.wDict = dict()
    data.aDict = dict()
    data.defaultList = list()
    data.customList = list()
    data.customEnglishList = list()
    data.defaultAndCustomList = list()
    
    # Leaderboard stored info init
    data.lDict = dict()
    
    # Progress info init
    data.prog = Progress()
    
    data.currXP = 0
    data.allXP = 0
    
    # Translator init
    data.translator = Translator()
        
def initWordEnemy(data):
    # Make words and initialize their random positions
    data.count = 0
    data.allW = list()
    data.word = Word(data.lang)
    data.word.setLanguage(data)
    data.word.createWords(data) 
    
    # Get first word
    (data.newWord, data.oldWord, data.newSent, data.pronounciation, \
        data.english) = data.word.getVocabWord(data) 
        
    # Make enemies and initialize their random positions
    data.enemy = Enemy(random.randint(5, 10), data.lang)
    data.enemy.createEnemies(data) 

def mousePressed(event, data):
    # Language page
    if data.language:
        left = data.width * 3 / 5 - 75
        right = data.width * 4 / 5 - 75
        genH = data.height / 30
        if (left <= event.x <= right and \
            12 * genH <= event.y <= 14 * genH):
                data.language = False
                # Set language to Chinese
                data.lang = "Chinese"
                initWordEnemy(data)
                data.home = True
                read(data)
                readLeaderboard(data)
        elif (left <= event.x <= right and \
            15 * genH <= event.y <= 17 * genH):
                data.language = False
                # Set language to Korean
                data.lang = "Korean"
                initWordEnemy(data)
                data.home = True
                read(data)
                readLeaderboard(data)
    # Home page
    elif data.home:
        left = data.width * 3 / 5 - 75
        right = data.width * 4 / 5 - 75
        genH = data.height / 30
        if (left <= event.x <= right and \
            9 * genH <= event.y <= 11 * genH):
                data.home = False
                # Change to play
                data.play = True
        elif (left <= event.x <= right and \
            12 * genH <= event.y <= 14 * genH):
                data.home = False
                # Change to learn
                data.learn = True
        elif (left <= event.x <= right and \
            15 * genH <= event.y <= 17 * genH):
                # Pop custom page
                data.custom = True
        elif (left <= event.x <= right and \
            18 * genH <= event.y <= 20 * genH):
                data.home = False
                # Change to progress
                data.progress = True
        elif (left <= event.x <= right and \
            21 * genH <= event.y <= 23 * genH):
                data.home = False
                # Change to leaderboards
                data.leaderboard = True
        elif (left <= event.x <= right and \
            24 * genH <= event.y <= 26 * genH):
                data.home = False
                # Change to about
                data.about = True
    # Play page
    elif data.play:
        genW = data.width / 40
        genH = data.height / 40
        # Check if button is clicked
        if (30 * genW - 175 <= event.x <= 30 * genW - 25) and \
            (23 * genH <= event.y <= 25 * genH):
                # Check if the player's answer is correct
                if data.boxText != "Next":
                    check = data.word.checkAnswer(data)
                # Move based on answer
                if data.boxText == "Check answer": 
                    data.boxText = "Next"
                # Go to next sentence
                elif data.boxText == "Next":
                    data.count += 1
                    resetGame(data)
                else:
                    data.wrong = True
                    data.boxText = "Next"
        # Backspace button
        if (30 * genW - 175 <= event.x <= 30 * genW - 25) and \
            (26 * genH <= event.y <= 28 * genH):
                data.word.delete(data)
        # Save button
        if (30 * genW - 175 <= event.x <= 30 * genW - 25) and \
            (29 * genH <= event.y <= 31 * genH):
                data.saved = True
                data.prog.loopThrough(data)
                data.leader.updateLeaderboard(data)
        # Home button
        if (30 * genW - 175 <= event.x <= 30 * genW - 25) and \
            (32 * genH <= event.y <= 34 * genH):
                # Go back to home screen
                data.home = True
                data.play = False
                data.wrong = False
                if not data.saved:
                    data.prog.loopThrough(data)
                    data.leader.updateLeaderboard(data)
                resetGame(data)
    # Learn page
    elif data.learn:
        genW = data.width / 4
        genH = data.height / 40
        # English tab that can be clicked to be visible or not visible
        if (2 * genW - 450) <= event.x <= (2 * genW + 450) \
                and (20 * genH - 35) <= event.y <= (20 * genH - 5):
                if data.showEnglish: 
                    data.showEnglish = False
                else: 
                    data.showEnglish = True
        # Pronounciation tab that can be clicked to be visible or not visible
        if (2 * genW - 450) <= event.x <= (2 * genW + 450) \
                and (20 * genH + 85) <= event.y <= (20 * genH + 100):
                if data.showPronounciation: 
                    data.showPronounciation = False
                else: 
                    data.showPronounciation = True
        genW = data.width / 40
        genH = data.height / 40
        if (30 * genW - 175 <= event.x <= 30 * genW - 25) and \
            (32 * genH <= event.y <= 34 * genH):
                # Go back to home screen
                data.home = True
                data.learn = False
                data.showEnglish = False
                data.showPronounciation = False
    # Progress
    elif data.progress:
        genW = data.width / 40
        genH = data.height / 40
        if (30 * genW - 175 <= event.x <= 30 * genW - 25) and \
            (32 * genH <= event.y <= 34 * genH):
                # Go back to home screen
                data.home = True
                data.progress = False
    # Leaderboard
    elif data.leaderboard:
        genW = data.width / 40
        genH = data.height / 40
        if (30 * genW - 175 <= event.x <= 30 * genW - 25) and \
            (32 * genH <= event.y <= 34 * genH):
                # Go back to home screen
                data.home = True
                data.leaderboard = False
    # About
    elif data.about:
        genW = data.width / 40
        genH = data.height / 40
        if (30 * genW - 175 <= event.x <= 30 * genW - 25) and \
            (32 * genH <= event.y <= 34 * genH):
                # Go back to home screen
                data.home = True
                data.about = False
    
def keyPressed(event, data):
    
    # Play: keys control player movement
    if data.play:
        if event.keysym == "Up":
            data.player.move("Up", data)
        if event.keysym == "Right":
            data.player.move("Right", data)
        if event.keysym == "Left":
            data.player.move("Left", data)
        if event.keysym == "Down":
            data.player.move("Down", data)
    # Learn: space bar moves to the next word to study
    elif data.learn:
        if (event.keysym == "space"): 
            data.next = True
            data.showEnglish = False
            data.showPronounciation = False

def timerFired(data):
    # Home/Language: moving words aesthetic
    if data.home:
        data.word.move(data)
        data.enemy.move(data)
    # Play: increment game timer, check collisions, move words and enemies
    elif data.play:
        data.timer += 1
        data.word.collide(data)
        data.enemy.collide(data)
        data.word.move(data)
        data.enemy.move(data)
    # Learn: gets next word if space bar was pressed
    elif data.learn:
        if (data.next): 
            (data.newWord, data.oldWord, data.newSent, data.pronounciation, data.english) =\
                data.word.getVocabWord(data)
            data.next = False

def redrawAll(canvas, data):
    # Black background
    canvas.create_rectangle(0, 0, data.width, data.height, 
                            fill = "black")

    # Top right welcome player text
    canvas.create_text(data.width - 250, data.height * 2 / 20, 
                        text = "Hi %s!" % (data.name), 
                        fill = "white", font="Calibri 20 bold")
    
    # Language page
    if data.language:
        drawLanguagePage(canvas, data)    
    # Home page
    elif data.home:
        drawHomePage(canvas, data)
    # Play page
    elif data.play:
        drawPlayPage(canvas, data)
    # Learn page
    elif data.learn:
        drawLearnPage(canvas, data)
    # Progress page
    elif data.progress:
        drawProgressPage(canvas, data)
    # Leaderboard page
    elif data.leaderboard:
        drawLeaderboardPage(canvas, data)
    # About page
    elif data.about:
        drawAboutPage(canvas, data)
    
    # Can run same time as home    
    if data.custom:
        getCustom(data)
        data.custom = False

def getCustom(data):
    
    # Based off of tutorial on widgets 
    # http://www.tkdocs.com/tutorial/text.html
    
    root1 = Tk()

    # Get input from text box and save in variable
    def getSentence():
        english=textBox.get("1.0","end-1c")
        if data.lang == "Chinese":
            data.translated = str(data.translator.translate(english, dest = "zh-CN"))
        else:
            data.translated = str(data.translator.translate(english, dest = "ko"))
        text = re.search(r'\b(text)\b', data.translated)
        pro = re.search(r'\b(pronunciation)\b', data.translated)
        textStart = text.start() + 5
        textEnd = pro.start() - 2
        proStart = pro.start() + 14
        proEnd = len(data.translated) - 1
        newLang = data.translated[textStart:textEnd]
        pronounciation = data.translated[proStart:proEnd]
        data.customList.append((None, None, newLang, pronounciation, english))
        data.customEnglishList.append(english)
        data.defaultAndCustomList.append((None, None, newLang, pronounciation, english))
        # Close window after text is obtained
        root1.destroy()

    textBox=Text(root1, height=1, width=75, 
                    highlightbackground = "black", borderwidth=2)
    textBox.pack()
    button = Button(root1, bg = 'black', 
                    text = 'Add this sentence to my practice bank', \
                    command=lambda: getSentence())
    button.pack()

def updateCustomList(data):
    # Loops through all customized sentences in list
    for sentence in data.customEnglishList:
        if data.lang == "Chinese":
            data.translated = str(data.translator.translate(sentence, dest = "zh-CN"))
        else:
            data.translated = str(data.translator.translate(sentence, dest = "ko"))
        # Locate text and pronounciation tags in the string
        text = re.search(r'\b(text)\b', data.translated)
        pro = re.search(r'\b(pronunciation)\b', data.translated)
        textStart = text.start() + 5
        textEnd = pro.start() - 2
        proStart = pro.start() + 14
        proEnd = len(data.translated) - 1
        # Translation in the other language
        newLang = data.translated[textStart:textEnd]
        # Pronounciation
        pronounciation = data.translated[proStart:proEnd]
        data.customList.append((None, None, newLang, pronounciation, sentence))
        data.defaultAndCustomList.append((None, None, newLang, pronounciation, sentence))
    
def drawLanguagePage(canvas, data):
        genWL = data.width * 3 / 5 - 75
        genWR = data.width * 4 / 5 - 75
        txtW = data.width * 7 / 10 - 75
        genH = data.height / 30
        # CatChars Title
        canvas.create_text(data.width / 2 - 325, data.height / 2 - 25, 
                            text = "CatChars", anchor = "center",
                            fill = "springgreen", font="Calibri 90 bold")
        # Instruction to pick language
        canvas.create_text(txtW, 9 * genH, 
                            text = "Pick a language:", fill = "white", 
                            font="Calibri 30 bold")
        # Chinese option
        canvas.create_rectangle(genWL, 12 * genH, 
                                genWR, 14 * genH, 
                                fill = "white")
        canvas.create_text(txtW, 13 * genH, 
                            text = "Chinese", fill = "black", 
                            font="Calibri 20 bold")
        # Korean option
        canvas.create_rectangle(genWL, 15 * genH, 
                                genWR, 17 * genH, 
                                fill = "white")
        canvas.create_text(txtW, 16 * genH, 
                            text = "Korean", fill = "black", 
                            font="Calibri 20 bold")   

def drawHomePage(canvas, data):
        data.word.draw(canvas, data)
        data.enemy.draw(canvas, data)
        genWL = data.width * 3 / 5 - 75
        genWR = data.width * 4 / 5 - 75
        txtW = data.width * 7 / 10 - 75
        genH = data.height / 30
        # CatChars Title
        canvas.create_text(txtW, 6 * genH, 
                            text = "CatChars", fill = "springgreen", 
                            font="Calibri 75 bold")
        # Play button
        canvas.create_rectangle(genWL, 9 * genH, genWR, 11 * genH, 
                                fill = "white")
        canvas.create_text(txtW, 10 * genH, 
                            text = "PLAY", fill = "black", 
                            font="Calibri 20 bold")
        # Learn button
        canvas.create_rectangle(genWL, 12 * genH, genWR, 14 * genH, 
                                fill = "white") 
        canvas.create_text(txtW, 13 * genH, 
                            text = "LEARN", fill = "black", 
                            font="Calibri 20 bold")
        # Custom button
        canvas.create_rectangle(genWL, 15 * genH, genWR, 17 * genH, 
                                fill = "white")
        canvas.create_text(txtW, 16 * genH, 
                            text = "CUSTOMIZE", fill = "black", 
                            font="Calibri 20 bold")
        # Progress button
        canvas.create_rectangle(genWL, 18 * genH, genWR, 20 * genH, 
                                fill = "white")
        canvas.create_text(txtW, 19 * genH, 
                            text = "PROGRESS", fill = "black", 
                            font="Calibri 20 bold")
        # Leaderboards button
        canvas.create_rectangle(genWL, 21 * genH, genWR, 23 * genH, 
                                fill = "white")
        canvas.create_text(txtW, 22 * genH, 
                            text = "LEADERBOARDS", fill = "black", 
                            font="Calibri 20 bold")
        # About button
        canvas.create_rectangle(genWL, 24 * genH, genWR, 26 * genH, 
                                fill = "white")
        canvas.create_text(txtW, 25 * genH, 
                            text = "ABOUT", fill = "black", 
                            font="Calibri 20 bold")

def drawPlayPage(canvas, data):
        data.board.draw(canvas, data, data.width // 2, data.height)
        data.walls.draw(canvas, data, data.width // 2, data.height)
        data.word.draw(canvas, data)
        data.enemy.draw(canvas, data)
        data.player.draw(canvas, data)
        genW = data.width * 3 / 4
        genH = data.height / 40
        # Score Display
        canvas.create_text(data.width / 2 + 25, data.height * 2 / 20, 
                            anchor = "center", 
                            text = "XP: " + str(data.currXP), fill = "cyan2", 
                            font="Calibri 20 bold")
        # Either "Check answer" or "Next"
        canvas.create_rectangle(genW - 175, 23 * genH, genW - 25, 25 * genH,
                                fill = "white")
        canvas.create_text(genW - 100, 24 * genH,
                            text = data.boxText, fill = "black", 
                            font="Calibri 15 bold")
        # Backspace button
        canvas.create_rectangle(genW - 175, 26 * genH, genW - 25, 28 * genH,
                                fill = "white")
        canvas.create_text(genW - 100, 27 * genH,
                            text = "Backspace", fill = "black", 
                            font="Calibri 15 bold")
        # Save button
        canvas.create_rectangle(genW - 175, 29 * genH, genW - 25, 31 * genH,
                                fill = "white")
        canvas.create_text(genW - 100, 30 * genH,
                            text = "Save Progress", fill = "black", 
                            font="Calibri 15 bold")
        # Shows player created answer
        if data.wrong:
            canvas.create_text(genW - 100, 12 * genH, 
                            anchor = "center", text = "Your string:", 
                            fill = data.stringColor, font="Calibri 25 bold")
            canvas.create_text(genW - 100, 14 * genH, 
                            anchor = "center", text = "".join(data.allPicked), 
                            fill = data.stringColor, font="Calibri 25 bold")
        else:
            canvas.create_text(genW - 100, 12 * genH, 
                            anchor = "center", text = "Your string:", 
                            fill = data.stringColor, font="Calibri 25 bold")
            canvas.create_text(genW - 100, 14 * genH, 
                            anchor = "center", text = "".join(data.allPicked), 
                            fill = data.stringColor, font="Calibri 25 bold")
        drawHomeButton(canvas, data)

def drawLearnPage(canvas, data):
        halfW = data.width // 2
        genWL = data.width // 2 - 450
        genWR = data.width // 2 + 450
        halfH = data.height // 2
        # Learn label
        canvas.create_text(halfW, data.height * 2 / 10, 
                            anchor = "center", text = "LEARN", 
                            fill = "white", font="Calibri 60 bold underline")
        # Instruction to press space bar for next sentence
        canvas.create_text(halfW, data.height * 11 / 40, 
                            anchor = "center",
                            text = "Click the space bar for next sentence", 
                            fill = "white", font="Calibri 20 bold italic")
        if data.showEnglish:
            # English
            canvas.create_rectangle(genWL, halfH - 125, genWR, halfH - 35, 
                                fill = "lavenderblush", outline = "lavenderblush")
            canvas.create_text(halfW, halfH - 80, 
                                anchor = "center", text = data.english, 
                                fill = "black", font="Calibri 40")
        # Divider
        canvas.create_rectangle(genWL, halfH - 35, genWR, halfH - 5, 
                            fill = "blanchedalmond", outline = "blanchedalmond")
        canvas.create_text(halfW, halfH - 20, 
                            anchor = "center", text = "Click for English", 
                            fill = "black", font="Calibri 15")
        # newLang
        canvas.create_rectangle(genWL, halfH - 5, genWR, halfH + 85, 
                        fill = "lemonchiffon", outline = "lemonchiffon")
        canvas.create_text(halfW, halfH + 40, 
                            anchor = "center", text = data.newSent, 
                            fill = "black", font="Calibri 40")
        # Divider
        canvas.create_rectangle(genWL, halfH + 85, genWR, halfH + 115, 
                            fill = "aliceblue", outline = "aliceblue")
        canvas.create_text(halfW, halfH + 100, 
                            anchor = "center", text = "Click for pronounciation", 
                            fill = "black", font="Calibri 15")
        # Pronounciation
        if data.showPronounciation:
            canvas.create_rectangle(genWL, halfH + 115, genWR, halfH + 205, 
                            fill = "lavender", outline = "lavender")
            canvas.create_text(halfW, halfH + 160, 
                                anchor = "center", text = data.pronounciation, 
                                fill = "black", font="Calibri 40")
        drawHomeButton(canvas, data)

def drawProgressPage(canvas, data):
        rList = data.prog.getRightList()
        rCount = data.prog.getRightCount()
        wList = data.prog.getWrongList()
        aList = data.prog.getAllList()
        aCount = data.prog.getAllCount()
        together = data.prog.getTogether()
        rwDict = dict()
        txt = ""
        try:
            percentage = (float(rCount)/float(aCount)) * 100.0
            percentage = round(percentage, 2)
            txt = str(percentage) + "% Overall"
        except:
            txt = "No history!"
        canvas.create_text(data.width * 3 / 4 - 175, data.height * 20 / 40 - 100,
                            text = txt, anchor = "w",
                            fill = "white", font="Calibri 50 bold")
        canvas.create_text(data.width * 3 / 4 - 175, data.height * 20 / 40,
                            text = str(rCount) + "/" + str(aCount) + " Correct", 
                            anchor = "w", fill = "white", font="Calibri 50 bold")
        # Total XP Display
        canvas.create_text(data.width / 2 + 250, data.height * 2 / 20, 
                            anchor = "center", 
                            text = "Total XP: " + str(data.allXP), fill = "cyan2", 
                            font="Calibri 20 bold")
        # Y axis line
        canvas.create_rectangle(data.offset + data.border, 
                                data.offset + data.border, 
                                data.offset + 2 * data.border, 
                                data.border + data.height * 3 / 4, 
                                fill = "white")
        # X axis line
        canvas.create_rectangle(data.offset + data.border, 
                                data.height * 3 / 4, 
                                data.width * 3 / 5, 
                                data.border + data.height * 3 / 4, 
                                fill = "white")
        # Space out points on the graph depending on number of x's
        xAxis = data.width * 3 / 5 - (data.offset + data.border)
        r = len(rList)
        w = len(wList)
        try:
            space = xAxis / len(together)
        except:
            # Together is empty so there is no data to graph
            space = 0
        i = 0
        thick = space / 2
        # Loop through all values in together
        for key in together:
            try:
                english = key
                r = data.word.findIndex(data, english)
                if data.lang == "Chinese":
                    newLang = chineseVerbs[r][0]
                else:
                    newLang = koreanVerbs[r][0]
                (correct, wrong) = together[key]
                percentage = 0
                # Calculate percentage of accuracy
                try:
                    percentage = (float(correct)/float(correct + wrong)) * 100.0
                    percentage = round(percentage, 2)
                except:
                    # No data so there is no percentage
                    print("NO DATA ON THIS")
                # Draw red bar for wrong percentage
                canvas.create_rectangle(data.offset + 3 * data.border + i * space, 
                                data.offset + data.border, 
                                data.offset + 4 * data.border + i * space + thick, 
                                data.border + data.height * 3 / 4 - data.border,
                                fill = "tomato", outline = "tomato")
                dist = (data.border + data.height * 3 / 4 - data.border) \
                        - (data.offset + data.border)
                # Draw green bar for correct percentage
                canvas.create_rectangle(data.offset + 3 * data.border + i * space, 
                                data.offset + data.border + \
                                (1 - (percentage / 100)) * dist, 
                                data.offset + 4 * data.border + i * space + thick, 
                                data.border + data.height * 3 / 4 - data.border,
                                fill = "springgreen", outline = "springgreen")
                midX = (data.offset + 3 * data.border + i * space + data.offset + \
                        4 * data.border + i * space + thick) / 2
                midY = (data.offset + data.border + data.border + \
                        data.height * 3 / 4 - data.border) / 2
                size = 10 + int(45 / len(together))
                # Draw word in other language
                canvas.create_text(midX, 
                                data.height * 3 / 4 + 50,
                                text = newLang, 
                                fill = "white", font="Calibri %s bold" % (size))
                # Draw word in English
                canvas.create_text(midX, 
                                data.height * 3 / 4 + 100,
                                text = english, 
                                fill = "white", font="Calibri %s bold" % (size))
                # Draw percentage on bar
                canvas.create_text(midX, midY,
                                text = str(percentage) + "%", 
                                fill = "white", font="Calibri %s bold" % (size))
                i += 1
            except:
                print("CAN'T SHOW THIS WORD'S PROGRESS")
        genW = data.width * 3 / 4
        genH = data.height / 40
        # Home button
        canvas.create_rectangle(genW - 175, 32 * genH,
                                genW - 25, 34 * genH,
                                fill = "white")
        canvas.create_text(genW - 100, 33 * genH,
                            text = "Back to Home", fill = "black", 
                            font="Calibri 15 bold")

def drawLeaderboardPage(canvas, data):
        canvas.create_text(data.width / 2, data.height * 2 / 10, 
                            anchor = "center", text = "LEADERBOARD", 
                            fill = "white", font="Calibri 60 bold underline")
        data.leader.updateLeaderboard(data)
        data.leader.draw(data, canvas)
        drawHomeButton(canvas, data)

def drawAboutPage(canvas, data):
        canvas.create_text(data.width / 2, data.height * 2 / 10, 
                            anchor = "center", text = "ABOUT", 
                            fill = "white", font="Calibri 60 bold underline")
        # Play details
        canvas.create_rectangle(data.width / 2 - 200, data.height / 2 - 30,
                                data.width / 2 + 200, data.height / 2 + 95, 
                                fill = None, outline = "springgreen", width = 5)
        canvas.create_text(data.width / 2, data.height / 2, 
                            anchor = "center", text = "PLAY", 
                            fill = "springgreen", font="Calibri 20 bold")
        canvas.create_text(data.width / 2, data.height / 2 + 40, 
                            anchor = "center", 
                            text = "Test your knowledge!\nPress arrow keys to move.\nCheck the string you created with the correct answer.", 
                            fill = "white", font="Calibri 12 bold")
        # Learn details
        canvas.create_rectangle(data.width / 2 - 600, data.height / 2 - 155,
                                data.width / 2 - 200, data.height / 2 - 30, 
                                fill = None, outline = "springgreen", width = 5)
        canvas.create_text(data.width / 2 - 400, data.height / 2 - 125, 
                            anchor = "center", text = "LEARN", 
                            fill = "springgreen", font="Calibri 20 bold")
        canvas.create_text(data.width / 2 - 400, data.height / 2 - 85, 
                            anchor = "center", 
                            text = "Practice your knowledge through flashcards!\nLearn the English, characters, and pronounciation.", 
                            fill = "white", font="Calibri 12 bold")
        # Customize details
        canvas.create_rectangle(data.width / 2 - 600, data.height / 2 + 95,
                                data.width / 2 - 200, data.height / 2 + 195, 
                                fill = None, outline = "springgreen", width = 5)
        canvas.create_text(data.width / 2 - 400, data.height / 2 + 125, 
                            anchor = "center", text = "CUSTOMIZE", 
                            fill = "springgreen", font="Calibri 20 bold")
        canvas.create_text(data.width / 2 - 400, data.height / 2 + 165, 
                            anchor = "center", 
                            text = "Create your own practice!\nInput the sentences you want to practice.", 
                            fill = "white", font="Calibri 12 bold")
        # Progress details
        canvas.create_rectangle(data.width / 2 + 200, data.height / 2 - 155,
                                data.width / 2 + 600, data.height / 2 - 30, 
                                fill = None, outline = "springgreen", width = 5)
        canvas.create_text(data.width / 2 + 400, data.height / 2 - 125, 
                            anchor = "center", text = "PROGRESS", 
                            fill = "springgreen", font="Calibri 20 bold")
        canvas.create_text(data.width / 2 + 400, data.height / 2 - 85, 
                            anchor = "center", 
                            text = "Check out your progress!\nWe keep track of how much you understand.", 
                            fill = "white", font="Calibri 12 bold")
        # Leaderboard details
        canvas.create_rectangle(data.width / 2 + 200, data.height / 2 + 95,
                                data.width / 2 + 600, data.height / 2 + 195, 
                                fill = None, outline = "springgreen", width = 5)
        canvas.create_text(data.width / 2 + 400, data.height / 2 + 125, 
                            anchor = "center", text = "LEADERBOARDS", 
                            fill = "springgreen", font="Calibri 20 bold")
        canvas.create_text(data.width / 2 + 400, data.height / 2 + 165, 
                            anchor = "center", 
                            text = "See how you compare to other players!\nThe top ten players are shown as well as their cumulative XP.", 
                            fill = "white", font="Calibri 12 bold")
        drawHomeButton(canvas, data)

def drawHomeButton(canvas, data):
    genW = data.width * 3 / 4
    genH = data.height / 40
    # Home button
    canvas.create_rectangle(genW - 175, 32 * genH,
                            genW - 25, 34 * genH,
                            fill = "white")
    canvas.create_text(genW - 100, 33 * genH,
                        text = "Back to Home", fill = "black", 
                        font="Calibri 15 bold")

def resetGame(data):
    # Start player from the top left of board again    
    data.player = Player(data)
    # Create new board
    data.walls = Wall()
    data.walls.createWalls(data)
    data.all = data.walls.getWalls(data)
    data.allW = list()
    # Choose new word to test on
    data.word = Word(data.lang)
    data.word.setLanguage(data)
    data.word.createWords(data)
    # Spawn new enemies
    data.enemy = Enemy(random.randint(2, 4), data.lang)
    data.enemy.createEnemies(data)
    # Reset variables for a new round
    data.allPicked = list()
    data.boxText = "Check answer"
    data.wrong = False
    data.correct = False
    data.saved = False
    data.stringColor = "white"

# Read functions based off of 15112 notes

# READ USER FILE
def read(data):
    # TRY TO READ FROM FILE
    try:
        with open('data//%s%s' % (data.name, data.lang)) as f:
            content = f.readlines()
        # Remove out whitespace characters
        content = [x.strip() for x in content]
        # Initialize data objects with player history
        for index in range(len(content)):
            if index == 0:
                data.cDict = ast.literal_eval(content[0])
            elif index == 1:
                data.wDict = ast.literal_eval(content[1])
            elif index == 2:
                data.aDict = ast.literal_eval(content[2])
            elif index == 3:
                data.customEnglishList = ast.literal_eval(content[3])
            elif index == 4:
                data.allXP = ast.literal_eval(content[4])
    except:
        print("READING FROM USER FILE FAILED")
    updateCustomList(data)
    data.prog.loopThrough(data)
    
# READ LEADERBOARD
def readLeaderboard(data):
    # TRY TO READ FROM FILE
    try:
        with open('data//leaderboard%s' % (data.lang)) as f:
            content = f.readlines()
        # Remove out whitespace characters
        content = [x.strip() for x in content]
        # Initialize data objects with leaderboard history
        data.lDict = ast.literal_eval(content[0])
        data.leader.sortLeaderboard(data)
    except:
        print("READING FROM LEADERBOARD FAILED")
    
####################################
# Run-function based off of 15112 notes 
####################################

def run(name = "", width=1500, height=750):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 10 # milliseconds
    # NAME VAR INIT
    data.name = name
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    print("Hi!")
    root.mainloop()  # blocks until window is closed
    
    # Write functions based off of 15112 notes
    
    # WRITE TO USER FILE BEFORE EXITING 
    def write(data):
        try: 
            # WRITE TO FILE
            f = open('data//%s%s' % (name, data.lang), 'w')
            f.write(str(data.cDict) + "\n" + \
                    str(data.wDict) + "\n" + \
                    str(data.aDict) + "\n" + \
                    str(data.customEnglishList) + "\n" + \
                    str(data.currXP + data.allXP))
            f.close()
        except:
            print("WRITING TO USER FILE FAILED")
    write(data)
    
    # WRITE TO LEADERBOARD FILE BEFORE EXITING
    def writeLeaderboard(data):
        try: 
            # WRITE TO FILE
            f = open('data//leaderboard%s' % (data.lang), 'w')
            f.write(str(data.lDict))
            f.close()
        except:
            print("WRITING TO LEADERBOARD FAILED")
    writeLeaderboard(data)
    print("Bye!")