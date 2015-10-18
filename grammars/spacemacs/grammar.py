from functions import *

def leader(keys):
    return "<alt>M" + keys


grammar = {
    "alter": "ciw",
    "center": "zz",
    "evaluate": "<alt>:",
    "jerk": "<esc>A",
    "beep": "<esc>o",
    "reload": ":e!",
    "reformat": "<alt>q",
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
    "other": leader("<tab>"),
    "persist": leader("fs"),
    "reinitialize": leader("yi"),
    "search": leader("ss"),
    "next": leader("yn"),
    "status": leader("gs"),
    "switch": leader("bb"),
    "viewing": leader("bv")
}
