from functions import *

def leader(keys):
    return "<alt>M" + keys


grammar = {
    "evaluate": "<alt>:",
    "jerk": "<esc>A",
    "reload": ":e!",
    "shell": "shell",
    "snippet": "snippet",
    "undo": "<ctrl>_",

    "committing": leader("gh"),
    "compile": leader("cC") + "<enter>",
    "difference": leader("gd"),
    "flip": leader("ww"),
    "frame": leader("wo"),
    "helm": leader(":"),
    "home": leader(":"),
    "open": leader("ff"),
    "persist": leader("fs"),
    "reinitialize": leader("yi"),
    "search": leader("ss"),
    "slap": leader("yn"),
    "status": leader("gs"),
    "switch": leader("bb"),
    "viewing": leader("bv")
}
