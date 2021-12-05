import Worker from "workerize-loader!./worker.ts"; // eslint-disable-line import/no-webpack-loader-syntax

const webSocketAddress = "ws://localhost:7700";
for (let i = 0; i < 2; i++) {
  const worker = new Worker();
  worker.onerror = console.error;
  worker.onmessage = console.log;

  worker.execute(
    i,
    `
  from js import WebSocket, console
  import marshal, types
  import json
  import base64

  socket = WebSocket.new('${webSocketAddress}')

  map_function = None
  def set_map_function(code: str):
    global map_function
    code = marshal.loads(base64.b64decode(code))
    map_function = types.FunctionType(code, globals(), "map_function")
    print(map_function(12))

  def handle_message(event):
    message = json.loads(event.data)
    print(message)
    {
      "function": set_map_function
    }[message['type']](message['value'])

    
 
  socket.addEventListener('open', lambda event: socket.send('Hello Server!'))
  socket.addEventListener('message', handle_message)

  
    `
  );
}

export const executePython = async (script: string) => {
  /*return new Promise(function (onSuccess, onError) {
    run(script, context, onSuccess, onError);
  });*/
};
