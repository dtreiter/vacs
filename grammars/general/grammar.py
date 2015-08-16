from functions import *

grammar = {
    # Symbols
    "-": "-",
    "hyphen": "-",
    "_": "_",
    "underscore": "_",
    "parentheses": "(",
    "smile": ")",
    "brace": "[",
    "bruce": "[",
    "square": "]",
    "currently": "{",
    "curly": "{",
    "girlie": "{",
    "girly": "{",
    "squiggle": "}",
    "bracket": "<",
    "knows": ">",
    "nose": ">",
    "*": "*",
    "~": "~",
    "`": "`",
    "bang": "!",
    "at": "@",
    "pound": "#",
    "dollar": "$",
    "percent": "%",
    "^": "^",
    "carrot": "^",
    "caret": "^",
    "&": "&",
    "ampersand": "&",
    "star": "*",
    "flower": "*",
    "question": "?",
    "space": " ",
    ",": ",",
    ":": ":",
    ";": ";",
    "period": ".",
    "case": ".",
    "base": ".",
    "ace": ".",
    "quote": "<quote>",
    "quotes": "<quote>",
    "smack": "<quote>",
    "snack": "<quote>",
    "mac": "<quote>",
    "smudge": "'",
    "/": "/",
    "search": "/",
    "peanut": "<backslash>",

    # Control characters
    "multiplex": "<ctrl>a",
    "trash": "<ctrl>c",
    "quit": "<ctrl>g",
    "backspace": "<ctrl>h",
    "complete": "<ctrl>n",
    "insert": "<ctrl>r",
    "window": "<ctrl>w",
    "extend": "<ctrl>x",
    "escape": "<esc>",
    "undo": "<ctrl>_",
    "tab": "<tab>",
    "turn": "<tab>",
    "turned": "<tab>",
    "enter": "<enter>",
    "yes": "<enter>",
    "yeah": "<enter>",

    # Alphabet corrections
    "hey": "a",
    "be": "b",
    "bee": "b",
    "see": "c",
    "egg": "e",
    "eat": "e",
    "find": "f",
    "fine": "f",
    "joe": "j",
    "top": "<up>",
    "talk": "<up>",
    "down": "<down>",
    "right": "<right>",
    "wright": "<right>",
    "write": "<right>",
    "left": "<left>",

    # Phonetic alphabet that using names
    "albert" : "a",
    "bob" : "b",
    "bill" : "b",
    "carol" : "c",
    "carroll" : "c",
    "caroll" : "c",
    "cici": "cc",
    "daniel" : "d",
    "dede": "dd",
    "didi": "dd",
    "edward" : "e",
    "frederick" : "f",
    "gary" : "g",
    "garry" : "g",
    "gerry" : "g",
    "gigi": "gg",
    "gege": "gg",
    "gerald": "G",
    "jerald": "G",
    "howard" : "h",
    "high": "i",
    "hi": "i",
    "eye": "i",
    "ireland" : "I",
    "jeffrey" : "j",
    "christine" : "k",
    "larry" : "l",
    "mark" : "m",
    "nancy" : "n",
    "oscar" : "o",
    "patrick" : "p",
    "quick" : "q",
    "robert" : "r",
    "sarah" : "s",
    "thomas" : "t",
    "ultimate" : "u",
    "umbrella": "U",
    "valerie" : "v",
    "william" : "w",
    "javier" : "x",
    "text" : "x",
    "yolanda" : "y",
    "yankee": "y",
    "huewai": "yy",
    "wife": "y",
    "zebra" : "z",
    "sibra" : "z",
    "zipper": "z",
    "in": "n",
    "oh": "o",
    "paste": "p",
    "pope": "p",
    "are": "r",
    "you": "u",
    "the": "v",
    "visual": "V",
    "visible": "V",
    "why": "y",

    # Numbers
    "zero": "0",
    "one": "1",
    "two": "2",
    "to": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",

    # General
    "trace": "()<left>",
    "string": "<quote><quote><left>",
    "compare": " == ",
    "equals": " = ",
    "plus": " + ",
    "increment": " += ",
    "increments": " += ",
    "clap": ":",
    "clapp": ":",
    "minus": " - ",

    "lower": lowercase
}
