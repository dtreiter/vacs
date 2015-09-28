from functions import *

def leader(keys):
    return "<alt>M" + keys


grammar = {
    "reload": ":e!",
    "shell": "shell",
    "undo": "<ctrl>_",

    "committing": leader("gh"),
    "compile": leader("cC") + "<enter>",
    "difference": leader("gd"),
    "flip": leader("ww"),
    "frame": leader("wo"),
    "helm": leader(":"),
    "home": leader(":"),
    "persist": leader("fs"),
    "search": leader("ss"),
    "status": leader("gs"),
    "switch": leader("bb"),
    "viewing": leader("bv")
}
