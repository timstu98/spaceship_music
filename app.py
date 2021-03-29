from flask import Flask, render_template, flash, redirect
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from forms import NewSongForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/SSdb.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'put some random string here' # for migrations
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean' # for admin
db = SQLAlchemy(app)

migrate = Migrate(app, db)

from models import Article, Song

admin = Admin(app, name='Articles and Songs', template_mode='bootstrap3')
admin.add_view(ModelView(Article, db.session))
admin.add_view(ModelView(Song, db.session))

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

@app.route('/db_add', methods=['GET', 'POST'])
def db_add():
    form = NewSongForm()
    print('------')
    if not form.validate_on_submit():
        print('no submit')
        return render_template('db_add.html', form=form)

    artist = form.artist.data.strip()
    name = form.name.data.strip()
    article_no = int(form.article_no.data)
    print('loaded data')
    print(f'artis: {artist} . Song: {name} . Article_no: {article_no} ')
    print(len(Song.query.filter(Song.article_no == article_no).all()))

    if len(Song.query.filter(Song.article_no == article_no).all()) == 0:
        print('about to flash')
        print(Song.query.filter().all())
        flash(f'Error: Article number {article_no} does not exist' )
        return render_template('db_add.html', form=form)

    song = Song(artist=artist,name=name, article_no=article_no)
    db.session.add(song)
    db.session.commit()
    flash(f'New song {name} created')
    print('Reached end')
    return redirect('/db')