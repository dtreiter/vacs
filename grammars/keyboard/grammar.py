from functions import *

grammar = {
    " ": " ",
    "\\x7f": "<bspace>",
    "\\x0d": "<enter>",
    "\\x1b": "<esc>",
    "\\x09": "<tab>",
    "\\x1b\\x5b\\x35\\x7e": "<pgup>",
    "\\x1b\\x5b\\x36\\x7e": "<pgdn>",
    "\\x1b\\x5b\\x61": "<up>",
    "\\x1b\\x5b\\x62": "<down>",
    "\\x1b\\x5b\\x63": "<right>",
    "\\x1b\\x5b\\x64": "<left>",

    ".": ".",
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "\\\\": "<backslash>",
}
