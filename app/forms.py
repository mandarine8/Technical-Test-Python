from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class Exercise1Form(FlaskForm):
  phrase = StringField('Enter your phrase:', validators=[DataRequired()])
  submit = SubmitField('Submit')

class Exercise2Form(FlaskForm):
  phrase = TextAreaField('Enter your text:', validators=[DataRequired()])
  submit = SubmitField('Submit')
