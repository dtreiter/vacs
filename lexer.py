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
MODIFIERS = ["ctrl", "alt"]

def lex(grammar):
    """
    Turns a grammar dictionary into a list of entries each containing
    a key and tokens. Each token consists of a list of modifiers and a
    symbol.
    """
    tokenized_grammar = []
    for entry in grammar:
        if callable(grammar[entry]):
            tokens = [{
                "type": "function",
                "function": grammar[entry]
            }]
        else:
            characters = split_characters(grammar[entry])
            tokens = tokenize(characters)
        tokenized_entry = {
            "key": entry,
            "tokens": tokens
        }
        tokenized_grammar.append(tokenized_entry)

    return tokenized_grammar


def split_characters(string):
    """Splits the string into a list of individual symbols and tags."""
    return split_letters(split_tags(string))


def split_letters(strings):
    """
    Given a list of tags and strings, return a list of tags
    and individual symbols.
    """
    characters = []
    for string in strings:
        if is_tag(string):
            characters.append(string)
        else:
            characters.extend(list(string))

    return characters


def split_tags(string):
    """Splits the string into a list of tags and strings."""
    return re.split("(<[^>]+>)", string)


def tokenize(characters):
    """
    Turns a list of characters into a list of dictionaries each containing
    the symbols and any modifiers which should be pressed with that symbols.
    """
    tokens = []
    iter_characters = iter(characters)
    for character in iter_characters:
        token = {
            "type": "symbol",
            "modifiers": []
        }
        while is_modifier(character):
            modifier = get_tag(character)
            token["modifiers"].append(modifier)
            character = next(iter_characters)

        if is_special(character):
            special = get_tag(character)
            token["symbol"] = special
        elif len(character) == 1:
            token["symbol"] = character
        else:
            print("ERROR: Unrecognized tag '" + character + "' in grammar.")
            return

        tokens.append(token)

    return tokens


def is_tag(character):
    """Determine if the character is a tag."""
    match = re.match("<[^>]+>", character)
    if match:
        return True

    return False


def get_tag(character):
    """Return the contents of the tag."""
    match = re.match("<([^>]+)>", character)
    return match.group(1)


def is_modifier(string):
    """Determine if the string is a modifier."""
    if is_tag(string):
        if get_tag(string) in MODIFIERS:
            return True

    return False


def is_special(string):
    """Determine if the string is a special character."""
    if is_tag(string):
        if get_tag(string) in SPECIALS:
            return True

    return False

def lex_string(string):
    characters = split_characters(string)
    return tokenize(characters)
