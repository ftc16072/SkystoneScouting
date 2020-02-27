<%def name="title()">Home Page - ftc16072</%def>
<%def name="head()"></%def>
<%inherit file = "base.mako"/>

<head>
<h1 style="text-align:center;"> Scouting Home Page </h1>
</head>

<body>
    <h4 style="text-align:center">
        This page was built by 16072 -- The Quantum Quacks <br/>
    </h4>
    <fieldset>
    <legend> Disclaimer </legend>
    <p>
        All of the data here is only as accurate as it can be for 5 or less matches of data. <br/>
        This data is entered by <b><i>Humans</i></b> this means that not all of the data is 100% accurate <br/>
        If you are detail oriented and would like to help keep this data accurate for teams, please consider scouting for some matches. <br/>
        If you are interested, Find Rishi from Quantum Quacks.
    </p>
    </fieldset>
  <table>
        <tr>
            <td> <a href="/present"> <button> All data </button> </a>
        </tr>
        <tr style="height:10px">
        </tr>
        <tr> 
            </td> <td>View Team Page:<td/>
            <td> <form action="teamPage" method="post" enctype="multipart/form-data">
            <select name="teamId">
                %for team in teamList:
                    <option value=${team.teamId}> ${team.teamNumber} -- ${team.teamName} </option>
                %endfor
            <input type="submit"> </form>
        </tr>
    </table> <br/>
            <form  action="getData" method="post" enctype="multipart/form-data">
                     <select name="fieldName">
                        %for field in fieldList:
                            <option value=${field}> ${field} </option>
                        %endfor
                     </select>
                     <select name="operator">
                        %for operator in ["=", ">", "<", ">=", "<="]:
                            <option value=${operator}> ${operator} </option>
                        %endfor
                    </select>
                    <input type="text-area" name="text">
                    ORDER BY
                     <select name="orderBy">
                        %for field in fieldList:
                            <% selected = "" %>
                            <% if field == "Teams.number":
                                    selected = "selected"
                            %>
                            <option value=${field} ${selected}> ${field} </option>
                        %endfor
                     </select>
                     <br/> <input type="submit">
            </form>
</body>
<img src='data:image/png;base64,${imageData}'/>