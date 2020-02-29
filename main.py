import os
import base64
from io import BytesIO
import sqlite3
import cherrypy
from matplotlib.pyplot import Figure
from mako.lookup import TemplateLookup
from teams import Team, Teams
from matches import Match, Matches
from matchSim import MatchSim, Auto
from plots import Plots

DB_STRING = os.path.join(os.path.dirname(__file__), 'data/database.sqlite3')

class Scouting(object):
    
    def __init__(self):
        self.lookup = TemplateLookup(directories = ['HtmlTemplates'], default_filters=['h'])
        self.teams = Teams()
        self.matches = Matches()
        self.plots = Plots()

    def dbConnect(self):
        return sqlite3.connect(DB_STRING, detect_types=sqlite3.PARSE_DECLTYPES)

    def template(self, template_name, **kwargs):
        return self.lookup.get_template(template_name).render(**kwargs)

    @cherrypy.expose
    def index(self):
        fieldList = ["Matches.id","Teams.number","matchNum","alliance","skystoneBonus","stonesDelivered","waffle","autoPark","stonesDeliveredTele","stonesPlaced","height","repositioning","capstone","parking","notes","penalties","broken", "submitedByNum"]    
        with sqlite3.connect(DB_STRING) as connection:   
            data = self.plots.fullMatches(self.matches.getAllMatches(connection))
            teamList = self.teams.getTeamList(connection)
        return self.template('home.mako', fieldList=fieldList, imageData=data, teamList=teamList)


    @cherrypy.expose
    def scouting(self):
        with sqlite3.connect(DB_STRING) as connection:
            teamList = self.teams.getTeamList(connection)

        return self.template('scouting.mako', teamList=teamList, startingMatchNum=1)


    @cherrypy.expose
    def scouted(self, team, matchNum, redAlliance, skystoneBonus, stonesDelivered, autoStonesPlaced, waffle, autoPark, stonesDeliveredTele, stonesPlaced, height, repositioning, capstone, parking, notes, penalties, broken, submitedById, knocked):
        with sqlite3.connect(DB_STRING) as connection:
            teamList = self.teams.getTeamList(connection)
            self.matches.addMatch(connection, team, matchNum, redAlliance, skystoneBonus, stonesDelivered, autoStonesPlaced, waffle, autoPark, stonesDeliveredTele, stonesPlaced, height, repositioning, capstone, parking, notes, knocked, penalties, broken, submitedById)
            
        return self.template('scouting.mako', teamList=teamList, startingMatchNum=int(matchNum)+1)

    @cherrypy.expose
    def present(self):
        with sqlite3.connect(DB_STRING) as connection:
            matchList = self.matches.getAllMatches(connection)
            print(matchList)
        return self.template('display.mako', matchList=matchList)
    
    @cherrypy.expose
    def getData(self, fieldName, operator, text, orderBy):
        combined = ""
        try:
            int(text)
            combined = fieldName + operator + text
        except ValueError:
            combined = fieldName + operator + "'" + text + "'"

          
        print(combined)       

        with sqlite3.connect(DB_STRING) as connection:
            if(combined):
                matchList = self.matches.getSelectedMatches(connection, combined, orderBy)
            else:
                matchList = self.matches.getAllMatches(connection)
            print(matchList)
        return self.template('display.mako', matchList=matchList)

    @cherrypy.expose
    def teamPage(self, teamId):
        with sqlite3.connect(DB_STRING) as connection:
            broken = self.matches.isTeamBroken(connection, teamId)
            penalised = self.matches.hasTeamBeenPenalized(connection, teamId)
            infoDict = self.matches.getTeamInfo(connection, teamId)
            matchBar = self.plots.bar(infoDict["matchScores"])
            print(broken)
            team = self.teams.getTeamfromID(connection, teamId)
            matchList = self.matches.getSelectedMatches(connection, f"Teams.number={team.teamNumber}", "matchNum")
        return self.template('teamPage.mako', matchList=matchList, team=team, broken=broken, penalised=penalised, infoDict=infoDict, matchBar=matchBar)
    
    @cherrypy.expose
    def matchSimulationLanding(self):
        with sqlite3.connect(DB_STRING) as connection:
            teamList = self.teams.getTeamList(connection)
        return self.template("landingPage.mako", teamList=teamList)

    @cherrypy.expose
    def matchSim(self, red1, red2, blue1, blue2):
        with sqlite3.connect(DB_STRING) as connection:
            matchSim = MatchSim(red1, red2, blue1, blue2, connection)
        return self.template("matchSim.mako", matchSim=matchSim)




if __name__ == "__main__":
    cherrypy.quickstart(Scouting(), config='development.conf')
   