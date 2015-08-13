import os
import sys
import tty
import importlib
import modes
import utilities

# Holds all grammar rules that the interpreter will use.
MODE_GRAMMAR = {}

def load_grammars():
    """
    Loads each compiled grammar from the subdirectories of the grammars
    directory.
    """
    grammars = {}
    directories = utilities.child_directories("grammars")
    for directory in directories:
        print("Loading grammar: '" + directory + "'")
        module = ".".join(["grammars", directory, "grammar_compiled"])
        grammar = importlib.import_module(module)
        grammars[directory] = grammar.grammar

    return grammars

def set_mode(mode, grammars):
    """
    Populates MODE_GRAMMARS with each grammar specified by the mode.
    """
    global MODE_GRAMMAR
    if mode in modes.modes:
        MODE_GRAMMAR.clear()
        # The list of grammars which make up this mode.
        mode_grammars = modes.modes[mode]
        for grammar in mode_grammars:
            # Add the rules from the grammar to MODE_GRAMMAR.
            MODE_GRAMMAR.update(grammars[grammar])
    else:
        print("Unrecognized mode: " + mode)

def read_input():
    """
    Reads continuously from standard input and looks up the input in the
    MODE_GRAMMAR dictionary.
    """
    fileno = sys.stdin.fileno()
    tty.setraw(fileno)
    while 1:
        data = os.read(0, 1024).lower()
        if data in MODE_GRAMMAR:
            os.system("tmux send-keys " + MODE_GRAMMAR[data])
            print(data + " -> " + MODE_GRAMMAR[data])
        else:
            print("Unrecognized rule: " + data)

def interpret():
    grammars = load_grammars()
    set_mode("python", grammars)
    read_input()
