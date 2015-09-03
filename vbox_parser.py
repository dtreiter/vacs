import parser

def parse_token(token):
    if callable(token["symbol"]):
        return token["symbol"]

    normalize_shift(token)
    scancode = get_scancode(token["symbol"])
    return scancode

def normalize_shift(token):
    """
    Converts a symbol which requires the shift key to a plain symbol with the
    shift modifier.

    For example:
      : -> <shift>;
    """
    if token["symbol"] in SHIFT_SYMBOLS:
        token["modifiers"].append("shift")
        token["symbol"] = SHIFT_SYMBOLS[token["symbol"]]
    elif token["symbol"].istitle():
        token["modifiers"].append("shift")
        token["symbol"] = token["symbol"].lower()


def get_scancode(symbol):
    if symbol in scancodes:
        keydown = scancodes[symbol]
        keyup = keydown + 128
        keystring = format(keydown, "x") + " " + format(keyup, "x")
        return keystring

    return ""


parser.parse_token = parse_token
def parse(tokenized_grammar):
    return parser.parse(tokenized_grammar)


SHIFT_SYMBOLS = {
    "_": "-",
    "+": "=",
    "{": "[",
    "]": "}",
    ":": ";",
    "\"": "'",
    "~": "`",
    "|": "\\",
    "<": ",",
    ">": ".",
    "?": "/"
}

scancodes = {
    "esc": 1,
    "1": 2,
    "2": 3,
    "3": 4,
    "4": 5,
    "5": 6,
    "6": 7,
    "7": 8,
    "8": 9,
    "9": 10,
    "0": 11,
    "-": 12,
    "=": 13,
    "bksp": 14,
    "tab": 15,
    "q": 16,
    "w": 17,
    "e": 18,
    "r": 19,
    "t": 20,
    "y": 21,
    "u": 22,
    "i": 23,
    "o": 24,
    "p": 25,
    "[": 26,
    "]": 27,
    "enter": 28,
    "ctrl": 29,
    "a": 30,
    "s": 31,
    "d": 32,
    "f": 33,
    "g": 34,
    "h": 35,
    "j": 36,
    "k": 37,
    "l": 38,
    ";": 39,
    "`": 40,
    "shift": 41,
    "backslash": 42,
    "z": 43,
    "x": 44,
    "c": 45,
    "v": 46,
    "b": 47,
    "n": 48,
    "m": 49,
    ",": 50,
    ".": 51,
    "/": 52,
    "rshift": 53,
    "ptscr": 54,
    "alt": 55,
    " ": 56,
    "cpslk": 57,
    "f1": 58,
    "f2": 59,
    #"": 60,
    #"": 61,
    #"": 62,
    #"": 63,
    #"": 64,
    #"": 65,
    #"": 66,
    #"": 67,
    #"": 68,
    #"": 69,
    #"": 70,
    #"": 71,
    "up": 72,
    #"": 73,
    #"": 74,
    "left": 75,
    #"": 76,
    "right": 77,
    #"": 78,
    #"": 79,
    "down": 80
    #"": 81,
    #"": 82,
    #"": 83,
    #"": 84,
    #"": 85,
    #"": 86,
    #"": 87,
    #"": 88,
    #"": 89,
    #"": 90,
    #"": 91,
    #"": 92,
    #"": 93,
    #"": 94,
    #"": 95,
    #"": 96,
    #"": 97,
    #"": 98,
    #"": 99,
    #"": 100,
    #"": 101,
    #"": 102,
}
