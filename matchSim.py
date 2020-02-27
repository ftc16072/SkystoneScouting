from matches import Matches, Match

class role(IntEnum):
    STACKING = 1
    FERRYING = 2
    BOTH = 3
    NONE = 4
    OTHER = 5

class matchSim():
    def __init__(self, red1, red2, blue1, blue2):
        self.matches = Matches()
        self.teamDict = teamDict
        self.red1 = self.matches.getTeamInfo(red1)
        self.red2 = self.matches.getTeamInfo(red2)
        self.blue1 = self.matches.getTeamInfo(blue1)
        self.blue2 = self.matches.getTeamInfo(blue2)
    
    def getAutoRoles(self, team1, team2):
        pass
    
 