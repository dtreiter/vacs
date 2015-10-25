class BaseParser():
    """
    This base class implements most of the code required to parse a
    tokenized_grammar. Note that this class is not meant to be instantiated -
    all methods are class methods.

    Subclasses will need to implement:
        parse_token - Class method that returns a string in the form the
                      interpreter expects to send the connection.
    """

    @classmethod
    def parse(cls, tokenized_grammar):
        """
        Given a list representing the tokenized grammar, return a dictionary
        representing the compiled grammar.
        """
        grammar = {}
        for entry in tokenized_grammar:
            key = entry["key"]
            value = cls.parse_tokens(entry["tokens"])
            grammar[key] = value

        return grammar

    @classmethod
    def parse_tokens(cls, tokens):
        """
        Given a list of tokens, return a string representing the parsed tokens.
        If the list of tokens is a function reference, return the function
        reference.
        """
        parsed = []
        for token in tokens:
            parsed.append(cls.parse_token(token))

        if callable(parsed[0]):
            return parsed[0]
        else:
            # Convert list to string.
            return " ".join(parsed)

    @classmethod
    def parse_token(cls, token):
        """
        This is just a stub. Subclasses should implement the following behavior:

        Given a symbol and a list of modifiers, return a string representing
        the parsed token.
        If the symbol is a function reference, return the function reference.
        """
        raise NotImplementedError()

    @classmethod
    def parse_string(cls, string):
        """
        Creates a token for each letter in string and then parses them.
        """
        tokens = []
        for letter in list(string):
            tokens.append({
                "modifiers": [],
                "symbol": letter
            })

        return cls.parse_tokens(tokens)
