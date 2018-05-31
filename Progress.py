"""
Progress
Shows the player's history of percentages on what they got right and wrong.
"""

class Progress(object):
    
    def __init__(self):
        self.rightList = list()
        self.rightCount = 0
        self.wrongList = list()
        self.wrongCount = 0
        self.allList = list()
        self.allCount = 0
        self.together = dict()
    
    # Updates player data with most recent play history
    def loopThrough(self, data):
        self.allCount = 0
        self.rightCount = 0
        for key, val in data.aDict.items():
            self.allList.append(key)
            self.allCount += val
            self.together[key] = (0, 0)
        for key, val1 in data.cDict.items():
            self.rightList.append(key)
            self.rightCount += val1
            self.together[key] = (val1, 0)
        for key, val2 in data.wDict.items():
            self.wrongList.append(key)
            self.wrongCount += val2
            (val3, val4) = self.together[key]
            self.together[key] = (val3, val2)
        data.allXP += data.currXP
        data.currXP = 0
    
    # Returns list of characters gotten correct
    def getRightList(self):
        return self.rightList
    
    # Returns number of times player has scored something correct
    def getRightCount(self):
        return self.rightCount
    
    # Returns list of characters gotten wrong
    def getWrongList(self):
        return self.wrongList
    
    # Returns list of all characters played
    def getAllList(self):
        return self.allList
    
    # Returns number of times player has tried to score something
    def getAllCount(self):
        return self.allCount
    
    # Returns list that contains the tuple of correct and incorrect count
    def getTogether(self):
        return self.together