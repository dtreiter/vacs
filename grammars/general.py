def lowercase(text):
    return text.lower()

def uppercase(text):
    return text.upper()

def capitalcase(text):
    return ''.join(letter for letter in text.title() if letter.isalpha())

def camelcase(text):
    output = ''.join(letter for letter in text.title() if letter.isalpha())
    return output[0].lower() + output[1:]

def spinecase(text):
    return "-".join(text.lower().split(" "))

def titlecase(text):
    return text[0].upper() + text[1:]

def dotcase(text):
    return ".".join(text.lower().split(" "))

def nospaces(text):
    return "".join(text.lower().split(" "))

def snakecase(text):
    return "_".join(text.lower().split(" "))


grammar = {
    # Symbols
    "-": "-",
    "hyphen": "-",
    "_": "_",
    "underscore": "_",
    "parentheses": "(",
    "smile": ")",
    "brace": "[",
    "square": "]",
    "curly": "{",
    "squiggle": "}",
    "bracket": "<lbracket>",
    "nose": "<rbracket>",
    "*": "*",
    "~": "~",
    "squish": "~",
    "`": "`",
    "pipe": "|",
    "|": "|",
    "bang": "!",
    "at": "@",
    "pound": "#",
    "dollar": "$",
    "percent": "%",
    "^": "^",
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
    "dot": ".",
    "case": ".",
    "quote": "<quote>",
    "\\\"": "<quote>",
    "smack": "<quote>",
    "smudge": "'",
    "/": "/",
    "peanut": "<backslash>",

    # Control characters
    "multiplex": "<ctrl>a",
    "quit": "<ctrl>g",
    "complete": "<ctrl>n",
    "insert": "<ctrl>r",
    "extend": "<ctrl>x",
    "escape": "<esc>",
    "backspace": "<backspace>",
    "scrub": "<backspace>",
    "scroll": "<pgup>",
    "page": "<pgdn>",
    "tab": "<tab>",
    "turn": "<tab>",
    "enter": "<enter>",
    "yes": "<enter>",
    "yeah": "<enter>",

    # Alphabet
    " ": " ",
    "a": "a",
    "b": "b",
    "c": "c",
    "cc": "cc",
    "d": "d",
    "dd": "dd",
    "e": "e",
    "f": "f",
    "g": "g",
    "gg": "gg",
    "h": "h",
    "i": "i",
    "j": "j",
    "k": "k",
    "l": "l",
    "m": "m",
    "n": "n",
    "o": "o",
    "p": "p",
    "q": "q",
    "r": "r",
    "s": "s",
    "t": "t",
    "u": "u",
    "v": "v",
    "w": "w",
    "x": "x",
    "y": "y",
    "yy": "yy",
    "z": "z",

    "find": "f",
    "up": "<up>",
    "down": "<down>",
    "down-down": "<down><down>",
    "right": "<right>",
    "left": "<left>",

    # Phonetic alphabet that using names
    "albert" : "a",
    "bill" : "b",
    "carol" : "c",
    "daniel" : "d",
    "edward" : "e",
    "frederick" : "f",
    "gary" : "g",
    "howard" : "h",
    "jeffrey" : "j",
    "christine" : "k",
    "larry" : "l",
    "mark" : "m",
    "nancy" : "n",
    "oscar" : "o",
    "patrick" : "p",
    "robert" : "r",
    "sarah" : "s",
    "thomas" : "t",
    "ultimate" : "u",
    "valerie" : "v",
    "william" : "w",
    "text" : "x",
    "yankee": "y",
    "zebra" : "z",
    "zipper": "z",
    "paste": "p",
    "the": "v",

    # Capital letters
    "alvin": "A",
    "blake": "B",
    "charlie": "C",
    "devon": "D",
    "devin": "D",
    "elsie": "E",
    "flanders": "F",
    "gerald": "G",
    "jerald": "G",
    "ireland" : "I",
    "orbit": "O",
    "dorbett": "O",
    "umbrella": "U",

    # Control letters
    "august": "<ctrl>a",
    "billy": "<ctrl>b",
    "charles": "<ctrl>c",
    "dillan": "<ctrl>d",
    "eddie": "<ctrl>e",
    "philip": "<ctrl>f",
    "george": "<ctrl>g",
    "hannah": "<ctrl>h",
    "isaac": "<ctrl>i",
    "john": "<ctrl>j",
    "carl": "<ctrl>k",
    "lance": "<ctrl>l",
    "michael": "<ctrl>m",
    "newman": "<ctrl>n",
    "omar": "<ctrl>o",
    "pedro": "<ctrl>p",
    "quillan": "<ctrl>q",
    "ralph": "<ctrl>r",
    "steven": "<ctrl>s",
    "tom": "<ctrl>t",
    "utah": "<ctrl>u",
    "vladimir": "<ctrl>v",
    "walter": "<ctrl>w",
    "jagger": "<ctrl>x",
    "jarvis": "<ctrl>y",
    "spencer": "<ctrl>z",

    # Numbers
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",

    # General
    "trace": "()<left>",
    "array": "[]<left>",
    "list": "{}<left>",
    "tag": "<lbracket><rbracket><left>",
    "string": "<quote><quote><left>",
    "compare": " == ",
    "equals": " = ",
    "plus": " + ",
    "multiply": " * ",
    "divide": " / ",
    "increment": " += ",
    "clap": ":",
    "minus": " - ",
    "modulo": " % ",
    "entry": ", ",
    "less": " <lbracket> ",
    "greater": " <rbracket> ",

    "lower": lowercase,
    "upper": uppercase,
    "camel": camelcase,
    "capital": capitalcase,
    "spine": spinecase,
    "say": titlecase,
    "property": dotcase,
    "joint": nospaces,
    "join": nospaces,
    "spell": nospaces,
    "snake": snakecase
}