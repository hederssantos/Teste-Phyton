from flask import Flask

app = Flask("hello")

@app.route("/")
def hello():
    return "Hello Word"

@app.route("/contatos") 
def contato():
    return "<h3>Alô, mundo!</h3>, email"

