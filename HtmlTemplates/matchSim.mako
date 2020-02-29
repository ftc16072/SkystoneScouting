<%def name="title()">Match Sim (Beta)</%def>
<%def name="head()"></%def>
<%inherit file = "base.mako"/>

<head>
    <br/><a href="/"> <button> Home </button> </a>
    <a href="/matchSimulationLanding"> <button> Match Sim Home </button> </a>

    <h1 style="text-align:center;"> Match Simulator (beta)</h1>
</head>

<body>
    <table class="matches">
        <tr style="text-align:center;"><td>Red</td><td>Blue</td></tr>
        <% 
        simAutoDict = matchSim.getAlianceAutoRoles() 
        simTeleDict = matchSim.getAlianceTelopRole()
        
        %>
        <tr> 
            <td>
                Auto: ${simAutoDict["Red"][0].score + simAutoDict["Red"][1].score} <br/>
                Teleop: ${(simTeleDict["Red"][2]) + (simTeleDict["Red"][3]) + (2 * simTeleDict["Red"][4])}

                <ul>
                    <li> Teleop <ul>
                    <li>Red1: ${simTeleDict["Red"][0]} </li>
                    <li>Red2: ${simTeleDict["Red"][1]} </li>
                    <li>Deliverd: ${simTeleDict["Red"][2]} </li>
                    <li>Placed: ${simTeleDict["Red"][3]} </li>
                    <li> Height: ${simTeleDict["Red"][4]} </li>
                    </ul>
                    </li>
                </ul>
            </td>
            <td>
                Auto: ${simAutoDict["Blue"][0].score + simAutoDict["Blue"][1].score} <br/>
                Teleop: ${(simTeleDict["Blue"][2]) + (simTeleDict["Blue"][3]) + (2 * simTeleDict["Blue"][4])}

                <ul>
                    <li> Teleop <ul>
                    <li>Blue1: ${simTeleDict["Blue"][0]} </li>
                    <li>Blue2: ${simTeleDict["Blue"][1]} </li>
                    <li>Deliverd: ${simTeleDict["Blue"][2]} </li>
                    <li>Placed: ${simTeleDict["Blue"][3]} </li>
                    <li> Height: ${simTeleDict["Blue"][4]} </li>
                    </ul>
                    </li>
                </ul>
            </td>
        </tr>
    </table>

</body>