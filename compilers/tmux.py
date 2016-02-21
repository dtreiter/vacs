from base import BaseCompiler

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

class TmuxCompiler(BaseCompiler):
    @classmethod
    def compile_key_event(cls, key_event):
        """
        Given a key and a list of modifiers, return a string representing the
        compiled key event.
        """

        # If we can apply the shift modifier ourselves, then do so. For example,
        # uppercase letters and symbols like `$`.
        #
        # Otherwise, if the key is a special character it will pick up tmux's
        # shift modifier when compile_modifiers gets called. For example,
        # <shift><tab> -> S-Tab
        if "shift" in key_event["modifiers"]:
            if key_event["key"] in SHIFT_SYMBOLS:
                key_event["key"] = SHIFT_SYMBOLS[key_event["key"]]
                key_event["modifiers"].remove("shift")
            elif len(key_event["key"]) == 1:
                key_event["key"] = key_event["key"].upper()
                key_event["modifiers"].remove("shift")

        if key_event["key"] in SPECIAL_CHARACTERS:
            key_event["key"] = SPECIAL_CHARACTERS[key_event["key"]]

        compiled_modifiers = cls.compile_modifiers(key_event["modifiers"])
        return compiled_modifiers + key_event["key"]

    @classmethod
    def compile_modifiers(cls, modifiers):
        """
        Given a list of modifiers compile them into the form the interpreter needs.
        Returns the compiled modifiers as a string.
        """
        compiled_modifiers = ""
        for modifier in modifiers:
            if modifier in MODIFIERS:
                compiled_modifiers += MODIFIERS[modifier]

        return compiled_modifiers
