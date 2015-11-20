from functions import *

import config

def escape(keys):
    if config.CONNECTION_TYPE == "tmux":
        # When using tmux, keypresses can occur so quickly that Emacs
        # experiences problems. So instead we rely on spacemacs' evil-escape key
        # sequence.
        return "<f10>" + keys
    else:
        return "<esc>" + keys

def leader(keys):
    return "<alt>M" + keys


grammar = {
    "above": escape("O"),
    "alter": "ciw",
    "below": escape("o"),
    "beginning": "gg",
    "bottom": "G",
    "buffer": "<ctrl>xh",
    "center": "zz",
    "copy": "yy",
    "evaluate": "<alt>:",
    "jerk": escape("A"),
    "okay": "<esc>",
    "okay": escape(""),
    "inside": "vi",
    "trim": escape("$x"),
    "reload": ":e!",
    "reformat": "<alt>q",
    "repeat": "@q",
    "replace": ":s/",
    "reselect": "gv",
    "remove": "dd",
    "scratch": "<ctrl>x<backspace>",
    "shell": "shell",
    "snippet": "snippet",
    "undo": "<ctrl>_",

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
    "project": leader("/"),
    "register": leader("yr"),
    "reinitialize": leader("yi"),
    "search": leader("ss"),
    "store": "viw" + leader("yr"),
    "next": leader("yn"),
    "rotate": leader("wR"),
    "status": leader("gs"),
    "switch": leader("bb"),
    "viewing": leader("bv")
}
