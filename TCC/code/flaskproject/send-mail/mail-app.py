from flask import Flask
from flask_mail import Mail, Message

app = Flask('mail-app')

app.config['MAIL_SERVER']='mail.infomaniak.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'adminpad@monuage.ch'
app.config['MAIL_PASSWORD'] = 'w$7!7.P3zEoLM'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def index():
  msg = Message('Hello from the other side!', sender =   'adminpad@monuage.ch', recipients = ['pib@pirboazo.net'])
  msg.body = "Hey Paul, sending you this email from my Flask app, lmk if it works"
  print(msg.body)
  mail.send(msg)
  return "Message envoyé!"

if __name__ == '__main__':
   app.run()
