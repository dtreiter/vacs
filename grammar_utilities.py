import config
import utilities

def log(text):
    utilities.log(text)

# TODO This function does not need to take any arguments or return anything.
# Revisit when this is been accounted for in the interpreter.
def reload_grammars(text):
    log("Reloading grammars and aliases.")
    config.Interpreter.reinitialize()
    log("Reloading complete.")
    return " "

def set_mode(mode):
    config.Interpreter.set_mode(mode)
