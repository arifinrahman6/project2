from datetime import datetime
import os
from queue import Queue

from flask import Flask, session, redirect, render_template, request, url_for, session
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

socketio = SocketIO(app)

channel_list = []
messages = {}


@app.route("/", methods = ['GET', 'POST'])
def index():
    '''User can enter screen name, can add channels and shows list of channels'''
    if request.method == 'POST':
        if 'name' in request.form:
            session['name'] = request.form['name']
        if 'new_channel' in request.form:
            # Create a new channel
            new_channel = request.form['new_channel']
            messages[new_channel] = Queue(maxsize=100)
            channel_list.append(new_channel)
        
        # Redirect after post
        if 'name' in session:
            return redirect(url_for('index', name=session['name'], channels=channel_list))
        else:
            return redirect(url_for('index', channels=channel_list))
    # GET requests
    else:
        if 'name' in session:
            return render_template('index.html', name=session['name'], channels=channel_list)
        else:
            return render_template('index.html', channels=channel_list)


@app.route("/channels/<channel_name>", methods=['GET', 'POST'])
def channel(channel_name):
    '''Shows messages in the channel'''
    if request.method == 'POST':
        # A formatted message includes message, time, and name
        now = datetime.now()
        formatted_now = now.strftime("%d/%m/%Y %H:%M")
        new_message = (request.form['message'], formatted_now, session['name'])

        # Pop a message if queue gets full
        if messages[channel_name].full():
            messages[channel_name].get()

        messages[channel_name].put(new_message)

        return redirect(url_for('channel', channel_name=channel_name, messages=messages[channel_name].queue))

    return render_template('channel.html', channel_name=channel_name, messages=messages[channel_name].queue)


# @app.route('/leave')
# def leave():
#     # remove the name from the session if it's there
#     session.pop('name', None)
#     return redirect(url_for('index'))

@socketio.on("send message")
def chat(data):
    data['name'] = session['name']
    emit("receive message", data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)