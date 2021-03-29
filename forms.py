from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class NewSongForm(FlaskForm):
    artist = StringField('Artist', validators=[DataRequired()])
    name = StringField('Song', validators=[DataRequired()])
    article_no = IntegerField('Article index', validators=[DataRequired()])
    submit = SubmitField('Submit')
