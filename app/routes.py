from flask import render_template
from app import app
from app.forms import Exercise1Form, Exercise2Form
from app.exercises.phrase_reverse import phrase_reverse
from app.exercises.char_splitter import char_splitter

@app.route('/')
def index():
  return render_template('index.html', title='Home')

@app.route('/exercise1', methods=['GET', 'POST'])
def exercise_1():
  form = Exercise1Form()
  response = ""
  if form.validate_on_submit():
    response = phrase_reverse(form.phrase.data)
  return render_template('exercise_1.html', title='Phrase reverse', form=form, response=response)

@app.route('/exercise2', methods=['GET', 'POST'])
def exercise_2():
  form = Exercise2Form()
  response = ""
  if form.validate_on_submit():
    response = char_splitter(form.phrase.data)
  return render_template('exercise_2.html', title='Char splitter', form=form, response=response)

