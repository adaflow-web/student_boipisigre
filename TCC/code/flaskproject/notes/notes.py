import flask
from flask import Flask

app = Flask("notes")

def get_html(page):
    file=open(page+".html")
    content=file.read()
    file.close()
    return content

def get_notes():
    contactdb=open("static/lesnotes.txt")
    contact = contactdb.read()
    contactdb.close()
    contacts=contact.split("\n")
    return  contacts

@app.route("/")
def homepage():
    return get_html("index")

@app.route("/about")
def about():
    return get_html("about")

@app.route("/notes")
def notes():
    notepage = get_html("notes")
    lesnotes=get_notes()

    change_value=""
    for note in lesnotes :
        change_value=change_value + "<p>" + note + "</p>"
    return notepage.replace("$$MesNotes$$",change_value)

@app.route("/chercher")
def chercher():
    return get_html("recherche")

@app.route("/rechercher")
def rechercher():
    # return "résultat de ma recherche"
    txt_recherche =flask.request.args.get("query")
    change_value=" "
    notepage = get_html("notes")
    lesnotes=get_notes()
    trouvé=False
    for unenote in lesnotes:
        if (txt_recherche.upper() in unenote.upper()):
            change_value=change_value + "<p>" + unenote + "</p>"
            trouvé=True

    if not(trouvé):
        change_value= change_value + "<p> note non trouvée</p>"

    return contactpage.replace("$$MesNotes$$",change_value)
