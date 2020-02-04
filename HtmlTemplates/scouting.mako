<%def name="title()">Home Page - ftc16072</%def>
<%def name="head()"></%def>
<%inherit file = "base.mako"/>

<head>
<a href="/"> <button> Home </button> </a>

<h1 style="text-align:center;"> Scouting </h1>
</head>

<body>
    <form action="/scouted">
        <select>
            <% print(teamList) %>
            % for team in teamList:
                <option value=${team.teamId}> ${str(team.teamNumber) + "--" + team.teamName} </option>
            % endfor
        </select>
        <fieldset> <legend>Auto</legend>
            <label for="skystoneBonus">Skystone Bonus:</label> <br/>
            <input type="radio" name="skystoneBonus" value="0" checked>0
            <input type="radio" name="skystoneBonus" value="1">1
            <input type="radio" name="skystoneBonus" value="2">2
            <br/> <br/> <label for="stonesDelivered"> Stones delivered: </label><br/>
            <input type="number" name="stonesDelivered" step="1" value=0>
            <br/> <br/> <label for="waffle"> Repositioning: </label>
            <input type="checkbox" name="waffle">

            <br/> <label for="park"> Parking: </label>
            <input type="checkbox" name="park">
        </fieldset>
        <fieldset> <legend>Tele-op</legend>
            <label for="stonesDelivered"> Stones delivered: </label><br/>
            <input type="number" name="stonesDelivered" step="1" value=0>

            <br/> <br/> <label for="stonesPlaced"> Stones placed: </label><br/>
            <input type="number" name="stonesPlaced" step="1" value=0>

            <br/> <br/> <label for="height"> Height Stacked: </label><br/>
            <input type="number" name="height" step="1" value=0> !-- it doesn't matter if they knock it down, what hight did they reach?

        </fieldset>
        <fieldset> <legend>Endgame</legend>
            <label for="waffle"> Repositioning: </label>
            <input type="checkbox" name="waffle">

            <br/> <br/> <label for="capstone"> Capstone Height: </label><br/>
            <input type="number" name="capstone" step="1" value=-1>

        </fieldset>
    </form>
</body>
