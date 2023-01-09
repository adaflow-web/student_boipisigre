import flask
import sqlite3
from flask import Flask

app = Flask("notes")

def get_html(page):
    file=open(page+".html")
    content=file.read()
    file.close()
    return content

def get_notes():
    DBCon = sqlite3.connect('static/db/lesnotes.db')

    print("Connection established ..........")
    # print("=================================")
    # Ouvrir un curseur
    ltable = DBCon.cursor()
    notes = ltable.execute("select titre ||' € '|| corps from notes").fetchall()
    # print(notes)
    ltable.close()
    DBCon.close()
    # print("=================================")
    return  notes

def add_notes(col1,col2):
    DBCon = sqlite3.connect('static/db/lesnotes.db')

    print("Connection established ..........")
    # print("=================================")
    # Ouvrir un curseur
    updtable = DBCon.cursor()
    data = [col1,col2]
    updtable.execute("insert into notes (titre,corps) values (?, ?)", data)
    DBCon.commit()
    print ("sauver")
    updtable.close()
    DBCon.close()
    return

def affiche_note(listenotes):
    change_value=""
    for note in listenotes :
        # print(note[0])
        champs=note[0].split("€")
        change_value=change_value + "<p class='titre'>" + champs[0] + "</p> <p class='corps'>" + champs[1] + "</p>"
    return change_value

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
    return notepage.replace("$$MesNotes$$",affiche_note(lesnotes))

@app.route("/addnotes")
def addnotes():
    return get_html("ajoutnote")

app.route("/menu")
def menu():
    return get_html("menu")


@app.route("/ajoutnote")
def ajoutnote():
    txt_titre =flask.request.args.get("titre")
    txt_corps = flask.request.args.get("corps")
    txt_corps = txt_corps.replace("\n"," ")
    note = txt_titre + " € " + txt_corps + "\n"
    add_notes(txt_titre,txt_corps)
    notepage = get_html("notes")
    message = " notes "+ txt_titre + " sauvée "

    return  notepage.replace("$$MesNotes$$",message)


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
            champs=unenote[0].split("€")
            if (txt_recherche.upper() in champs[0].upper()):
                change_value=change_value + "<p class='titre'>" + champs[0] + "</p> <p class='corps'>" + champs[1] + "</p>"
                trouvé=True

        if not(trouvé):
            change_value= change_value + "<p> note non trouvée</p>"
    else:
        change_value= "<p> recherche non valide</p>"

    return notepage.replace("$$MesNotes$$",change_value)
