import sqlite3
import os

from teams import Teams
from matches import Matches, Match

teams = Teams()
matches = Matches()


teamDict = {
    000:"Select Team",
    731:"Wannabee Strange",
    2901:"Purple Gears",
    4653:"Irrational DoorKeepers",
    5064:"Aperture Science",
    5309:"Plan B",
    5795:"Back To The Drawing Board",
    5881:"Tungsteel",
    6078:"Cut the Red Wire",
    6183:"Thunderducks",
    7083:"Team Tundrabots",
    7105:"SWIFT Intergalactic Space Squirrels",
    7444:"Sisters of the Motherboard",
    8300:"Pi Rho Eagles",
    8569:"RoboKnights",
    9021:"Literally Everyone",
    9076:"Sketchy Engineering",
    9548:"Highly Combustible",
    9977:"Circuit Shifters",
    9993:"Storm Bots",
    11528:"Bots of Prey",
    12584:"Not Yet Determined",
    13597:"Yadkin Valley Innovators",
    13735:"∏∆S (Pirates) FTC",
    14163:"The Pitt Crew",
    14667:"Robo Goats",
    14828:"Crypto Cardinals",
    15249:"HYDRALX",
    15333:"Code Sisters",
    15707:"Bots by the Creek",
    15830:"SWIFT Subaquatic Sea Sheep",
    16072:"Quantum Quacks",
    16147:"Mavericks Robotics",
    16328:"Trial n' Error",
    16429:"VoltEDGE",
    16447:"Mechanical Maniacs",
    16890:"TMSA Batteries",
    17373:"Going Crazy"
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


