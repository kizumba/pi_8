from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('mapa.html')

@app.route('/sobre')
def sobre():
	return render_template('sobre.html')