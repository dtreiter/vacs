import os
import glob
import importlib

import config

def set_connection(connection_type):
    """
    Imports the parser and interpreter corresponding to connection_type.
    """
    if connection_type == "vbox":
        config.CONNECTION_TYPE = "vbox"
        config.Parser = import_attribute("parsers.vbox", "VboxParser")
        config.Interpreter = import_attribute("interpreters.vbox", "VboxInterpreter")
    elif connection_type == "tmux":
        config.CONNECTION_TYPE = "tmux"
        config.Parser = import_attribute("parsers.tmux", "TmuxParser")
        config.Interpreter = import_attribute("interpreters.tmux", "TmuxInterpreter")

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

def dump_grammar(grammar, output_file):
    """
    Writes a given grammar dictionary to output_file as a human readable dictionary.
    """
    dump = "from functions import *\n"
    dump += "grammar = {\n"
    for key in grammar:
        if callable(grammar[key]):
            value = grammar[key].__name__
        else:
            value = "\"" + grammar[key] + "\""
        dump += "    \"" + key + "\": " + value + ",\n"

    # Remove trailing comma
    dump = dump[:-2]
    dump += "\n}"
    output_file.write(dump)

def dump_aliases(aliases, output_file):
    """
    Writes a given alias mapping to output_file as a human readable dictionary.
    """
    dump = "aliases = {\n"
    for key in aliases:
        dump += "    \"" + key + "\": \"" + aliases[key] + "\",\n"

    # Remove trailing comma
    dump = dump[:-2]
    dump += "\n}"
    output_file.write(dump)

def create_grammar(grammar_name):
    pass
