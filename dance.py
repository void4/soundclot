from flask import Flask, render_template, session
from flask_socketio import SocketIO, emit

from tracks import getCurrentTrack

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

uid = 0

def getUID():
    global uid
    uid += 1
    return uid

@socketio.on('connect')
def test_connect():
    print("Client connected")
    session["uid"] = getUID()

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')
    send("logout", {"uid":session["uid"]}, broadcast=True)

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)

def send(typ, data, *args, **kwargs):
    print("sending", typ, data)
    emit("json", {"type":typ, "data":data}, *args, **kwargs)

@socketio.on('json')
def handle_json(json):
    print('received json: ' + str(json))
    typ, data = json["type"], json["data"]

    if typ == "user":
        send("user", {"uid":session["uid"], "x":data["x"], "y":data["y"]}, broadcast=True, include_self=False)
    elif typ == "sync":
        index, millis = getCurrentTrack()
        send("seek", {"index":index, "millis":millis})

if __name__ == '__main__':
    socketio.run(app, port=1338)
