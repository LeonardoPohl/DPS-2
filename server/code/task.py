from typing import Callable


class Task:
  def __init__(self, function: Callable[[_T], _S], iteratable: Iterable[_T]):
    self.func = function
    self.iter = iteratable

  def __enter__(self):
    # Pickle Function, start up server, define Url .. 
    code_string = marshal.dumps(self.func.__code__)
    print(code_string)

  def __exit__(self, type, value, traceback):
    # Collect all threads check status
    pass