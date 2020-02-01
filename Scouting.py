import os
import sqlite3
import cherrypy
from mako.lookup import TemplateLookup

DB_STRING = os.path.join(os.path.dirname(__file__), 'data/database.sqlite3')


class Scouting(object):
    
    def __init__(self):
        self.lookup = TemplateLookup(directories = ['HtmlTemplates'], default_filters=['h'])

    def dbConnect(self):
        return sqlite3.connect(DB_STRING, detect_types=sqlite3.PARSE_DECLTYPES)

    def template(self, template_name, **kwargs):
        return self.lookup.get_template(template_name).render(**kwargs)

    @cherrypy.expose
    def index(self):
        return self.template('home.mako')

    @cherrypy.expose
    def scouting(self):
        teamDict = {
            "Number": "Name",
            "16072":"Quantum Quacks"
        }
        return self.template('scouting.mako', teamDict=teamDict)



if __name__ == "__main__":
    cherrypy.quickstart(Scouting(), config='development.conf')
   