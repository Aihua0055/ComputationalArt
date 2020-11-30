from flask import Flask
from flask import abort, redirect, url_for


app = Flask(__name__)

# FLASK_ENV=development FLASK_APP=hello.py python -m flask run
@app.route('/')
def index():
    return redirect(url_for('hello'))


@app.route('/xijinping')
def gfw():
    abort(404)

@app.errorhandler(404)
def page_not_found(error):
    return "XJP 404 Not Found", 404


from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/video')
@app.route('/shipin')
def login():
    return '<b>Shi Pin</b>'