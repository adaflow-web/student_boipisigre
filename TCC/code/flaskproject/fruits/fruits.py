import flask


from flask import Flask

app = Flask("fruits")

@app.route("/")
def homepage():
    return "<p>Bonjour, vous!</p>"
