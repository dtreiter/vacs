from core import BaseParser

SPECIAL_CHARACTERS = {
    "esc": "Escape",
    "enter": "Enter",
    "bspace": "Bspace",
    "tab": "Tab",
    "pgup": "PgUp",
    "pgdn": "PgDn",
    "up": "Up",
    "down": "Down",
    "left": "Left",
    "right": "Right",
    "lbracket": "\\\\<",
    "rbracket": "\\\\>",
    "quote": "\\\\\\\"",
    "backslash": "\\\\\\\\",
    "(": "\\\\(",
    ")": "\\\\)",
    "[": "\\\\[",
    "]": "\\\\]",
    "'": "\\\\'",
    "`": "\\\\`",
    ";": "\\\"\\\\;\\\"",
    " ": "Space",
    "#": "\\\\#",
    "*": "\\\\*"
}

MODIFIERS = {
    "ctrl": "C-",
    "alt": "M-"
}

class TmuxParser(BaseParser):
    @classmethod
    def parse_token(cls, token):
        """
        Given a symbol and a list of modifiers, return a string representing
        the parsed token.
        If the symbol is a function reference, return the function reference.
        """
        if callable(token["symbol"]):
            return token["symbol"]
        elif token["symbol"] in SPECIAL_CHARACTERS:
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
