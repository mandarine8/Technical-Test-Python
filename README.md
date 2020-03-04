# Technical Test Python - Documentation


Details :
=========

### Description:
This application is a showcase for some technical exercises in Python and Flask.
The interface is used to try the results of the exercises.
Some additionnal functionnalites can be added like graphics, performances, storage of the results...
This app have to be deployed on Heroku. The tests are mandatory. Google is allowed.

### Instructions:
The purpose is to evaluate technical skills of the candidate, motivation and curiosity through:
* Code quality
* Unit test
* Conception
* UI
* Git use

### Have to contain:
* Language: Python3 + Flask
* Technologies UI: HTML, CSS, Bootstrap, Javascript, Ajax
* Framework: Pytest
* Git repository: Github + Heroku
* Minimun 3 exercises
* Documentation to explain how to execute the code, the tests, for the API and for the algorithms or the difficulties.


How to proceed :
================

### Requirements
* python 3.7
* virtualenv
* A github account

### Installation

#### How to start
```sh
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### How to execute the code
```sh
flask run
```

### Tests - How to run it
```sh
pytest
```

### Difficulties

There is still an issue remaining with the exercise 2, Char splitter.
Despite my successfull tests, when a text with the first line containing 10 characters
is submitted, a useless line is added in the response.
I tried to fix it by removing the "second" delimiter, but the problem persists and I don't understand why.

Learning Python and Flask in few days was challenging, and it's why it is not complete.
I wish I had time to finish at least a third exercise, and more features like a database
to store the responses.

### Acknowledgments

I am proud of what I have done, even if it's not complete.
I love learning, and this Python and Flask introduction was great.





More détails on Github:
* https://github.com/mandarine8/Technical-Test-Python
