import importlib

VERBOSE = False
Parser = None
Interpreter = None

def set_connection(connection_type):
    global Parser, Interpreter
    if connection_type == "vbox":
        Parser = getattr(importlib.import_module("parsers.vbox"), "VboxParser")
        Interpreter = getattr(importlib.import_module("interpreters.vbox"), "VboxInterpreter")
    elif connection_type == "tmux":
        Parser = getattr(importlib.import_module("parsers.tmux"), "TmuxParser")
        Interpreter = getattr(importlib.import_module("interpreters.tmux"), "TmuxInterpreter")

