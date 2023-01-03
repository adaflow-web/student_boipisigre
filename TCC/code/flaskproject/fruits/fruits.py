import flask
from flask import Flask

app = Flask("fruits")

def get_index(page):
    file=open(page)
    content=file.read()
    file.close()
    return content

@app.route("/")
def homepage():
    return get_index("index.html")

@app.route("/about")
def about():
    return get_index("about.html")
