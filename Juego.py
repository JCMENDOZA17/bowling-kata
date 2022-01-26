class Juego():
    
    def __init__(self, pins):
        self.pins = pins

    def getScore(self):
        return self.totalScore()

    def scoreConverter(self, roll):
        
        if self.pins[roll] == 'X':
            return 10
        elif self.pins[roll] == '/':
            return 10 - self.scoreConverter(roll - 1)
        else:
            if self.pins[roll] == '-':
                return 0
            else:
                return int(self.pins[roll])

    def totalScore(self):
        
        strike = 10
        spare = 10

