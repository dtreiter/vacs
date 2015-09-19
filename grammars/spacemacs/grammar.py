from functions import *

def leader(keys):
    return "<alt>M" + keys


grammar = {
    "shell": "shell",
    "shelf": "shell",
    "cell": "shell",
    "sell": "shell",
    "show": "shell",
    "she'll": "shell",
    "shall": "shell",
    "okay": "fd",
    "reload": ":e!",
    "persist": leader("fs"),
    "persists": leader("fs"),
    "process": leader("fs"),
    "processed": leader("fs"),
    "switch": leader("bb"),
    "search": leader("ss"),
    "frame": leader("wo"),
    "lip": leader("ww"),
    "flip": leader("ww"),
    "flipped": leader("ww"),
    "slip": leader("ww"),
    "flick": leader("ww"),
    "viewing": leader("bv"),
    "helm": leader(":"),
    "home": leader(":"),
    "compile": leader("cC") + "<enter>",
    "status": leader("gs"),
    "difference": leader("gd"),
    "committing": leader("gh")
}
