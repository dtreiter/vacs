from functions import *

def prefix(keys):
    return "<ctrl>t" + keys

def window(title):
    return prefix("'" + title + "<enter>")

def command(name):
    return prefix(";" + name + "<enter>")

grammar = {
    "window": prefix("'"),
    "applications": prefix("<quote>"),
    "destroy": prefix("k"),
    "split": prefix("S"),
    "title": command("title"),
    "refresh": window("firefox") + "<ctrl>r",
    "firefox": window("firefox"),
    "terminal": window("terminal"),
    "editor": window("emacs")
}
