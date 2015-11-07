from functions import *

def leader(keys):
    return "<alt>M" + keys


grammar = {
    "alter": "ciw",
    "center": "zz",
    "evaluate": "<alt>:",
    "store": "viw" + leader("yr"),
    "jerk": "<esc>A",
    "above": "<esc>O",
    "below": "<esc>o",
    "inside": "vi",
    "trim": "<esc>$x",
    "reload": ":e!",
    "reformat": "<alt>q",
    "remove": "dd",
    "scratch": "<ctrl>x<bspace>",
    "shell": "shell",
    "snippet": "snippet",
    "undo": "<ctrl>_",

    "column": leader("wv"),
    "committing": leader("gh"),
    "compile": leader("cC") + "<enter>",
    "difference": leader("gd"),
    "flip": leader("ww"),
    "frame": leader("wo"),
    "helm": leader(":"),
    "home": leader(":"),
    "maximize": leader("wm"),
    "open": leader("ff"),
    "other": leader("<tab>"),
    "persist": leader("fs"),
    "project": leader("/"),
    "register": leader("yr"),
    "reinitialize": leader("yi"),
    "search": leader("ss"),
    "next": leader("yn"),
    "rotate": leader("wR"),
    "status": leader("gs"),
    "switch": leader("bb"),
    "viewing": leader("bv")
}
