from js import WebSocket, webSocketAddress, onFinished
import pickle
import json
import base64
from typing import Any
from time import sleep

import micropip
await micropip.install('cloudpickle')

!!INSTALL_DEPENDENCIES!!

map_function = None
def set_map_function(code: str):
    global map_function
    map_function = pickle.loads(base64.b64decode(code))

def execute_map(data: str) -> Any:
    decoded_data = pickle.loads(base64.b64decode(data))
    result = map_function(decoded_data)
    encoded_result = base64.b64encode(pickle.dumps(result)).decode('utf-8')
    socket.send(json.dumps({"type": "result", "value": encoded_result}))
    onFinished()


def handle_message(event):
    message = json.loads(event.data)
    {
        "function": set_map_function,
        "data": execute_map,
    }[message['type']](message['value'])


socket = WebSocket.new(webSocketAddress)
socket.addEventListener('open', lambda _: socket.send(json.dumps({"type": "ready", "value": None})))
socket.addEventListener('message', handle_message)