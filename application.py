import os

from flask import Flask, session, redirect, render_template, request, url_for, session
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

socketio = SocketIO(app)

channel_list = []

@app.route("/", methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_name = request.form['name']
        new_channel = request.form['new_channel']

        if new_name != "":
            session['name'] = new_name
        if new_channel != "":
            channel_list.append(new_channel)

        return redirect(url_for('index', name=session['name'], channels=channel_list))
    
    return render_template('index.html', name=session['name'], channels=channel_list)

@app.route("/channels")
def channels():
    return render_template('index.html')