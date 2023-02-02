
import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, session
from werkzeug.exceptions import abort

# from werkzeug.datastructures import ImmutableMultiDict

app = Flask("notes")
SESSION_TYPE = 'redis'
app.config.from_object('notes')
app.config.update(SECRET_KEY='osd(99092=36&462134kjKDhuIS_d23')



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

def get_notes_user(filtre):
    DBCon = get_db_connection()

    # print("=================================")
    # Ouvrir un curseur
    ltable = DBCon.cursor()
    # print(filtre)
    if filtre == "*":
        notes = ltable.execute("select * from notes").fetchall()
    else:
        filtre=filtre.upper()+"%"
        # print(filtre)
        notes = ltable.execute("select * from notes where upper(nomcreateur) like ?",[filtre,]).fetchall()# print(notes)
        # print(notes)

    ltable.close()
    DBCon.close()
    # print("=================================")
    return  notes


def add_notes(col1,col2,col3):
    DBCon = get_db_connection()
    # print("=================================")
    # Ouvrir un curseur
    updtable = DBCon.cursor()
    data = [col1,col2,col3]
    updtable.execute("insert into notes (titre,corps,creation,modif,nomcreateur) values (?, ?, date(), date(),?)", data)
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
    print(post)
    if post is None:
        abort(404)
    return post

def get_user(nom):
    conn = get_db_connection()
    mdp = conn.execute('SELECT mdp FROM utilisateur WHERE nom = ?',(nom,)).fetchone()
    conn.close()
    print(mdp[0])
    if mdp is None:
        abort(404)
    return mdp

def saveuserDB(nom):
    session["user_name"] = nom
    '''    conn = get_db_connection()
        # data=[nom,]
        conn.execute('UPDATE utilisateur SET nom = ?, modif=date() '
                ' WHERE id = 1',
                  (nom,))
                  conn.commit()
                  conn.close()
    '''
    return nom

@app.route("/")
def homepage():
    #print(session['logged_in'])
    if not session.get("logged_in"):
        # print(session["user_name"])
        return render_template('login.html')
    else:
        print(session["user_name"])
        return render_template('index.html')

@app.route('/login', methods=['POST',"GET"])
def do_admin_login():

    #
    nom=request.args.get("username")
    pwd=get_user(nom)

    if request.args.get("password") == pwd[0] :
        session['logged_in'] = True
        session['user_name'] = nom
        # print(session['logged_in'])
        # print(session['user_name'])

    else:
        flash('wrong password!')
        session['logged_in'] = False

    return homepage()

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/notes")
def notes():
    lesnotes=get_notes("*")
    utilisateur=session["user_name"]
    # utilisateur=get_user()
    #print(utilisateur[0])
    return render_template('notes.html', posts=lesnotes, nom=utilisateur)

@app.route("/addnotes")
def addnotes():
    return render_template("ajoutnote.html")

@app.route("/clear")
def clear():
    return render_template("login.html", action="clear")

@app.route("/ajoutnote", methods=('GET', 'POST'))
def ajoutnote():
    message = ""
    if request.method == 'POST':
        txt_titre = request.form['titre']
        txt_createur = request.form['createur']
        txt_corps = request.form["corps"]
        if not txt_titre :
            flash('Un titre est obligatoire!')
        else:
            txt_corps = txt_corps.replace("\n"," ")
            # note = txt_titre + " € " + txt_corps + "\n"
            add_notes(txt_titre,txt_corps,txt_createur)
            message = " notes "+ txt_titre + " ajoutée "
            flash(message)
    return redirect(url_for('notes'))

@app.route('/<int:post_id>/<string:createur>')
def post(post_id,createur):
    post = get_post(post_id)
    return render_template('unenote.html', post=post, auteur=createur)

@app.route("/chercher")
def chercher():
    return render_template("recherche.html",query="titre")

@app.route("/cheruser")
def cheruser():
    return render_template("recherche.html", query="user")


@app.route("/rechercher")
def rechercher():
    # return "résultat de ma recherche"
    txt_recherche =request.args.get("titre")
    lesnotes=get_notes(txt_recherche)
    trouvé=False
    if len(lesnotes) > 0:
        trouvé=True

    if not(trouvé):
        flash('note non trouvée!')

    # utilisateur=get_user()
    utilisateur=session["user_name"]
    return render_template('notes.html', posts=lesnotes, nom=utilisateur)


@app.route("/recheruser")
def recheruser():
    # return "résultat de ma recherche"
    txt_recherche =request.args.get("user")
    # notepage = render_template("notes.html")
    lesnotes=get_notes_user(txt_recherche)
    trouvé=False
    if len(lesnotes) > 0:
        trouvé=True

    if not(trouvé):
        flash('note non trouvée!')

    utilisateur=session["user_name"]
    return render_template('notes.html', posts=lesnotes, nom=utilisateur)


@app.route("/saveuser")
def saveuser():
    # return "résultat de ma recherche"
    nomuser =request.args.get("user")
    saveuserDB(nomuser)

    return render_template("index.html",NomUtilisateur=nomuser)

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
            conn.execute('UPDATE notes SET titre = ?, corps = ?, modif=date()'
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
