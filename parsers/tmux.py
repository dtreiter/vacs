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
    "alt": "M-"
}

class TmuxParser(BaseParser):
    @classmethod
    def parse_symbol(cls, token):
        """
        Given a symbol and a list of modifiers, return a string representing
        the parsed token.
        """
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
