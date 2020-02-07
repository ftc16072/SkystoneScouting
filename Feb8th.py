import sqlite3
import os

from teams import Teams
from matches import Matches, Match

teams = Teams()
matches = Matches()


teamDict = {
    2901:"Purple Gears",
    5270:"Cary Academy & Cary Academy",
    5309:"Plan B",
    7083:"Team Tundrabots",
    9021:"Literally Everyone",
    9076:"Sketchy Engineering",
    9581:"RoboRavens",
    12010:"ChargerBots",
    15571:"Penderlea Stingers",
    15680:"RoboRavens1",
    15681:"RoboRavens2",
    15707:"Bots by the Creek",
    16065:"OHMS",
    16072:"Quantum Quacks",
    16299:"0x474F Cyclones",
    16447:"Mechanical Maniacs",
    16509:"Hotline",
    16967:"Insight Robotics",
    17060:"MSR Miners"
}

if __name__ == "__main__":
    DB_STRING = os.path.join(os.path.dirname(__file__), 'data/database.sqlite3')
    
    try:
        os.remove(DB_STRING)
    except IOError:
        pass #delete File, if it doesn't exist we don't care

    with sqlite3.connect(DB_STRING) as connection:
        teams.createTable(connection)
        teams.setupTeams(teamDict, connection)
        matches.createTable(connection)
        print(teams.getTeamList(connection))


