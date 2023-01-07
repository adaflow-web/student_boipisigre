import flask
from flask import Flask

app = Flask("notes")

def get_html(page):
    file=open(page+".html")
    content=file.read()
    file.close()
    return content

def get_notes():
    notesdb=open("static/lesnotes.txt")
    note = notesdb.read()
    notesdb.close()
    notes=note.splitlines()
    return  notes

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
        champs=note.split("€")
        change_value=change_value + "<p>" + champs[0] + "</p> <p>" + champs[1] + "</p>"
    return notepage.replace("$$MesNotes$$",change_value)

@app.route("/addnotes")
def addnotes():
    return get_html("ajoutnote")

@app.route("/chercher")
def chercher():
    return get_html("recherche")

@app.route("/rechercher")
def rechercher():
    # return "résultat de ma recherche"
    txt_recherche =flask.request.args.get("query")
    change_value=" "
    notepage = get_html("notes")
    if (txt_recherche != ""):
        lesnotes=get_notes()
        trouvé=False
        for unenote in lesnotes:
            champs=unenote.split("€")
            if (txt_recherche.upper() in champs[0].upper()):
                change_value=change_value + "<p>" + champs[0] + "</p> <p>" + champs[1] + "</p>"
                trouvé=True

        if not(trouvé):
            change_value= change_value + "<p> note non trouvée</p>"
    else:
        change_value= "<p> recherche non valide</p>"

    return notepage.replace("$$MesNotes$$",change_value)
