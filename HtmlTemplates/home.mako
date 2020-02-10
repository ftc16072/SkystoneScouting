<%def name="title()">Home Page - ftc16072</%def>
<%def name="head()"></%def>
<%inherit file = "base.mako"/>

<head>
<h1 style="text-align:center;"> Scouting Home Page </h1>
</head>

<body>
  <table>
        <tr>
            <td> <a href="/present"> <button> All data </button> </a> </td>
        </tr>
    </table>
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
                     <br/> <input type="submit">
            </form>
</body>