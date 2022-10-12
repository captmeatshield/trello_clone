from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://trello_dev:password123@127.0.0.1:5432/trello'

db = SQLAlchemy(app)

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    date = db.Column(db.String)
    status = db.Column(db.String)
    priority = db.Column(db.String)


@app.cli.command('create')
def create_db():
    db.create_all()
    print("Tables created")

@app.route('/')
def index():
    return 'hello'