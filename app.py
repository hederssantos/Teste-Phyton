from flask import Flask

app = Flask("hello")

@app.route("/")
def hello():
    return "Hello Word"

@app.route("/contatos") 
def contato():
    return"""<html>
	<head>
		<title> Contatos </title>
	</head>
	<body>
		<h2>Heder Souza dos Santos</h2>
</html>l"""

