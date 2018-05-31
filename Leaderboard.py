""" 
Leaderboard
Displays top ten players' names and their scores.
"""
import operator

class Leaderboard(object):
    
    def __init__(self):
        pass
    
    def draw(self, data, canvas):
        if len(data.lDict) == 0:
            canvas.create_text(data.width / 2, data.height / 2, 
                                anchor = "center", text = "No history!",
                                fill = "white", font="Calibri 25 bold")
        else:
            canvas.create_text(data.width * 1 / 4 + 100, data.height * 6 / 20, 
                            anchor = "w", text = "Player", 
                            fill = "white", font="Calibri 25 bold underline")
            canvas.create_text(data.width * 1 / 4 + 500, data.height * 6 / 20, 
                            anchor = "w", text = "Total XP", 
                            fill = "white", font="Calibri 25 bold underline")
            for i in range(1, len(data.lDict) + 1):
                canvas.create_text(data.width * 1 / 4, data.height * (i + 6) / 20, 
                                anchor = "center", text = str(i) + ".", 
                                fill = "white", font="Calibri 25 bold")
            i = 1
            for (key, val) in self.sortedByScoreReverse:
                canvas.create_text(data.width * 1 / 4 + 100, data.height * (i + 6)  / 20, 
                                anchor = "w", text = key, 
                                fill = "white", font="Calibri 25 bold")
                canvas.create_text(data.width * 1 / 4 + 500, data.height * (i + 6)  / 20, 
                                anchor = "w", text = str(val), 
                                fill = "white", font="Calibri 25 bold")
                i += 1
    
    # Put the player on the leaderboard if they're top ten
    def updateLeaderboard(self, data):
        keyList = list(data.lDict.keys())
        valList = list(data.lDict.values())
        if len(data.lDict) < 10:
            data.lDict[data.name] = data.allXP
        elif data.name in keyList:
            data.lDict[data.name] = data.allXP
        else:
            Leaderboard.checkIfLeader(self, data)
        Leaderboard.sortLeaderboard(self, data)
    
    # Check if the player should be on the leaderboard 
    def checkIfLeader(self, data):
        (lowKey, lowVal) = self.sortedByScore[0]
        if lowVal < data.allXP:
            del data.lDict[lowKey]
            data.lDict[data.name] = data.allXP

    # Makes a list of the top ten in numerical order
    def sortLeaderboard(self, data):
        try:
            self.sortedByScore = sorted(data.lDict.items(), \
                                    key=operator.itemgetter(1))
            self.sortedByScoreReverse = self.sortedByScore[::-1]
        except:
            print("NOTHING TO SORT")