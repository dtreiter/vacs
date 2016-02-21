import re

SPECIALS = [
    "esc",
    "f1",
    "f2",
    "f3",
    "f4",
    "f5",
    "f6",
    "f7",
    "f8",
    "f9",
    "f10",
    "f11",
    "f12",
    "tab",
    "backspace",
    "enter",
    "insert",
    "delete",
    "home",
    "end",
    "up",
    "down",
    "left",
    "right",
    "quote",
    "backslash",
    "pagedown",
    "pageup",
    "lbracket",
    "rbracket"
]
MODIFIERS = ["ctrl", "alt", "shift"]

# Mapping of symbols which require the shift key to the non-shift key they are
# physically located on.
SHIFT_SYMBOLS = {
    "_": "-",
    "+": "=",
    "{": "[",
    "}": "]",
    ":": ";",
    "quote": "'",
    "~": "`",
    "|": "backslash",
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

def parse(grammar):
    """
    Turns a grammar dictionary into a list of entries each containing
    a key and tokens. Each token consists of a list of modifiers and a
    symbol.
    """
    parsed_grammar = []
    for entry in grammar:
        if callable(grammar[entry]):
            parsed_entry = {
                "type": "function",
                "identifier": entry,
                "value": grammar[entry]
            }
        else:
            key_events = parse_string(grammar[entry])
            parsed_entry = {
                "type": "key_events",
                "identifier": entry,
                "value": key_events
            }
        parsed_grammar.append(parsed_entry)

    return parsed_grammar


def parse_string(string):
    """Parses a string into a list of key events."""
    tokens = tokenize(string)
    return parse_tokens(tokens)


def tokenize(string):
    """Splits the string into a list of individual letters and tags."""
    return split_letters(split_tags(string))


def split_letters(strings):
    """
    Given a list of tags and strings, return a list of tags and individual
    letters.
    """
    tokens = []
    for string in strings:
        if is_tag(string):
            tokens.append(string)
        else:
            tokens.extend(list(string))

    return tokens


def split_tags(string):
    """Splits the string into a list of tags and strings."""
    return re.split("(<[^>]+>)", string)


def parse_tokens(tokens):
    """
    Turns a list of tokens into a list of key events each containing the key and
    any modifiers which should be pressed with that key.
    """
    key_events = []
    iter_tokens = iter(tokens)
    for token in iter_tokens:
        key_event = {
            "modifiers": []
        }
        while is_modifier(token):
            modifier = get_tag(token)
            key_event["modifiers"].append(modifier)
            token = next(iter_tokens)

        if is_special(token):
            special = get_tag(token)
            key_event["key"] = special
        elif len(token) == 1:
            key_event["key"] = token
        else:
            print("ERROR: Unrecognized tag '" + token + "' in grammar.")
            return

        normalize_shift(key_event)
        key_events.append(key_event)

    return key_events

def normalize_shift(key_event):
    """
    Converts a key which requires the shift key to a plain key with
    the shift modifier.

    For example:
    : -> <shift>;
    """
    if key_event["key"] in SHIFT_SYMBOLS:
        key_event["modifiers"].append("shift")
        key_event["key"] = SHIFT_SYMBOLS[key_event["key"]]
    elif key_event["key"].istitle():
        key_event["modifiers"].append("shift")
        key_event["key"] = key_event["key"].lower()

def is_tag(token):
    """Determine if the token is a tag."""
    match = re.match("<[^>]+>", token)
    if match:
        return True

    return False


def get_tag(token):
    """Return the contents of the tag."""
    match = re.match("<([^>]+)>", token)
    return match.group(1)


def is_modifier(token):
    """Determine if the token is a modifier."""
    if is_tag(token):
        if get_tag(token) in MODIFIERS:
            return True

    return False


def is_special(token):
    """Determine if the token is a special character."""
    if is_tag(token):
        if get_tag(token) in SPECIALS:
            return True

    return False
