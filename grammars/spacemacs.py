import grammar_utilities

def escape(keys):
    if grammar_utilities.get_target() == "tmux":
        # When using tmux, keypresses can occur so quickly that Emacs
        # experiences problems. So instead we rely on mapping f10 to
        # evil-force-normal-state.
        return "<f10>" + keys
    else:
        return "<esc>" + keys

def leader(keys):
    return "<alt>m" + keys

def jump(text):
    if text.isdigit():
        return text + "gg"
    else:
        utilities.log("ERROR: Non-digit argument provided to jump function")
        return ""

def correct(text):
    return escape("0/" + text + "<enter>")

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
    "correct": correct,
    "done": escape(leader("fs")),
    "drawer": leader("ft"),
    "evaluate": "<alt>:",
    "exit": "q",
    "highlight": leader("sc"),
    "jam": escape("I"),
    "jerk": escape("A"),
    "jump": jump,
    "leader": "<alt>m",
    "merge": "J",
    "next": "<ctrl>e",
    "okay": escape(""),
    "previous": "''",
    "inside": "vi",
    "trim": escape("$x"),
    "record": "qq",
    "reformat": "<alt>q",
    "repeat": "@q",
    "replace": ":s/",
    "reselect": "gv",
    "retry": "<ctrl>_",
    "remove": "dd",
    "clear": "<ctrl>x<backspace>",
    "select": "v",
    "shell": "shell",
    "snipe": escape("0s"),
    "snippet": "snippet",
    "surround": "s",
    "test": "<ctrl>ao<up><enter>",
    "top": "zt",
    "undo": "<ctrl>_",
    "until": "t",
    "uppercase": "U",
    "visual": "V",
    "word": "w",
    "example": "<shift><tab>",

    "first": "<down><enter>",
    "second": "<down><down><enter>",
    "third": "<down><down><down><enter>",
    "fourth": "<down><down><down><down><enter>",

    "archive": leader("gsll"),
    "completion": leader("ta"),
    "column": leader("wv"),
    "commit": leader("gscc"),
    "committing": leader("gsds"),
    "compile": leader("cC") + "<enter>",
    "configuration": leader("fed"),
    "describe": leader("hdk"),
    "difference": leader("gsdu"),
    "flip": leader("ww"),
    "frame": leader("wo"),
    "helm": leader(":"),
    "home": leader(":"),
    "line": "<ctrl>q", # For selecting Helm lines
    "maximize": leader("wm"),
    "open": leader("ff"),
    "other": leader("<tab>"),
    "persist": leader("fs"),
    "project": leader("pf"),
    "register": leader("yr"),
    "reconfigure": leader("yi"),
    "reload": leader("fn"),
    "save": leader("fs"),
    "search": leader("ss"),
    "store": "viw" + leader("yr"),
    "relative": leader("tr"),
    "rotate": leader("wR"),
    "status": leader("gs"),
    "switch": leader("bb"),
    "viewing": leader("bv")
}
