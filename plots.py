import base64
import random
from io import BytesIO
from matplotlib.pyplot import Figure
from matches import Match


class Plots():
    def test(self):
        x = []
        y=[]
        z=[]
        for i in range(0,100):
            x.append(random.randrange(0,100,1))
            y.append(random.randrange(0,100,1))
            z.append(random.randrange(0,100,1))
        return self.scatter(x,y,z)
    
    def scatter(self, x, y, z):
        fig = Figure()
        ax = fig.subplots()
        ax.scatter(x,y,s=z*1000, alpha=0.5)
        buf = BytesIO()
        fig.savefig(buf, format="png")
        # Embed the result in the html output.
        return base64.b64encode(buf.getbuffer()).decode("ascii")
    
    def fullMatches(self, matchList):
        x = []
        y = []
        z = []
        for match in matchList:
            x.append(match.autoScore)
            y.append(match.teleOpScore)
            z.append(match.endGameScore)
        return self.scatter(x,y,z)