# TODO This parser is specifically for the tmux set up.

SPECIAL_CHARACTERS = {
    "esc": "Escape",
    " ": "Space",
    "space": "Space",
    "backslash": "\\",
    "tab": "Tab",
    "*": "\\\\*",
    "enter": "Enter"
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
    """
    parsed = []
    for token in tokens:
        parsed.append(parse_token(token))

    # Convert list to string.
    return " ".join(parsed)

def parse_token(token):
    """
    Given a symbol and a list of modifiers, return a string representing
    the parsed token.
    """
    if token["symbol"] in SPECIAL_CHARACTERS:
        token["symbol"] = SPECIAL_CHARACTERS[token["symbol"]]

    if "ctrl" in token["modifiers"]:
        return "C-" + token["symbol"]
    else:
        return token["symbol"]
