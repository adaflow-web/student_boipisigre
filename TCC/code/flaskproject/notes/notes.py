
import markdown
from flask import Flask, render_template, request, url_for, flash, redirect, session
from werkzeug.exceptions import abort
from werkzeug.security import generate_password_hash, check_password_hash
import time
from database import *
# from werkzeug.datastructures import ImmutableMultiDict

app = Flask("notes")
SESSION_TYPE = 'redis'
app.config.from_object('notes')
app.config.update(SECRET_KEY='osd(99092=36&462134kjKDhuIS_d23')

@app.route("/")
def homepage():
    if not session.get("logged_in"):
        return render_template('login.html',action='message')
    else:
        return render_template('index.html')

@app.route('/login', methods=['POST',"GET"])
def do_admin_login():
    nom=request.args.get("username")
    pwd=get_user(nom)
    session['logged_in'] = False
    if pwd is None :
        flash('Utilisateur inconnu!')
    else:
        if check_password_hash(pwd[0], request.args.get("password")):
            session['logged_in'] = True
            session['user_name'] = nom
        else:
            flash('Mot de passe éroné!')

    return homepage()

@app.route('/register', methods=['POST',"GET"])
def register():
    return render_template("register.html", action="clear")

@app.route('/logout', methods=['POST',"GET"])
def logout():
    session['logged_in'] = False
    return render_template("index.html", action="clear")


@app.route('/registeruser', methods=['POST',"GET"])
def registeruser():

    nom=request.args.get("username")
    pwd=request.args.get("password")
    hashpwd=generate_password_hash(pwd)
    add_user(nom, hashpwd)
    session['logged_in'] = False
    return homepage()

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/readme")
def readme():
    # Ouverture fichier readme.me
    lefichier= open("readme.md")
    contentmd = lefichier.read()
    lefichier.close()
    content=markdown.markdown(contentmd)

    return render_template("readme.html", texte=content)

@app.route("/notes")
def notes():
    lesnotes=get_notes("*")
    if session.get("logged_in") :
        utilisateur=session["user_name"]
        return render_template('notes.html', posts=lesnotes, nom=utilisateur)
    else:
        flash("Vous n'êtes pas connecté!")
        return homepage()


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
            time.sleep(0.5)
    return redirect(url_for('homepage'))

@app.route('/<int:post_id>/<string:createur>')
def post(post_id,createur):
    post = get_post(post_id)
    rows=[]
    for ligne in post:
        ligne = dict(ligne)
        ligne['corps'] = markdown.markdown(ligne['corps'])
        rows.append(ligne)

    return render_template('unenote.html', post=rows[0], auteur=createur)

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


@app.route('/redakti/<int:id>', methods=('GET', 'POST'))
def redakti(id):

    post = get_post(id)
    if request.method == 'POST':
        titolo = request.form['titolo']
        enhavo = request.form['enhavo']
        if not titolo:
            flash('Un titre est obligatoire!')
        else:
            update_note(titolo, enhavo, id)
            return redirect(url_for('homepage'))

    return render_template('editer.html', post=post[0])

@app.route('/<int:id>/forigi', methods=('POST',))
def delete(id):
    post = get_post(id)
    delete_note(id)
    flash('"{}" was successfully deleted!'.format(post[0]['titre']))
    time.sleep(0.5)
    return redirect(url_for('homepage'))
