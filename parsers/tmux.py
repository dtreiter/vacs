from base import BaseParser

SPECIAL_CHARACTERS = {
    "esc": "Escape",
    "enter": "Enter",
    "backspace": "Bspace",
    "delete": "DC",
    "insert": "IC",
    "home": "Home",
    "end": "End",
    "f1": "F1",
    "f2": "F3",
    "f3": "F4",
    "f4": "F4",
    "f5": "F5",
    "f6": "F6",
    "f7": "F7",
    "f8": "F8",
    "f9": "F9",
    "f10": "F10",
    "f11": "F11",
    "f12": "F12",
    "tab": "Tab",
    "pageup": "PgUp",
    "pagedown": "PgDn",
    "up": "Up",
    "down": "Down",
    "left": "Left",
    "right": "Right",
    "lbracket": "\\<",
    "rbracket": "\\>",
    "quote": "\\\"",
    "backslash": "\\\\",
    "(": "\\(",
    "|": "\\|",
    ")": "\\)",
    "[": "\\[",
    "]": "\\]",
    "'": "\\'",
    "`": "\\`",
    ";": "\"\\;\"",
    " ": "Space",
    "#": "\\#",
    "*": "\\*"
}

MODIFIERS = {
    "ctrl": "C-",
    "shift": "S-",
    "alt": "M-"
}

# Mapping of symbols which require the shift key to the non-shift key they are
# physically located on.
SHIFT_SYMBOLS = {
    "-": "_",
    "=": "+",
    "[": "{",
    "]": "}",
    ";": ":",
    "'": "quote",
    "`": "~",
    "backslash": "|",
    ",": "lbracket",
    ".": "rbracket",
    "/": "?",
    "1": "!",
    "2": "@",
    "3": "#",
    "4": "$",
    "5": "%",
    "6": "^",
    "7": "&",
    "8": "*",
    "9": "(",
    "0": ")",
}

class TmuxParser(BaseParser):
    @classmethod
    def parse_symbol(cls, token):
        """
        Given a symbol and a list of modifiers, return a string representing
        the parsed token.
        """

        # If we can apply the shift modifier ourselves, then do so. For example,
        # uppercase letters and symbols like `$`.
        #
        # Otherwise, if the symbol is a special character it will pick up tmux's
        # shift modifier when parse_modifiers gets called. For example,
        # <shift><tab> -> S-Tab
        if "shift" in token["modifiers"]:
            if token["symbol"] in SHIFT_SYMBOLS:
                token["symbol"] = SHIFT_SYMBOLS[token["symbol"]]
                token["modifiers"].remove("shift")
            elif len(token["symbol"]) == 1:
                token["symbol"] = token["symbol"].upper()
                token["modifiers"].remove("shift")

        if token["symbol"] in SPECIAL_CHARACTERS:
            token["symbol"] = SPECIAL_CHARACTERS[token["symbol"]]

        parsed_modifiers = cls.parse_modifiers(token["modifiers"])
        return parsed_modifiers + token["symbol"]

    @classmethod
    def parse_modifiers(cls, modifiers):
        """
        Given a list of modifiers parse them into the form the interpreter needs.
        Returns the parsed modifiers as a string.
        """
        parsed_modifiers = ""
        for modifier in modifiers:
            if modifier in MODIFIERS:
                parsed_modifiers += MODIFIERS[modifier]

        return parsed_modifiers
