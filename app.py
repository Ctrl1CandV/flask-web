from flask_sqlalchemy import SQLAlchemy
from markupsafe import escape
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://lyj:20030626@localhost/flaskweb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))

@app.route('/')
def index():
    return "index page"

@app.route('/user/<name>')
def user_page(name):
    return f'User: {escape(name)}'

@app.route('/operation/add/<int:x>/<int:y>')
def add(x, y):
    return f'{x} + {y} = {x + y}'

if __name__ == '__main__':
    app.run()