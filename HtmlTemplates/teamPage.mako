<%def name="title()">Team Page - ftc# ${team.teamNumber}</%def>
<%def name="head()"></%def>
<%inherit file = "base.mako"/>

<head>
    <a href="/"> <button> Home </button> </a>
    <div>
        %if broken:
            <div style="background-color:Red; height:60px; width:90px; float:left;">
                <h2 style="text-align:center;"> BROKEN </h2>
            </div>
        %endif
        %if penalised:
            <div style="background-color:Yellow; height:60px; width:90px; float:right;">
                <h2 style="text-align:center;"> PENALTY </h2>
            </div>
        %endif
        <h1 style="text-align:center;">${team.teamNumber} -- ${team.teamName}</h1>
    </div>
</head>

<body>
    <div>
        <div style="float:Left;width:33%">
            OPR: ${infoDict["avgAuto"] + infoDict["avgTele"] + infoDict["avgEnd"]} <br/>
            Average Auto Score: ${infoDict["avgAuto"]} <br/>
            Average TeleOp Score: ${infoDict["avgTele"]} <br/>
            Average Endgame Score: ${infoDict["avgEnd"]} <br/>
            Percent matches broken: ${infoDict["percentBroken"] * 100}% <br/>
            match scores: ${infoDict["matchScores"]}
        </div>
        <div>
            <img src='data:image/png;base64,${matchHist}'/>
        </div>
    </div>
    <div>
        <h2 style="text-align:center">Bot profile:</h2>
        <table class="matches">
            <tr> 
                <td>
                    <table class="matches">
                        <tr>
                            <td>
                                <h3 style="text-align:center;"> Ferry: </h3>
                                <ul>
                                    <li>Average blocks delivered: <b>${infoDict["avgTeleBlocks"]}</b> </li>
                                </ul>
                            </td>
                            <td>
                                <h3 style="text-align:center;"> Stacking: </h3>
                                <ul>
                                    <li>Average stones placed: <b>${infoDict["avgPlaced"]}</b> </li>
                                    <li>Average height: <b>${infoDict["avgHeight"]}</b> </li>
                                <ul>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <h3 style="text-align:center;"> Auto: </h3>
                                <ul>
                                    <li> Percent of the time they got the waffle: <b> ${infoDict["wafflePercent"] * 100}% </b> </li>
                                    <li> Average Skystones delivered: <b>${infoDict["avgSkystoneBonus"]}</b> </li>
                                    <li> Average Stones delivered: <b> ${infoDict["avgStonesDelivered"]}</b> </li>
                                    <li> Average Stones Placed: <b> ${infoDict["avgStonesPlaced"]} </b> </li>
                                    <li> Percent of the time they parked: <b> ${infoDict["autoParkedPercent"] * 100}% </b> </li>
                                </ul>
                            </td>
                            <td>
                                <h3 style="text-align:center;"> Endgame: </h3>
                                <ul>
                                    <li> Percent parked: ${infoDict["parkedPercent"] * 100}% </li>
                                    <li> Percent waflle: ${infoDict["repositioningPercent"] * 100}% </li>
                                    <li> Average capstone: ${infoDict["avgCapstone"]} </li>
                                </ul>
                            </td>
                        </tr>
                    </table>
                </td>
                <td>
                    <table class="matches">
                        <tr> <td> # </td> <td> round Num </td> <td> Bot was </td> <td> certenty </td> <td> Auto? </td></tr>
                        <% numIncrement = 0 %>
                        %for match in matchList:
                            <% numIncrement += 1 %>
                            <tr> <td> ${numIncrement} </td> <td> ${match.matchNum}</td> <td> </td> <td> </td> <td> </td>
                        %endfor
                    </table>
                </td>
        </table>
    </div>
    <div>
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
    </div>
</body>
