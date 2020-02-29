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
    
    def scatter(self, x, y, team):
        fig = Figure()
        ax = fig.subplots()
        print(x, y, team)
        for a, b, teamNum in zip(x, y, team):
            ax.scatter(a,b,s=100, alpha=0.5,)
            ax.annotate(s=teamNum,xy=(a,b), xytext=(a+0.5, b+0.5))
        ax.set_xlabel("Average Auto Score")
        ax.set_ylabel("Average Tele Op Score (incl End Game)")
        return self.saveAsPng(fig)
    
    def histogram(self, x):
        fig = Figure()
        ax = fig.subplots()
        ax.hist(x, bins=20)
        return self.saveAsPng(fig)

    def bar(self, y):
        fig = Figure()
        ax = fig.subplots()
        for i, j in zip(y, range(len(y))):
            print("******")
            print(j,i)
            ax.bar(j, i, width=0.4)
        ax.set_xlabel("Match Num")
        ax.set_ylabel("Points")
        return self.saveAsPng(fig)

    
    def fullMatches(self, matchList):
        scoreDict = {}
        x = []
        y = []
        team = []
        for match in matchList:
            if match.teamNum in scoreDict:
                scoreDict[match.teamNum]["x"].append(match.autoScore)
                scoreDict[match.teamNum]["y"].append(match.teleOpScore + match.endGameScore)
            else:
                scoreDict[match.teamNum] = {}
                scoreDict[match.teamNum]["x"] = [match.autoScore]
                scoreDict[match.teamNum]["y"] = [match.teleOpScore + match.endGameScore]
        for teamNum, scoreDicts in scoreDict.items():
            team.append(teamNum)
            for key, value in scoreDicts.items():
                valTot = 0
                valNum = len(value) - 1
                valNum = 1 if valNum == 0 else valNum
                for val in value:
                    valTot += val
                if key == "x":
                    x.append(valTot / valNum)
                elif key == "y":
                    y.append(valTot / valNum)


        return self.scatter(x,y,team)