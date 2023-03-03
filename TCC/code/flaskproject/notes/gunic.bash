# export FLASK_APP=notes
gunicorn -w 4 --bind 127.0.0.1:5000 wsgi:app
