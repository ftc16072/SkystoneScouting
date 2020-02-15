<%def name="title()">Home Page - ftc16072</%def>
<%def name="head()"></%def>
<%inherit file = "base.mako"/>

<head>
<a href="/"> <button> Home </button> </a>
<p>
    %if broken == "true":
    <div style="background-color:Red; height:30px; width:90px; text-align:left;">
        <h2 style="text-align:left;"> BROKEN </h2>
    </div>
    %endif
    %if penalised == True:
        <div style="background-color:Yellow;height:30px; width:90px; text-align:right;">
        <h2> PENALTY </h2>
        </div>
    %endif
<h1 style="text-align:center;">${team.teamNumber} -- ${team.teamName}</h1>
</p>
</head>

<body>
    <table class="matches">
        <tr class="heading"> <td> scouting form # </td> <td> Match #</td><td>Alliance</td> <td> Team #</td><td>skystoneBonus</td> <td>stonesDelivered</td> 
        <td>auto stones placed:</td><td>waffle</td><td>autoPark</td><td>teleStnsDliver</td><td>stonesPlaced</td><td> height</td><td>repositioning</td>
        <td>capstone</td><td>parking</td><td>notes</td><td>penalties</td><td>broken</td><td>Submited By:</td>
        %for match in matchList:
            <tr>
                <td>${match.matchId}</td>
                <td>${match.matchNum}</td>
                %if match.alliance:
                    <td>Red</td>
                %else:
                    <td>Blue</td>
                %endif
                <td>${match.teamNum}</td>
                <td>${match.skystoneBonus}</td>
                <td>${match.stonesDelivered}</td>
                <td>${match.autoStonesPlaced}
                <td>${match.waffle}</td>
                <td>${match.autoPark}</td>
                <td>${match.stonesDeliveredTele}</td>
                <td>${match.stonesPlaced}</td>
                <td>${match.height}</td>
                <td>${match.repositioning}</td>
                <td>${match.capstone}</td>
                <td>${match.parking}</td>
                <td>${match.notes}</td>
                <td>${match.penalties}</td>
                <td>${match.broken}</td>
                <td>${match.submitedByNum}</td>
            </tr>
        %endfor
    </table>
</body>
