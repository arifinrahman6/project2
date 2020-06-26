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
        if 'name' in request.form:
            session['name'] = request.form['name']
        if 'new_channel' in request.form:
            channel_list.append(request.form['new_channel'])

        return redirect(url_for('index', name=session['name'], channels=channel_list))
    
    return render_template('index.html', name=session['name'], channels=channel_list)

@app.route("/channels/<channel_name>")
def channel(channel_name):
    return render_template('channel.html', channel_name='{channel_name}')