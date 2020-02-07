import sqlite3
import os

class Match():
    def __init__(self, teamNum, skystoneBonus, stonesDelivered, waffle, autoPark, stonesDeliveredTele, stonesPlaced, height, repositioning, capstone, parking, notes, penalties, broken, matchId):
        self.teamNum = teamNum
        self.skystoneBonus = skystoneBonus
        self.stonesDelivered = stonesDelivered
        self.waffle = waffle
        self.autoPark = autoPark
        self.stonesDeliveredTele = stonesDeliveredTele
        self.stonesPlaced = stonesPlaced
        self.height = height
        self.repositioning = repositioning
        self.capstone = capstone
        self.parking = parking
        self.notes = notes
        self.penalties = penalties
        self.broken = broken
        self.matchId = matchId

class Matches():
    def createTable(self, dbConnection):
        dbConnection.execute("""
        CREATE TABLE Matches(
            id INTEGER PRIMARY KEY,
            teamid INTEGER NOT NULL,
            skystoneBonus INTEGER NOT NULL,
            stonesDelivered INTEGER NOT NULL, 
            waffle BOOLEAN NOT NULL, 
            autoPark BOOLEAN NOT NULL, 
            stonesDeliveredTele INTEGER NOT NULL, 
            stonesPlaced INTEGER NOT NULL, 
            height INTEGER NOT NULL, 
            repositioning BOOLEAN NOT NULL, 
            capstone INTEGER NOT NULL, 
            parking BOOLEAN NOT NULL, 
            notes TEXT, 
            penalties BOOLEAN NOT NULL, 
            broken BOOLEAN NOT NULL
        )""")
    
    def addMatch(self, dbConnection, teamid, skystoneBonus, stonesDelivered, waffle, autoPark, stonesDeliveredTele, stonesPlaced, height, repositioning, capstone, parking, notes, penalties, broken):
        dbConnection.execute("""
        INSERT INTO Matches (teamid, skystoneBonus, stonesDelivered, waffle, autoPark, stonesDeliveredTele, stonesPlaced, height, repositioning, capstone, parking, notes, penalties, broken) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """, (teamid, skystoneBonus, stonesDelivered, waffle, autoPark, stonesDeliveredTele, stonesPlaced, height, repositioning, capstone, parking, notes, penalties, broken))

    def getAllMatches(self, dbConnection):
        matchList = []
        for row in dbConnection.execute("""
        SELECT Teams.number, skystoneBonus, stonesDelivered, waffle, autoPark, stonesDeliveredTele, stonesPlaced, height, repositioning, capstone, parking, notes, penalties, broken, Matches.id
        FROM Matches INNER JOIN Teams ON Matches.teamid = Teams.id ORDER BY Teams.number
        """):
            matchList.append(Match(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13], row[14]))
        
        return matchList

    def getSelectedMatches(self, dbConnection, where):
        matchList = []
        text = f"""
        SELECT Teams.number, skystoneBonus, stonesDelivered, waffle, autoPark, stonesDeliveredTele, stonesPlaced, height, repositioning, capstone, parking, notes, penalties, broken, Matches.id
        FROM Matches INNER JOIN Teams ON Matches.teamid = Teams.id WHERE {where} ORDER BY Teams.number"""
        print(text)
        for row in dbConnection.execute(text):
            matchList.append(Match(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13], row[14]))
        
        return matchList

    def runCommand(self, dbConnection, command, inputs=("","")):
        if inputs:
            return dbConnection.execute(command, inputs)
        else:
            return dbConnection.execute(command)


if __name__ == "__main__":
    DB_STRING = os.path.join(os.path.dirname(__file__), 'data/testdatabase.sqlite3')
    matches = Matches()
    with sqlite3.connect(DB_STRING) as connection:
        matches.createTable(connection)
        matches.addMatch(connection, 1,1,1,0,0,0,0,0,0,0,0,"",0,0)
        matchList = matches.getAllMatches(connection)
        for mathch in matchList:
            print(mathch)
