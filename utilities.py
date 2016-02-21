import os
import glob
import importlib

import globals

def set_target(target_type, target_name):
    """
    Imports the compiler and interpreter corresponding to the target.
    """
    globals.TARGET_NAME = target_name
    if target_type == "vbox":
        globals.TARGET_TYPE = "vbox"
        globals.Compiler = import_attribute("compilers.vbox", "VboxCompiler")
        Interpreter = import_attribute("interpreters.vbox", "VboxInterpreter")
    elif target_type == "tmux":
        globals.TARGET_TYPE = "tmux"
        globals.Compiler = import_attribute("compilers.tmux", "TmuxCompiler")
        Interpreter = import_attribute("interpreters.tmux", "TmuxInterpreter")

    # Instantiate the interpreter.
    globals.Interpreter = Interpreter()

def set_verbose(is_verbose):
    globals.VERBOSE = is_verbose

def log(string, verbose=False):
    """
    Prints the string followed by a '\r', which is necessary when the terminal is
    in the raw mode.
    """
    if (not verbose) or (verbose and globals.VERBOSE):
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
