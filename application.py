import os

from flask import Flask, session, redirect, render_template, request, url_for, session
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

socketio = SocketIO(app)

@app.route("/", methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['name'] = request.form['name']
        return redirect(url_for('index', name=session['name']))
    
    if 'name' in session:
        return render_template('index.html', name=session['name'])
    
    return render_template('index.html')

@app.route("/channels")
def channels():
    return render_template('index.html')