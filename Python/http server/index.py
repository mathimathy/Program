import cgi

print("content-type: text/html; charset=utf-8\n")

#try:
#    with open("html/index.html") as f:
#        html = f.read()
#except:
#    html="<h1>ERROR 404</h1>"

html ="""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Bonjour</h1>
</body>
</html>"""

print(html)