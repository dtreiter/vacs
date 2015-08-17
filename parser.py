# TODO This parser is specifically for the tmux set up.

SPECIAL_CHARACTERS = {
    "esc": "Escape",
    "enter": "Enter",
    "tab": "Tab",
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
    " ": "Space",
    "*": "\\\\*"
}

MODIFIERS = {
    "ctrl": "C-",
    "alt": "M-"
}

def parse(tokenized_grammar):
    """
    Given a list representing the tokenized grammar, return a dictionary
    representing the compiled grammar.
    """
    grammar = {}
    for entry in tokenized_grammar:
        key = entry["key"]
        value = parse_tokens(entry["tokens"])
        grammar[key] = value

    return grammar

def parse_tokens(tokens):
    """
    Given a list of tokens, return a string representing the parsed tokens.
    If the list of tokens is a function reference, return the function
    reference.
    """
    parsed = []
    for token in tokens:
        parsed.append(parse_token(token))

    if callable(parsed[0]):
        return parsed[0]
    else:
        # Convert list to string.
        return " ".join(parsed)

def parse_token(token):
    """
    Given a symbol and a list of modifiers, return a string representing
    the parsed token.
    If the symbol is a function reference, return the function reference.
    """
    if callable(token["symbol"]):
        return token["symbol"]
    elif token["symbol"] in SPECIAL_CHARACTERS:
        token["symbol"] = SPECIAL_CHARACTERS[token["symbol"]]

    parsed_modifiers = parse_modifiers(token["modifiers"])
    return parsed_modifiers + token["symbol"]

def parse_modifiers(modifiers):
    """
    Given a list of modifiers parse them into the form the interpreter needs.
    Returns the parsed modifiers as a string.
    """
    parsed_modifiers = ""
    for modifier in modifiers:
        if modifier in MODIFIERS:
            parsed_modifiers += MODIFIERS[modifier]

    return parsed_modifiers
