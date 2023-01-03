import flask
from flask import Flask

app = Flask("contacts")

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

@app.route("/contacts")
def contact():
    contactpage = get_html("contacts.html")
    mycontacts=get_contact()
    mycontacts.sort()

    change_value=""
    for contact in mycontacts :
        change_value=change_value + "<p>" + contact + "</p>"

    return contactpage.replace("$$MesContacts$$",change_value)
