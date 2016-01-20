import config
import modes
import utilities

def log(text):
    utilities.log(text)

def reload_grammars():
    log("Reloading grammars and aliases.")
    config.Interpreter.reinitialize()
    log("Reloading complete.")

def set_mode(mode):
    if mode in modes.modes:
        log("Switching mode to: '" + mode + "'")
        config.Interpreter.set_mode(mode)
    else:
        log("Unrecognized mode: '" + str(mode) + "'")
