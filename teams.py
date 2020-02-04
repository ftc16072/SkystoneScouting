import sqlite3
import os

class Team():
    def __init__(self, teamNumber, teamName, teamID):
        self.teamNumber = teamNumber
        self.teamName = teamName
        self.teamId = teamID
    
    def __str__(self):
        return f"{self.teamId}: {self.teamNumber} -- {self.teamName}"
    def __repr__(self):
        return f"{self.teamId}: {self.teamNumber} -- {self.teamName}"


class Teams():
    def createTable(self, dbConnection):
        dbConnection.execute("""
        CREATE TABLE Teams(
            id INTEGER PRIMARY KEY,
            number INTEGER NOT NULL,
            name STRING NOT NULL
        )""")

    def addTeam(self, teamNumber, teamName, dbConnection):
        dbConnection.execute("INSERT INTO Teams (number, name) VALUES (?,?)", (teamNumber, teamName))
    
    def getTeamList(self, dbConnection):
        teamList = []
        for row in dbConnection.execute("SELECT number, name, id FROM Teams"):
            teamList.append(Team(row[0], row[1], row[2]))
        return teamList
    
    def setupTeams(self, teamDict, dbConnection):
        for number, name in teamDict.items():
            self.addTeam(number, name, dbConnection)


if __name__ == "__main__":
    DB_STRING = os.path.join(os.path.dirname(__file__), 'data/testdatabase.sqlite3')
    teams = Teams()

    try:
        os.remove(DB_STRING)
    except IOError:
        pass #delete File, if it doesn't exist we don't care

    with sqlite3.connect(DB_STRING) as connection:
        teams.createTable(connection)
        teams.addTeam(16072, "Quantum Quacks", connection)
        print(teams.getTeamList(connection))
