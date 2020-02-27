<%def name="title()">Match Sim (Beta)</%def>
<%def name="head()"></%def>
<%inherit file = "base.mako"/>

<head>
<h1 style="text-align:center;"> Match Sim Home Page </h1>
</head>
<form action="matchSim" method="post" enctype="multipart/form-data">
    <table>
    <tr style="text-align:center"> <td> RED </td><td> BLUE </td> </tr>
    <tr>
    <td>
    <select name="red1">
        %for team in teamList:
            <option value=${team.teamId}> ${team.teamNumber} -- ${team.teamName} </option>
        %endfor
        </td>
     <td>
    <select name="blue1">
        %for team in teamList:
            <option value=${team.teamId}> ${team.teamNumber} -- ${team.teamName} </option>
        %endfor
        </td>
    </tr>
    <tr> <td>
    <select name="red2">
        %for team in teamList:
            <option value=${team.teamId}> ${team.teamNumber} -- ${team.teamName} </option>
        %endfor
        </td>
         <td>
    <select name="blue2">
        %for team in teamList:
            <option value=${team.teamId}> ${team.teamNumber} -- ${team.teamName} </option>
        %endfor
        </td>
    </tr>
    </table>
    <input type="submit"> </form>
