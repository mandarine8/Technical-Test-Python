# Structure the forms for the entire application

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

# Form Properties for the Exercise 1
class Exercise1Form(FlaskForm):
  phrase = StringField('Enter your phrase:', validators=[DataRequired()])
  submit = SubmitField('Submit')

# Form Properties for the Exercise 2
class Exercise2Form(FlaskForm):
  phrase = TextAreaField('Enter your text:', validators=[DataRequired()])
  submit = SubmitField('Submit')
