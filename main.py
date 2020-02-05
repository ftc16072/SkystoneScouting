import os
import sqlite3
import cherrypy
from mako.lookup import TemplateLookup
from teams import Team, Teams
from matches import Match, Matches

DB_STRING = os.path.join(os.path.dirname(__file__), 'data/database.sqlite3')


class Scouting(object):
    
    def __init__(self):
        self.lookup = TemplateLookup(directories = ['HtmlTemplates'], default_filters=['h'])
        self.teams = Teams()
        self.matches = Matches()

    def dbConnect(self):
        return sqlite3.connect(DB_STRING, detect_types=sqlite3.PARSE_DECLTYPES)

    def template(self, template_name, **kwargs):
        return self.lookup.get_template(template_name).render(**kwargs)

    @cherrypy.expose
    def index(self):
        return self.template('home.mako')

    @cherrypy.expose
    def scouting(self):
        with sqlite3.connect(DB_STRING) as connection:
            teamList = self.teams.getTeamList(connection)

        return self.template('scouting.mako', teamList=teamList)


    @cherrypy.expose
    def scouted(self, team, skystoneBonus, stonesDelivered, waffle, autoPark, stonesDeliveredTele, stonesPlaced, height, repositioning, capstone, parking, notes, penalties, broken):
        with sqlite3.connect(DB_STRING) as connection:
            teamList = self.teams.getTeamList(connection)
            self.matches.addMatch(team, skystoneBonus, stonesDelivered, waffle, autoPark, stonesDeliveredTele, stonesPlaced, height, repositioning, capstone, parking, notes, penalties, broken)
            
        return self.template('scouting.mako', teamList=teamList)

    @cherrypy.expose
    def present(self):
        with sqlite3.connect(DB_STRING) as connection:
            return self.matches.getAllMatches(connection)
            


if __name__ == "__main__":
    cherrypy.quickstart(Scouting(), config='development.conf')
   