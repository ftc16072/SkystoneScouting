from enum import IntEnum
from matches import Matches, Match

class role(IntEnum):
    NONE = 0
    STACKING = 1
    FERRYING = 2
    BOTH = 3
    OTHER = 5

class Auto():
    def __init__(self, skystoneBonus, stonesDelivered, stonesPlaced, waffle, park, score):
        self.skystoneBonus = skystoneBonus
        self.stonesDelivered = stonesDelivered
        self.stonesPlaced = stonesPlaced
        self.waffle = waffle
        self.parked = park
        self.score = score

class MatchSim():
    def __init__(self, red1, red2, blue1, blue2, dbConnection):
        self.dbConnection = dbConnection
        self.matches = Matches()
        self.red1Id = red1
        self.red2Id = red2
        self.blue1Id = blue1
        self.blue2Id = blue2
        self.red1 = self.matches.getTeamInfo(self.dbConnection, red1)
        self.red2 = self.matches.getTeamInfo(self.dbConnection,red2)
        self.blue1 = self.matches.getTeamInfo(self.dbConnection,blue1)
        self.blue2 = self.matches.getTeamInfo(self.dbConnection,blue2)

    def getBestAuto(self, teamid):
        teamMatches = self.matches.getSelectedMatches(self.dbConnection, f"teamid = {teamid}", "matchNum")
        bestAutoScore = 0
        bestAuto = Auto(0,0,0,False, False, 0)
        for match in teamMatches:
            if match.autoScore >= bestAutoScore:
                bestAutoScore = match.autoScore
                bestAuto = Auto(match.skystoneBonus, match.stonesDelivered, match.stonesPlaced, match.waffle, match.autoPark, match.autoScore)
        return bestAuto

    def getAutoRoles(self, team1Id, team1Dict, team2Id, team2Dict):
        if team1Dict["avgAuto"] >= team2Dict["avgAuto"]:
            team1Auto = self.getBestAuto(team1Id)
            if team2Dict["autoParkedPercent"] >= 0:
                team2Auto = Auto(0,0,0,False,True, 5)
            else:
                team2Auto= Auto(0,0,0, False, False, 0)
        else:
            team2Auto = self.getBestAuto(team2Id)
            if team1Dict["autoParkedPercent"] >= 0:
                team1Auto = Auto(0,0,0,False,True,5)
            else:
                team1Auto = Auto(0,0,0,False, False, 0)
        return [team1Auto, team2Auto]

    def getAlianceAutoRoles(self):
        redAllianceAutoRoles = self.getAutoRoles(self.red1Id, self.red1, self.red2Id, self.red2)
        blueAllianceAutoRoles = self.getAutoRoles(self.blue1Id, self.blue1, self.blue2Id, self.blue2)
        return {
            "Red":redAllianceAutoRoles,
            "Blue":blueAllianceAutoRoles
        }
       
    
    def getTelopRoles(self, team1id, team1Dict, team2Id, team2Dict):
        team1Role = 0
        team2Role = 0
        blocksplaced = 0
        height = 0
        blocksDeliverd = 0
        if team1Dict["avgBlocksDeliverdFerryMatches"] >= team2Dict["avgPlacedStackingMatches"]:
            team1Role = 2
            team2Role = 1
            blocksplaced = team2Dict["avgPlacedStackingMatches"]
            blocksDeliverd = team1Dict["avgBlocksDeliverdFerryMatches"]
            height = team2Dict["avgHeightStackingMatches"]
        elif team2Dict["avgBlocksDeliverdFerryMatches"] >= team1Dict["avgPlacedStackingMatches"]:
            team1Role = 1
            team2Role = 2
            blocksplaced = team1Dict["avgPlacedStackingMatches"]
            blocksDeliverd = team2Dict["avgBlocksDeliverdFerryMatches"]
            height = team1Dict["avgHeightStackingMatches"]
        else:
            if team1Dict["avgHeight"] >= team2Dict["avgHeight"] and team1Dict["avgHeight"] > 0:
                team1Role += 1
            elif team2Dict["avgHeight"] > 0:
                team2Role += 1                
            if team1Dict["avgTeleBlocks"] >= team2Dict["avgTeleBlocks"] and team1Dict["avgTeleBlocks"] > 0:
                team1Role += 2                
            elif team2Dict["avgTeleBlocks"]:
                team2Role += 2
            if team1Role == 1 and team2Dict["avgBlocksDeliverdFerryMatches"] < team1Dict["avgPlacedStackingMatches"]:
                team1Role += 2
            elif team2Role == 1 and team1Dict["avgBlocksDeliverdFerryMatches"] < team2Dict["avgPlacedStackingMatches"]:
                team2Role += 2
                                   
        if blocksplaced == 0 and team1Role == 3:
            blocksplaced = team1Dict["avgBlocksPlaceBoth"]
            height = team1Dict["avgHeightBoth"]
            blocksDeliverd = team1Dict["avgBlocksDelBoth"] + team2Dict["avgTeleBlocks"]
        if blocksplaced == 0 and team2Role == 3:
            blocksplaced = team2Dict["avgBlocksPlaceBoth"]
            height = team2Dict["avgHeightBoth"]
            blocksDeliverd = team2Dict["avgBlocksDelBoth"] + team1Dict["avgTeleBlocks"]
        
        team1Role = role(team1Role)
        team2Role = role(team2Role)
        return [team1Role, team2Role, blocksDeliverd, blocksplaced, height]
        




    def getAlianceTelopRole(self):
        return {
            "Red": self.getTelopRoles(self.red1Id, self.red1, self.red2Id, self.red2),
            "Blue": self.getTelopRoles(self.blue1Id, self.blue1, self.blue2Id, self.blue2)

        }

    
    



            
            



    
 