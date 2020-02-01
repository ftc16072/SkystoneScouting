<!DOCTYPE html>
<html>
<head>
   <title>${self.title()}</title>
   ${self.head()} 
   <meta name="viewport" content="width=device-width, initial-scale=1">
   <script defer src="https://use.fontawesome.com/releases/v5.3.1/js/all.js"></script>
   <link rel="stylesheet" href="static/style.css">
  
</head>
% if destination and destination == "Screen":
<body>
% else:
<body class="Print">
% endif
    ${self.body()}

</body>

</html>