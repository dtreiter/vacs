from core import BaseParser

SHIFT_SYMBOLS = {
    "_": "-",
    "+": "=",
    "{": "[",
    "}": "]",
    ":": ";",
    "quote": "'",
    "~": "`",
    "|": "\\",
    "lbracket": ",",
    "rbracket": ".",
    "?": "/",
    "!": "1",
    "@": "2",
    "#": "3",
    "$": "4",
    "%": "5",
    "^": "6",
    "&": "7",
    "*": "8",
    "(": "9",
    ")": "0"
}

MODIFIER_SCANCODES = {
    "ctrl": "29",
    "alt": "56",
    "shift": "42"
}

SCANCODES = {
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
    "bspace": 14,
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
    "'": 40,
    "`": 41,
    "shift": 42,
    "backslash": 43,
    "z": 44,
    "x": 45,
    "c": 46,
    "v": 47,
    "b": 48,
    "n": 49,
    "m": 50,
    ",": 51,
    ".": 52,
    "/": 53,
    "rshift": 54,
    "ptscr": 55,
    "alt": 56,
    " ": 57,
    "cpslk": 58,
    "f1": 59,
    "f2": 60,
    "up": 72,
    "left": 75,
    "right": 77,
    "down": 80
}

class VboxParser(BaseParser):
    @classmethod
    def parse_token(cls, token):
        if callable(token["symbol"]):
            return token["symbol"]

        cls.normalize_shift(token)
        scancodes = cls.get_scancodes(token)
        return scancodes

    @classmethod
    def normalize_shift(cls, token):
        """
        Converts a symbol which requires the shift key to a plain symbol with
        the shift modifier.

        For example:
        : -> <shift>;
        """
        if token["symbol"] in SHIFT_SYMBOLS:
            token["modifiers"].append("shift")
            token["symbol"] = SHIFT_SYMBOLS[token["symbol"]]
        elif token["symbol"].istitle():
            token["modifiers"].append("shift")
            token["symbol"] = token["symbol"].lower()

    @classmethod
    def get_modifier_keydowns(cls, token):
        keydowns = []
        for modifier in token["modifiers"]:
            keydowns.append(cls.keydown(MODIFIER_SCANCODES[modifier]))

        return keydowns

    @classmethod
    def get_modifier_keyups(cls, token):
        keyups = []
        for modifier in token["modifiers"]:
            keyups.append(cls.keyup(MODIFIER_SCANCODES[modifier]))

        return keyups

    @classmethod
    def get_scancodes(cls, token):
        if token["symbol"] in SCANCODES:
            code = SCANCODES[token["symbol"]]
            scancodes = []
            scancodes.extend(cls.get_modifier_keydowns(token))
            scancodes.extend([cls.keydown(code), cls.keyup(code)])
            scancodes.extend(cls.get_modifier_keyups(token))
            return " ".join(scancodes)
        else:
            print("ERROR: Symbol '" + token["symbol"] + "' not in scan codes list.")
            return "" # TODO Should maybe throw exception?

    @classmethod
    def keydown(cls, code):
        return format(int(code), "02x")

    @classmethod
    def keyup(cls, code):
        return format(int(code) + 128, "02x")

    @classmethod
    def parse_string(cls, string):
        tokens = []
        for letter in list(string):
            tokens.append({
                "modifiers": [],
                "symbol": letter
            })

        return cls.parse_tokens(tokens)
