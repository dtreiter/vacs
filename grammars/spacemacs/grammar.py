from functions import *

import config

def escape(keys):
    if config.CONNECTION_TYPE == "tmux":
        # When using tmux, keypresses can occur so quickly that Emacs
        # experiences problems. So instead we rely on mapping f10 to
        # evil-force-normal-state.
        return "<f10>" + keys
    else:
        return "<esc>" + keys

def leader(keys):
    return "<alt>M" + keys


grammar = {
    "above": escape("O"),
    "after": "a",
    "again": ";",
    "alter": "ciw",
    "below": escape("o"),
    "beginning": "gg",
    "bottom": "G",
    "buffer": "<ctrl>xh",
    "center": "zz",
    "copy": "yy",
    "evaluate": "<alt>:",
    "jam": escape("I"),
    "jerk": escape("A"),
    "jump": jump,
    "merge": "J",
    "okay": escape(""),
    "previous": "''",
    "inside": "vi",
    "trim": escape("$x"),
    "reload": ":e!",
    "reformat": "<alt>q",
    "repeat": "@q",
    "replace": ":s/",
    "reselect": "gv",
    "retry": "<ctrl>_",
    "remove": "dd",
    "scratch": "<ctrl>x<backspace>",
    "shell": "shell",
    "snippet": "snippet",
    "surround": "s",
    "top": "zt",
    "undo": "<ctrl>_",
    "until": "t",
    "visual": "V",

    "column": leader("wv"),
    "committing": leader("gh"),
    "compile": leader("cC") + "<enter>",
    "configuration": leader("fed"),
    "difference": leader("gd"),
    "flip": leader("ww"),
    "frame": leader("wo"),
    "helm": leader(":"),
    "home": leader(":"),
    "maximize": leader("wm"),
    "open": leader("ff"),
    "other": leader("<tab>"),
    "persist": leader("fs"),
    "project": leader("/") + "<ctrl>x<backspace>",
    "register": leader("yr"),
    "reinitialize": leader("yi"),
    "save": leader("fs"),
    "search": leader("ss"),
    "store": "viw" + leader("yr"),
    "next": leader("yn"),
    "rotate": leader("wR"),
    "status": leader("gs"),
    "switch": leader("bb"),
    "viewing": leader("bv")
}
