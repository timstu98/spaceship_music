from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/SSdb.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

migrate = Migrate(app, db)

from models import Article, Song

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/blogs')
def blogs():
    return render_template('blogs.html')

@app.route('/db')
def db():
    songs_for_article = {
        article: Song.query.filter(Song.article == article)
        for article in Article.query.all()
    }
    return render_template('db.html',articles=Article.query.all(),songs_for_article=songs_for_article)