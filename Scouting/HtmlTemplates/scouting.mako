<%def name="title()">Home Page - ftc16072</%def>
<%def name="head()"></%def>
<%inherit file = "base.mako"/>

<head>
<a href="/"> <button> Home </button> </a>

<h1 style="text-align:center;"> Scouting </h1>
</head>

<body>
    <form>
        <select>
            <% print(teamDict) %>
            % for number, name in teamDict:
                <option value=${number}> ${number + "--" + name} </option>
            % endfor
        </select>
        <fieldset> <legend>Auto</legend>


        </fieldset>

        <fieldset> <legend>Tele-op</legend>


        </fieldset>

        <fieldset> <legend>Endgame</legend>


        </fieldset>
    </form>
</body>
