import os
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/host')
def host():
    pass

@app.route('/join')
def join():
    pass

app.run(host='0.0.0.0', port=81, debug = True)
