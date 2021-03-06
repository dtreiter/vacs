from base import BaseCompiler

# Mapping of keys to their corresponding decimal scan code. Note that only the
# key down scan codes are stored - the key up scan code is formed by adding 128
# to the original scan code.
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
    "backspace": 14,
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
    "f3": 61,
    "f4": 62,
    "f5": 63,
    "f6": 64,
    "f7": 65,
    "f8": 66,
    "f9": 67,
    "f10": 68,
    "home": 71,
    "up": 72,
    "pageup": 73,
    "left": 75,
    "right": 77,
    "end": 79,
    "down": 80,
    "pagedown": 81,
    "insert": 82,
    "delete": 83,
    "f11": 87,
    "f12": 88,
}

class VboxCompiler(BaseCompiler):
    @classmethod
    def compile_key_event(cls, key_event):
        """
        Return all key up and key down scan codes for the key event.
        """
        scancodes = cls.get_scancodes(key_event)
        return scancodes

    @classmethod
    def get_scancodes(cls, key_event):
        """
        Given a key event, return a space separated string containing the keyboard
        scan codes corresponding to the key event.
        """
        if key_event["key"] in SCANCODES:
            code = SCANCODES[key_event["key"]]
            scancodes = []
            scancodes.extend(cls.get_modifier_keydowns(key_event))
            scancodes.extend([cls.keydown(code), cls.keyup(code)])
            scancodes.extend(cls.get_modifier_keyups(key_event))
            return " ".join(scancodes)
        else:
            print("ERROR: Key '" + key_event["key"] + "' not in scan codes list.")
            return "" # TODO Should maybe throw exception?

    @classmethod
    def get_modifier_keydowns(cls, key_event):
        """
        Given a key event, return a list containing the keyboard scan codes
        corresponding to each key down for each modifier present in the key
        event.
        """
        keydowns = []
        for modifier in key_event["modifiers"]:
            keydowns.append(cls.keydown(SCANCODES[modifier]))

        return keydowns

    @classmethod
    def get_modifier_keyups(cls, key_event):
        """
        Given a key event, return a list containing the keyboard scan codes
        corresponding to each key up for each modifier present in the key
        event.
        """
        keyups = []
        for modifier in key_event["modifiers"]:
            keyups.append(cls.keyup(SCANCODES[modifier]))

        return keyups

    @classmethod
    def keydown(cls, code):
        """
        VirtualBox expects each scan code in a 2 digit hex format. Since we
        store it in decimal, we convert to hex here.
        """
        return format(code, "02x")

    @classmethod
    def keyup(cls, code):
        """
        Given a scan code, add 128 to it to form the key up scan code. Then
        convert it to the two digit hex format that VirtualBox expects.
        """
        return format(code + 128, "02x")
