import flask
from flask import Flask

app = Flask("param")

def get_html(page):
    file=open(page)
    content=file.read()
    file.close()
    return content

def get_contact():
    contactdb=open("static/lesinvités.txt")
    contact = contactdb.read()
    contactdb.close()
    contacts=contact.split("\n")
    return  contacts

@app.route("/")
def homepage():
    return get_html("index.html")

@app.route("/about")
def about():
    return get_html("about.html")

@app.route("/rechercher")
def rechercher():
    # return "résultat de ma recherche"
    texte=flask.request.args.get("query")
    change_value=" "
    contactpage = get_html("contacts.html")
    mycontacts=get_contact()
    try:
        resultat=mycontacts.index(texte)
        change_value=change_value + "<p>" + mycontacts[resultat] + "</p>"
    except:
        change_value= change_value + "<p> contact non trouvé</p>"

    return contactpage.replace("$$MesContacts$$",change_value)
