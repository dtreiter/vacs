import globals
import modes
import utilities

def log(text):
    utilities.log(text)

def reload_grammars():
    log("Reloading grammars and aliases.")
    globals.Interpreter.reinitialize()
    log("Reloading complete.")

def set_mode(mode):
    if mode in modes.modes:
        log("Switching mode to: '" + mode + "'")
        globals.Interpreter.set_mode(mode)
    else:
        log("Unrecognized mode: '" + str(mode) + "'")

def get_target():
    return globals.TARGET_TYPE
