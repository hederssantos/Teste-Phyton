from flask import Flask

app = Flask("hello")

@app.route("/")
def hello():
    return "Hello Word"

@app.route("/contatos") 
def contato():
    return"""<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>CSS experiment</title>
    <style>
      h1 {
        color: blue;
        background-color: yellow;
        border: 1px solid black;
      }

      p {
        color: red;
      }
    </style>
  </head>
  <body>
    <h3>Hello World!</h3>
    <p><h7>This is a CSS example</h7></p>
  </body>
</html>"""

