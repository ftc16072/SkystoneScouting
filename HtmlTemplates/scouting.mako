<%def name="title()">Home Page - ftc16072</%def>
<%def name="head()"></%def>
<%inherit file = "base.mako"/>

<head>
<a href="/"> <button> Home </button> </a>

<h1 style="text-align:center;"> Scouting </h1>
</head>

<body>
    <form action="scouted" method="post" enctype="multipart/form-data">
        <fieldset><legend>Info</legend>
        <label for="team"> Team: </label>
        <select name="team">
            % for team in teamList:
                <option value=${team.teamId}> ${str(team.teamNumber) + " -- " + team.teamName} </option>
            % endfor
        </select> <br/>
        <label for="matchNum"> Match Number: </label>
        <input type="number" name="matchNum" step=1 value=${startingMatchNum} max="30" min="0"> <br/>
        <label for="redAlliance">Alliance:</label>
        Red: <input type="radio" name="redAlliance" value="true" checked> Blue: <input type="radio" name="redAlliance" value="false">
        </fieldset>
        <fieldset> <legend>Auto</legend>
            <label for="skystoneBonus">Skystone Bonus:</label> <br/>
            <input type="radio" name="skystoneBonus" value="0" checked>0
            <input type="radio" name="skystoneBonus" value="1">1
            <input type="radio" name="skystoneBonus" value="2">2
            <br/> <br/> <label for="stonesDelivered"> Stones delivered: </label><br/>
            <input type="number" name="stonesDelivered" step="1" value=0 max="6" min="0">
            <br/> <br/> <label for="autoStonesPlaced"> Stones Placed: </label> <br/>
            <input type="number" name="autoStonesPlaced" step=1 value=0 max="6" min="0">
            <br/> <br/> <label for="waffle"> Foundation: </label>
            no: <input type="radio" name="waffle" value=false checked> yes: <input type="radio" name="waffle" value=true> 

            <br/> <label for="autoPark"> Parking: </label>
            no: <input type="radio" name="autoPark" value=false checked> yes: <input type="radio" name="autoPark" value=true>   
         </fieldset>
        <fieldset> <legend>Tele-op</legend>
            <label for="stonesDeliveredTele"> Stones delivered: </label><br/>
            <input type="number" name="stonesDeliveredTele" step="1" value=0>

            <br/> <br/> <label for="stonesPlaced"> Stones placed: </label><br/>
            <input type="number" name="stonesPlaced" step="1" value=0>

            <br/> <br/> <label for="height"> Height Stacked: </label><br/>
            <input type="number" name="height" step="1" value=0 min="0"> !-- it doesn't matter if they knock it down, what height did they reach?

        </fieldset>
        <fieldset> <legend>Endgame</legend>
            <label for="repositioning"> Foundation: </label>
            no: <input type="radio" name="repositioning" value=false checked> yes: <input type="radio" name="repositioning" value=true>   

            <br/> <br/> <label for="capstone"> Capstone Height: </label><br/>
            <input type="number" name="capstone" step="1" value=-1 min="-1"> !-- "-1" means no capstone

            <br/><label for="parking"> Parking: </label>
            no: <input type="radio" name="parking" value=false checked> yes: <input type="radio" name="parking" value=true>   

        </fieldset>

        <fieldset> <legend> Other </legend>
        <label for="notes">Notes:</label>
        <input type="textarea" name="notes">

        <br/><label for="penalties"> Did they cause a penalty? </label>
            no: <input type="radio" name="penalties" value=false checked> yes: <input type="radio" name="penalties" value=true>   
        
        <br/><label for="broken"> Did they break </label>
            no: <input type="radio" name="broken" value=false checked> yes: <input type="radio" name="broken" value=true>      

        </fieldset>
        <input type=submit>
    </form>
</body>
