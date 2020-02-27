import sqlite3
import os

from teams import Teams
from matches import Matches, Match

teams = Teams()
matches = Matches()


teamDict = {
    000:["Select Team", 0],
    731:["Wannabee Strange", 1],
    2901:["Purple Gears", 4],
    4653:["Irrational DoorKeepers", 5],
    5064:["Aperture Science", 6],
    5309:["Plan B", 7],
    5795:["Back To The Drawing Board", 2],
    5881:["Tungsteel", 8],
    6078:["Cut the Red Wire", 9],
    6183:["Thunderducks", 3],
    7083:["Team Tundrabots", 10],
    7105:["SWIFT Intergalactic Space Squirrels", 11],
    7444:["Sisters of the Motherboard", 12],
    8300:["Pi Rho Eagles", 15],
    8569:["RoboKnights", 16],
    9021:["Literally Everyone", 17],
    9076:["Sketchy Engineering", 18],
    9548:["Highly Combustible", 19],
    9977:["Circuit Shifters", 20],
    9993:["Storm Bots", 21],
    11528:["Bots of Prey", 22],
    12584:["Not Yet Determined", 23],
    12828:["Critical Overload", 24],
    13597:["Yadkin Valley Innovators", 25],
    13735:["∏∆S (Pirates) FTC", 26],
    14163:["The Pitt Crew", 27],
    14667:["Robo Goats", 28],
    14828:["Crypto Cardinals", 29],
    15249:["HYDRALX", 30],
    15333:["Code Sisters", 14],
    15707:["Bots by the Creek", 31],
    15830:["SWIFT Subaquatic Sea Sheep", 12],
    16072:["Quantum Quacks", 32],
    16147:["Mavericks Robotics", 33],
    16328:["Trial n' Error", 34],
    16429:["VoltEDGE", 35],
    16447:["Mechanical Maniacs", 36],
    16890:["TMSA Batteries", 37],
    17373:["Going Crazy", 38]
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


