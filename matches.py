import sqlite3
import os
from teams import Teams, Team

def getTeamRole(match):
    ferried = match.stonesDeliveredTele
    stacking = match.stonesPlaced
    role = ""
    if (ferried == 0) and (stacking > 0):
        role = "Stacking"
    elif (ferried > 0) and (stacking == 0):
        role = "Ferrying"
    elif (ferried == 0) and (stacking == 0):
        role = "None"
    elif abs(ferried - stacking) <= 1:
        role = "Both"
    else:
        role = f"inconclusive stacking:{stacking} ferried:{ferried}"
    return role
    


class Match():
    def __init__(self, teamNum, matchNum, alliance, skystoneBonus, stonesDelivered, autoStonesPlaced, waffle, autoPark, stonesDeliveredTele, stonesPlaced, height, repositioning, capstone, parking, notes, penalties, broken, matchId, submitedByNum, knocked):
        self.teamNum = teamNum
        self.matchNum = matchNum
        self.alliance = alliance
        self.skystoneBonus = skystoneBonus
        self.stonesDelivered = stonesDelivered
        self.autoStonesPlaced = autoStonesPlaced
        self.waffle = True if (waffle=="true") else False
        self.autoPark = True if (autoPark=="true") else False 
        self.stonesDeliveredTele = stonesDeliveredTele
        self.stonesPlaced = stonesPlaced
        self.height = height
        self.repositioning = True if (repositioning=="true") else False
        self.capstone = capstone
        self.parking = True if (parking=="true") else False
        self.notes = notes
        self.penalties = True if (penalties=="true") else False
        self.broken = True if (broken=="true") else False
        self.matchId = matchId
        self.submitedByNum = submitedByNum
        self.autoScore = (8 * skystoneBonus) + (2 * stonesDelivered) + (4 * autoStonesPlaced) + (10 if self.waffle else 0) + (5 if self.autoPark else 0)
        self.teleOpScore = (stonesDeliveredTele) + (stonesPlaced) + (2 * height)
        self.endGameScore = (10 if self.repositioning else 0) + ((capstone) + 5 if capstone != -1 else 0) + (5 if self.parking else 0)
        self.score = self.autoScore + self.teleOpScore + self.endGameScore
        self.blnAuto = True if self.autoScore > 0 else False
        self.role = getTeamRole(self)
        self.knocked = True if knocked == "true" else False

