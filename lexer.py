import re

def lex(grammar):
    """
    Turns a grammar dictionary into a list of entries each containing
    a key and tokens. Each token consists of a list of modifiers and a
    letter.
    """
    tokenized_grammar = []
    for entry in grammar:
        characters = split_characters(grammar[entry])
        tokens = tokenize(characters)
        tokenized_entry = {
            "key": entry,
            "tokens": tokens
        }
        tokenized_grammar.append(tokenized_entry)

    return tokenized_grammar


def split_characters(string):
    """Splits the string into a list of individual letters and modifiers."""
    return split_letters(split_modifiers(string))


def split_letters(strings):
    """
    Given a list of modifiers and strings, return a list of modifiers
    and individual letters.
    """
    characters = []
    for string in strings:
        if is_modifier(string):
            characters.append(string)
        else:
            characters.extend(list(string))

    return characters


def split_modifiers(string):
    """Splits the string into a list of modifiers and strings."""
    return re.split("(<[^>]+>)", string)


def tokenize(characters):
    """
    Turns a list of characters into a list of dictionaries each containing
    the letter and any modifiers which should be pressed with that letter.
    """
    tokens = []
    iter_characters = iter(characters)
    for character in iter_characters:
        token = {"modifiers": []}
        while is_modifier(character):
            modifier = get_modifier(character)
            token["modifiers"].append(modifier)
            character = next(iter_characters)
        token["letter"] = character
        tokens.append(token)

    return tokens


def is_modifier(character):
    """Determine if the character is a modifier."""
    match = re.match("<[^>]+>", character)
    if match:
        return True

    return False


def get_modifier(character):
    """Return the modifier contained within the tag."""
    match = re.match("<([^>]+)>", character)
    return match.group(1)
