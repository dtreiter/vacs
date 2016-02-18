import config
import utilities

def escape(keys):
    if config.TARGET_TYPE == "tmux":
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
    "done": escape(leader("fs")),
    "evaluate": "<alt>:",
    "jam": escape("I"),
    "jerk": escape("A"),
    "jump": jump,
    "merge": "J",
    "next": "<ctrl>e",
    "okay": escape(""),
    "previous": "''",
    "inside": "vi",
    "trim": escape("$x"),
    "record": "qq",
    "reload": ":e!",
    "reformat": "<alt>q",
    "repeat": "@q",
    "replace": ":s/",
    "reselect": "gv",
    "retry": "<ctrl>_",
    "remove": "dd",
    "clear": "<ctrl>x<backspace>",
    "select": "v",
    "shell": "shell",
    "snippet": "snippet",
    "surround": "s",
    "test": "<ctrl>ao<up><enter>",
    "top": "zt",
    "undo": "<ctrl>_",
    "until": "t",
    "uppercase": "U",
    "visual": "V",
    "word": "w",
    # "example": "<shift><tab>",

    "first": "<down><enter>",
    "second": "<down><down><enter>",
    "third": "<down><down><down><enter>",
    "fourth": "<down><down><down><down><enter>",

    "completion": leader("ta"),
    "column": leader("wv"),
    "commit": leader("gcc"),
    "committing": leader("gds"),
    "compile": leader("cC") + "<enter>",
    "configuration": leader("fed"),
    "describe": leader("hdk"),
    "difference": leader("gdu"),
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
    "reconfigure": leader("yi"),
    "save": leader("fs"),
    "search": leader("ss"),
    "store": "viw" + leader("yr"),
    "relative": leader("tr"),
    "rotate": leader("wR"),
    "status": leader("gs"),
    "switch": leader("bb"),
    "viewing": leader("bv")
}
