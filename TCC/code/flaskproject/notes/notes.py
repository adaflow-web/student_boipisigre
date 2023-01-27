
import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
# from werkzeug.datastructures import ImmutableMultiDict

app = Flask("notes")
app.config['SECRET_KEY'] = 'Pierre'


def get_db_connection():
    conn = sqlite3.connect('static/db/lesnotes.db')
    conn.row_factory = sqlite3.Row
    print("Connection established ..........")
    return conn

def get_notes(filtre):
    DBCon = get_db_connection()

    # print("=================================")
    # Ouvrir un curseur
    ltable = DBCon.cursor()
    # print(filtre)
    if filtre == "*":
        notes = ltable.execute("select * from notes").fetchall()
    else:
        filtre="%"+filtre.upper()+"%"
        # print(filtre)
        notes = ltable.execute("select * from notes where upper(titre) like ?",[filtre,]).fetchall()# print(notes)
        # print(notes)

    ltable.close()
    DBCon.close()
    # print("=================================")
    return  notes

def add_notes(col1,col2):
    DBCon = get_db_connection()
    # print("=================================")
    # Ouvrir un curseur
    updtable = DBCon.cursor()
    data = [col1,col2]
    updtable.execute("insert into notes (titre,corps,creation) values (?, ?, date())", data)
    DBCon.commit()
    print ("sauver")
    updtable.close()
    DBCon.close()
    return

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM notes WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post
@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/notes")
def notes():
    lesnotes=get_notes("*")
    return render_template('notes.html', posts=lesnotes)


@app.route("/addnotes")
def addnotes():
    return render_template("ajoutnote.html")

@app.route("/clear")
def clear():
    return render_template("ajoutnote.html")

@app.route("/ajoutnote", methods=('GET', 'POST'))
def ajoutnote():
    message = ""
    if request.method == 'POST':
        txt_titre = request.form['titre']
        txt_corps = request.form["corps"]
        if not txt_titre :
            flash('Un titre est obligatoire!')
        else:
            txt_corps = txt_corps.replace("\n"," ")
            # note = txt_titre + " € " + txt_corps + "\n"
            add_notes(txt_titre,txt_corps)
            message = " notes "+ txt_titre + " sauvée "
            flash(message)
    return redirect(url_for('notes'))

@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('unenote.html', post=post)

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
        lesnotes=get_notes(txt_recherche)
        trouvé=False
        if len(lesnotes) > 0:
            trouvé=True

        if not(trouvé):
            flash('note non trouvée!')
            #change_value= change_value + "<p> note non trouvée</p>"
    else:
        flash('Votre texte est vide : recherche non valide !')
        lesnotes=get_notes("€$")
        # change_value= "<p> recherche non valide</p>"

    return render_template("notes.html", posts=lesnotes)

@app.route('/redakti/<int:id>', methods=('GET', 'POST'))
def redakti(id):

    post = get_post(id)
    if request.method == 'POST':
        titolo = request.form['titolo']
        enhavo = request.form['enhavo']
        if not titolo:
            flash('Un titre est obligatoire!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE notes SET titre = ?, corps = ?, creation=date()'
                         ' WHERE id = ?',
                         (titolo, enhavo, id))
            conn.commit()
            conn.close()
            return redirect(url_for('notes'))

    return render_template('editer.html', post=post)

@app.route('/<int:id>/forigi', methods=('POST',))
def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM notes WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['titre']))
    return redirect(url_for('notes'))
