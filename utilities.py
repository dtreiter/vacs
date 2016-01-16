import os
import glob
import importlib

import config

def set_connection(connection_type, connection_name):
    """
    Imports the parser and interpreter corresponding to connection_type.
    """
    config.CONNECTION_NAME = connection_name
    if connection_type == "vbox":
        config.CONNECTION_TYPE = "vbox"
        config.Parser = import_attribute("parsers.vbox", "VboxParser")
        Interpreter = import_attribute("interpreters.vbox", "VboxInterpreter")
    elif connection_type == "tmux":
        config.CONNECTION_TYPE = "tmux"
        config.Parser = import_attribute("parsers.tmux", "TmuxParser")
        Interpreter = import_attribute("interpreters.tmux", "TmuxInterpreter")

    # Instantiate the interpreter.
    config.Interpreter = Interpreter()

def set_verbose(is_verbose):
    config.VERBOSE = is_verbose

def log(string, verbose=False):
    """
    Prints the string followed by a '\r', which is necessary when the terminal is
    in the raw mode.
    """
    if (not verbose) or (verbose and config.VERBOSE):
        print(string + "\r")

def import_attribute(module, attribute):
    """
    Imports an attribute from a module.
    """
    return getattr(importlib.import_module(module), attribute)

def get_grammar_names():
    """
    Returns a list of every grammar name contained in the grammar directory.
    """
    modules = glob.glob("grammars/*.py")
    module_names = [os.path.basename(f)[:-3] for f in modules if os.path.isfile(f)]
    # Remove __init__.py and aliases from the list.
    ignore = ["__init__", "aliases"]
    module_names = [name for name in module_names if name not in ignore]
    return module_names
