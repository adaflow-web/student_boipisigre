
import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
# from werkzeug.datastructures import ImmutableMultiDict

app = Flask("notes")
app.config['SECRET_KEY'] = 'Pierre'

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
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/notes")
def notes():
    notepage = render_template("notes.html")
    lesnotes=get_notes()
    return notepage.replace("$$MesNotes$$",affiche_note(lesnotes))

@app.route("/addnotes")
def addnotes():
    return render_template("ajoutnote.html")


@app.route("/ajoutnote", methods=('GET', 'POST'))
def ajoutnote():
    message = ""
    if request.method == 'POST':
        # data = ImmutableMultiDict(request.form)
        # txt_titre = data.get('titre')
        # txt_corps = data.get("corps")
        txt_titre = request.form['titre']
        txt_corps = request.form["corps"]
        if not txt_titre :
            flash('Un titre est obligatoire!')
        else:
            txt_corps = txt_corps.replace("\n"," ")
            note = txt_titre + " € " + txt_corps + "\n"
            add_notes(txt_titre,txt_corps)
            message = " notes "+ txt_titre + " sauvée "

    notepage = render_template("notes.html")
    return  notepage.replace("$$MesNotes$$",message)


@app.route("/chercher")
def chercher():
    return render_template("recherche.html")

@app.route("/rechercher")
def rechercher():
    # return "résultat de ma recherche"
    txt_recherche =request.args.get("query")
    change_value=" "
    # notepage = render_template("notes.html")
    if (txt_recherche != ""):
        lesnotes=get_notes()
        trouvé=False
        for unenote in lesnotes:
            champs=unenote[0].split("€")
            if (txt_recherche.upper() in champs[0].upper()):
                change_value=change_value + "<p class='titre'>" + champs[0] + "</p> <p class='corps'>" + champs[1] + "</p>"
                trouvé=True

        if not(trouvé):
            flash('note non trouvée!')
            #change_value= change_value + "<p> note non trouvée</p>"
    else:
        flash('Votre texte est vide : recherche non valide !')
        # change_value= "<p> recherche non valide</p>"
    notepage = render_template("notes.html")
    return notepage.replace("$$MesNotes$$",change_value)
