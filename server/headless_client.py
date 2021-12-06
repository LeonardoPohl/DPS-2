import base64
import json
import pickle
from sys import argv
from time import sleep

import websocket

map_function = None
socket: websocket.WebSocketApp = None


def set_map_function(code: str):
    global map_function
    map_function = pickle.loads(base64.b64decode(code))


def execute_map(data):
    decoded_data = pickle.loads(base64.b64decode(data))
    result = map_function(decoded_data)
    encoded_result = base64.b64encode(pickle.dumps(result)).decode("utf-8")
    socket.send(json.dumps({"type": "result", "value": encoded_result}))


def handle_message(ws, message):
    message = json.loads(message)
    {"function": set_map_function, "data": execute_map,}[
        message["type"]
    ](message["value"])


def wait_and_start_websocket(*_):
    sleep(1)
    start_websocket()


def on_open(ws):
    ws.send(json.dumps({"type": "ready", "value": None}))


def start_websocket():
    global socket
    socket = websocket.WebSocketApp(
        websocket_url,
        on_open=on_open,
        on_message=handle_message,
        on_close=wait_and_start_websocket,
    )
    socket.run_forever()


if __name__ == "__main__":
    _, websocket_url = argv
    start_websocket()
