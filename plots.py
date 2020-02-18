import base64
import random
from io import BytesIO
from matplotlib.pyplot import Figure
import numpy as np
from matches import Match


class Plots():
    def saveAsPng(self, fig):
        buf = BytesIO()
        fig.savefig(buf, format="png")
        # Embed the result in the html output.
        return base64.b64encode(buf.getbuffer()).decode("ascii")

    def test(self):
        x = []
        y=[]
        z=[]    
        for i in range(0,100):
            x.append(random.randrange(0,100,1))
            y.append(random.randrange(0,100,1))
            z.append(random.randrange(0,100,1))
        return self.scatter(x,y,z)
    
    def scatter(self, x, y, z, team):
        fig = Figure()
        ax = fig.subplots()
        print(x, y, z, team)
        for a, b, c, teamNum in zip(x, y, z, team):
            print(a, b, c, teamNum)
            ax.scatter(a,b,s=c*100, alpha=0.5, label=teamNum)
        ax.legend()
        return self.saveAsPng(fig)
    
    def histogram(self, x):
        fig = Figure()
        ax = fig.subplots()
        ax.hist(x, bins=20)
        return self.saveAsPng(fig)

    
    def fullMatches(self, matchList):
        scoreDict = {}
        x = []
        y = []
        z = []
        team = []
        for match in matchList:
            if match.teamNum in scoreDict:
                scoreDict[match.teamNum]["x"].append(match.autoScore)
                scoreDict[match.teamNum]["y"].append(match.teleOpScore)
                scoreDict[match.teamNum]["z"].append(match.endGameScore)
            else:
                scoreDict[match.teamNum] = {}
                scoreDict[match.teamNum]["x"] = [match.autoScore]
                scoreDict[match.teamNum]["y"] = [match.teleOpScore]
                scoreDict[match.teamNum]["z"] = [match.endGameScore]
        for teamNum, scoreDicts in scoreDict.items():
            team.append(teamNum)
            for key, value in scoreDicts.items():
                valTot = 0
                valNum = len(value) - 1
                for val in value:
                    valTot += val
                if key == "x":
                    x.append(valTot / valNum)
                elif key == "y":
                    y.append(valTot / valNum)
                else:
                    z.append(valTot / valNum)


        return self.scatter(x,y,z,team)