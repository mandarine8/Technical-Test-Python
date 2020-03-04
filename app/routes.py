# Skeletton of the application: Routes and controllers

from flask import render_template
from app import app
from app.forms import Exercise1Form, Exercise2Form
from app.exercises.phrase_reverse import phrase_reverse
from app.exercises.char_splitter import char_splitter

# Comportement of the Home page
@app.route('/')
def index():
  return render_template('index.html', title='Home')

# Comportement of the Exercise 1
@app.route('/exercise1', methods=['GET', 'POST'])
def exercise_1():
  form = Exercise1Form()
  response = ""
  if form.validate_on_submit():
    response = phrase_reverse(form.phrase.data)
  return render_template('exercise_1.html', title='Phrase reverse', form=form, response=response)

# Comportement of the Exercise 2
@app.route('/exercise2', methods=['GET', 'POST'])
def exercise_2():
  form = Exercise2Form()
  response = ""
  if form.validate_on_submit():
    response = char_splitter(form.phrase.data)
  return render_template('exercise_2.html', title='Char splitter', form=form, response=response)

# Comportement of the Contact page
@app.route('/contact')
def contact():
  return render_template('contact.html', title='Contact')
