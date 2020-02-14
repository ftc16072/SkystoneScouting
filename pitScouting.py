import sqlite3
import os
from teams import Teams

class PitSheet:
    def __init__(self, sheetId, teamNum, autoList, teleFerry, teleStack, teleStackHeight, endWaffle, endPark, capstone, notes, submitedBy):
        self.sheetId = sheetId
        self.teamNum = teamNum
        self.autoList = autoList
        self.teleFerry = teleFerry
        self.teleStack = teleStack
        self.teleStackHeight = teleStackHeight
        self.endWaffle = endWaffle
        self.endPark = endPark
        self.capstone = capstone
        self.notes = notes
        self.submitedBy = submitedBy
        
        
class pitScouting:

    def convertAutoStringToAutoList(self, autoString):
        autoList = []
        inWord = False
        word = ""

        for auto in autoString:
            if inWord:
                word += auto
            if auto == "'":
                if inWord:
                    autoList.append(word[:-1])
                    word = ""
                inWord = not inWord
        
        return autoList

    def createTable(self, dbConnection):
        dbConnection.execute("""
        CREATE TABLE pitScouting(
            id INTEGER PRIMARY KEY,
            teamId INTEGER NOT NULL,
            autos STRING,
            teleFerry BOLEAN NOT NULL,
            teleStack BOLEAN NOT NULL,
            teleStackHeight INTEGER NOT NULL,
            endWaffle BOLEAN NOT NULL,
            endPark BOLEAN NOT NULL,
            capstone INTEGER NOT NULL,
            notes STRING,
            submitedBy STRING
        )""")
    
    def addPitScoutSheet(self, dbConnection, teamId, autos, teleFerry, teleStack, teleStackHeight, endWaffle, endPark, capstone, notes, submitedBy):
        dbConnection.execute("INSERT INTO pitScouting (teamID, autos, teleFerry, teleStack, teleStackHeight, endWaffle, endPark, capstone, notes, submitedBy) VALUES (?,?,?,?,?,?,?,?,?,?)", (teamId, str(autos), teleFerry, teleStack, teleStackHeight, endWaffle, endPark, capstone, notes, submitedBy))
    
    def getAllPitScout(self, dbConnection):
        sheetList = []
        for row in dbConnection.execute("SELECT pitScouting.id, teams.number, autos, teleFerry, teleStack, teleStackHeight, endWaffle, endPark, capstone, notes, submitedBy FROM pitScouting INNER JOIN teams ON pitScouting.teamId = teams.id"):
            sheetId = row[0]
            teamNumber = row[1]
            autoList = self.convertAutoStringToAutoList(row[2])
            teleFerry = row[3]
            teleStack = row[4]
            teleStackHeight = row[5]
            endWaffle = row[6]
            endPark = row[7]
            capstone = row[8]
            notes = row[9]
            submitedBy = row[10]
            sheetList.append(PitSheet(sheetId, teamNumber, autoList, teleFerry, teleStack, teleStackHeight, endWaffle, endPark, capstone, notes, submitedBy))
        return sheetList

if __name__ == "__main__":
    DB_STRING = os.path.join(os.path.dirname(__file__), 'data/testdatabase.sqlite3')
    pitSheet = pitScouting()
    teams = Teams()

    try:
        os.remove(DB_STRING)
    except IOError:
        pass #delete File, if it doesn't exist we don't care

    with sqlite3.connect(DB_STRING) as connection:
        teams.createTable(connection)
        teams.addTeam(16072, "Quantum Quacks", connection)
        pitSheet.createTable(connection)
        pitSheet.addPitScoutSheet(connection, 1,"",1,0,0,0,0,0,"")
        sheetList = pitSheet.getAllPitScout(connection)
        for pitSheet in sheetList:
            print(pitScouting)