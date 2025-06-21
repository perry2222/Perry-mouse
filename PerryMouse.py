from flask import Flask
from flask_socketio import SocketIO
from pynput.mouse import Controller, Button

app = Flask(__name__, static_folder='static')
socketio = SocketIO(app, cors_allowed_origins='*')
mouse = Controller()

@app.route("/")
def index():
    return app.send_static_file("index.html")

@socketio.on("move")
def on_move(data):
    mouse.move(data["dx"], data["dy"])

@socketio.on("click")
def on_click(data):
    if data["button"] == "left":
        mouse.click(Button.left, 1)
    elif data["button"] == "right":
        mouse.click(Button.right, 1)

@socketio.on("scroll")
def on_scroll(data):
    mouse.scroll(0, data["dy"])

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
