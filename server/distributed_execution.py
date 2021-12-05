from typing import Any, Callable, Iterable, List
import logging
from tqdm import tqdm as tqdm_regular
from tqdm.notebook import tqdm_notebook
import marshal
import json
from time import sleep
from threading import Thread
from websocket_server import WebsocketServer
logger = logging.getLogger('DistributedExecution')
import base64


def is_in_notebook() -> bool:
    try:
        get_ipython()
        return True
    except NameError:
        return False


tqdm = tqdm_notebook if is_in_notebook() else tqdm_regular




class DistributedExecution:
    def __init__(self, port=7700):
        self._server = WebsocketServer(host='0.0.0.0', port=port, loglevel=logging.INFO)
        self._tasks = {}
        self._server.set_fn_new_client(self._on_new_client)

        logger.info(f'Created')
        self._map_function = None

    def map(
        self,
        function: Callable[[Any], Any],
        values: Iterable[Any],
        chunk_size=1,
    ) -> List[Any]:
        self._map_function = function
        thread = Thread(target =  self._server.serve_forever)
        thread.start()
        print("start")

        self._server.send_message_to_all(self._serialize_function(function))

        values = list(values)
        sleep(1000)
        self._map_function = None

        return list(map(function, values))


    @staticmethod
    def _serialize_function(function: Callable[[Any], Any]) -> str:
        print(marshal.dumps(function.__code__))
        return json.dumps({
            "type": "function",
            "value": base64.b64encode(marshal.dumps(function.__code__)).decode('utf-8')
        })

    def _on_new_client(self, client, server):
        if self._map_function:
            print("sent")
            
            server.send_message(client, self._serialize_function(self._map_function))

        print("hi")
        print(client)

    def __enter__(self):
        logger.info(f'Initiated')
        return self

    def __exit__(self, type, value, traceback):
        self._server.shutdown_gracefully()
        logger.info(f'Destroyed')
