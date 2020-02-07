<%def name="title()">Home Page - ftc16072</%def>
<%def name="head()"></%def>
<%inherit file = "base.mako"/>

<head>
<h1 style="text-align:center;"> Scouting Home Page </h1>
</head>

<body>
    <table>
        <tr>
            <td> <a href="/scouting"> <button> Scout </button> </a> </td>
            <td> <a href="/present"> <button> Info </button> </a> </td>
        </tr>
        <tr>
            <form  action="getData" method="post" enctype="multipart/form-data">
                <td>
                     Where: <input type="text-area" name="where">
                     <br/> <input type="submit">
                </td>
            </form>
        </tr>