class Matches():
    def __init__(self):
        self.teams = Teams()

    def createTable(self, dbConnection):
        dbConnection.execute("""
        CREATE TABLE Matches(
            id INTEGER PRIMARY KEY,
            teamid INTEGER NOT NULL,
            matchNum INTEGER NOT NULL,
            alliance BOOLEAN NOT NULL,
            skystoneBonus INTEGER NOT NULL,
            stonesDelivered INTEGER NOT NULL,
            autoStonesPlaced INTEGER NOT NULL, 
            waffle BOOLEAN NOT NULL, 
            autoPark BOOLEAN NOT NULL, 
            stonesDeliveredTele INTEGER NOT NULL, 
            stonesPlaced INTEGER NOT NULL, 
            height INTEGER NOT NULL, 
            repositioning BOOLEAN NOT NULL, 
            capstone INTEGER NOT NULL, 
            parking BOOLEAN NOT NULL,
            knocked BOOLEAN NOT NULL, 
            notes TEXT, 
            penalties BOOLEAN NOT NULL, 
            broken BOOLEAN NOT NULL,
            submitedByNum INTEGER NOT NULL
        )""")
    
    def addMatch(self, dbConnection, teamid, matchNum, redAlliance, skystoneBonus, stonesDelivered, autoStonesPlaced, waffle, autoPark, stonesDeliveredTele, stonesPlaced, height, repositioning, capstone, parking, notes, knocked, penalties, broken, submitedByNum):
        dbConnection.execute("""
        INSERT INTO Matches (teamid, matchNum, alliance, skystoneBonus, stonesDelivered, autoStonesPlaced, waffle, autoPark, stonesDeliveredTele, stonesPlaced, height, repositioning, capstone, parking, notes, penalties, broken, submitedByNum, knocked) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """, (teamid, matchNum, redAlliance, skystoneBonus, stonesDelivered, autoStonesPlaced, waffle, autoPark, stonesDeliveredTele, stonesPlaced, height, repositioning, capstone, parking, notes, penalties, broken, submitedByNum, knocked))
    
    def getMatches(self, dbConnection, text, params=""):
        matchList = []
        if params:
            for row in dbConnection.execute(text, params):
                matchList.append(Match(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13], row[14], row[15], row[16], row[17], row[18], row[19]))
        else:
            for row in dbConnection.execute(text):
                matchList.append(Match(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13], row[14], row[15], row[16], row[17], row[18], row[19]))
        return matchList

    def getAllMatches(self, dbConnection):
        text = """
        SELECT Teams.number, matchNum, alliance, skystoneBonus, stonesDelivered, autoStonesPlaced, waffle,
        autoPark, stonesDeliveredTele, stonesPlaced, height, repositioning, capstone, parking, notes, penalties, broken, Matches.id, submitedByNum, knocked
        FROM Matches INNER JOIN Teams ON Matches.teamid = Teams.id ORDER BY Teams.number"""
        return self.getMatches(dbConnection, text)

    def getSelectedMatches(self, dbConnection, where, orderBy):
        matchList = []
        text = f"""
        SELECT Teams.number, matchNum, alliance, skystoneBonus,
        stonesDelivered, autoStonesPlaced, waffle, autoPark, stonesDeliveredTele, stonesPlaced, height, repositioning, capstone, parking, notes, penalties, broken, Matches.id, submitedByNum, knocked
        FROM Matches INNER JOIN Teams ON Matches.teamid = Teams.id WHERE {where} ORDER BY {orderBy}"""
        return self.getMatches(dbConnection, text)
    
    def isTeamBroken(self, dbConnection, teamid):
        broken = ""
        findBrokenText = f"SELECT broken FROM matches WHERE teamid={teamid} ORDER BY matchNum"
        for row in dbConnection.execute(findBrokenText):
            broken = row[0]
        return (True if broken == "true" else False) if (broken) else False

    def hasTeamBeenPenalized(self, dbConnection, teamid):
        penatlies = False
        findPenaltyText = f"SELECT penalties FROM matches WHERE teamid={teamid} ORDER BY matchNum"
        for row in dbConnection.execute(findPenaltyText):
            if row[0] == "true":
                penatlies = True
        return penatlies

    def getTeamInfo(self, dbConnection, teamid):
        infoDict = {
            "avgAuto":0,
            "avgTele":0,
            "avgEnd":0,
            "percentBroken":0,
            "matchScores":[],
            "avgTeleBlocks":0,
            "avgBlocksDeliverdFerryMatches":0,
            "avgHeight":0,
            "avgHeightStackingMatches":0,
            "avgPlaced":0,
            "avgPlacedStackingMatches":0,
            "wafflePercent":0,
            "avgSkystoneBonus":0,
            "avgStonesDelivered":0,
            "avgStonesPlaced":0,
            "autoParkedPercent":0,
            "parkedPercent":0,
            "repositioningPercent":0,
            "avgCapstone":0,
            "knockedPercent":0
        }
        autoTot = 0
        teleTot = 0
        endTot = 0
        brokenTot = 0
        totalMatches = 0
        TeleBlocks = 0
        height = 0
        placed = 0
        wafflePercent = 0
        skystoneBonus = 0
        stonesDelivered = 0
        stonesPlaced = 0
        autoParkedPercent = 0
        parkedPercent = 0
        repositioningPercent = 0
        capstone = 0
        knockedPercent = 0
        matchScores = []
        matchList = self.getSelectedMatches(dbConnection, f"teamid={teamid}", "matchNum")
        for match in matchList:
            totalMatches += 1
            autoTot += match.autoScore
            teleTot += match.teleOpScore
            endTot += match.endGameScore
            matchScores.append(match.autoScore + match.teleOpScore + match.endGameScore)
            brokenTot += 1 if match.broken else 0
            TeleBlocks += match.stonesDeliveredTele
            height += match.height
            placed += match.stonesPlaced
            wafflePercent += match.waffle
            skystoneBonus += match.skystoneBonus
            stonesDelivered += match.stonesDelivered
            stonesPlaced += match.autoStonesPlaced
            autoParkedPercent += match.autoPark
            parkedPercent += match.parking
            repositioningPercent += match.repositioning
            capstone += match.capstone
            knockedPercent += match.knocked
        if totalMatches > 0:
            infoDict["avgAuto"] = round(autoTot / totalMatches, 1)
            infoDict["avgTele"] = round(teleTot / totalMatches, 1)
            infoDict["avgEnd"] = round(endTot / totalMatches, 1)
            infoDict["percentBroken"] = round(brokenTot / totalMatches, 1)
            infoDict["matchScores"] = matchScores
            infoDict["avgTeleBlocks"] = round(TeleBlocks / totalMatches, 1)
            infoDict["avgHeight"] = round(height / totalMatches, 1)
            infoDict["avgPlaced"] = round(placed / totalMatches, 1)
            infoDict["wafflePercent"] = round(wafflePercent / totalMatches, 1)
            infoDict["avgSkystoneBonus"] = round(skystoneBonus / totalMatches, 1)
            infoDict["avgStonesDelivered"] = round(stonesDelivered / totalMatches, 1)
            infoDict["avgStonesPlaced"] = round(stonesPlaced / totalMatches, 1)
            infoDict["autoParkedPercent"] = round(autoParkedPercent / totalMatches, 1)
            infoDict["parkedPercent"] = round(parkedPercent / totalMatches, 1)
            infoDict["repositioningPercent"] = round(repositioningPercent / totalMatches, 1)
            infoDict["avgCapstone"] = round(capstone / totalMatches, 1)
            infoDict["knockedPercent"] = round(knockedPercent / totalMatches, 1)
        
        return infoDict




if __name__ == "__main__":
    DB_STRING = os.path.join(os.path.dirname(__file__), 'data/testdatabase.sqlite3')
    matches = Matches()
    with sqlite3.connect(DB_STRING) as connection:
        matches.createTable(connection)
        matches.addMatch(connection, 1,1,1,0,0,0,0,0,0,0,0,"",0,0)
        matchList = matches.getAllMatches(connection)
        for mathch in matchList:
            print(mathch)
