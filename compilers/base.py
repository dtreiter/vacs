class BaseCompiler():
    """
    This base class implements most of the code required to compile an
    abstract grammar. Note that this class is not meant to be instantiated -
    all methods are class methods.

    Subclasses will need to implement:
        compile_token - Class method that returns a string in the form the
                      interpreter expects to send to the target.
    """

    @classmethod
    def compile(cls, abstract_grammar):
        """
        Given an abstract grammar, return a dictionary representing the compiled
        grammar.
        """
        compiled_grammar = {}
        for entry in abstract_grammar:
            identifier = entry["identifier"]
            # TODO
            #  if entry["type"] == "function":
            #      value = entry["value"]
            #  else:
            value = cls.compile_key_events(entry["value"])
            compiled_grammar[identifier] = value

        return compiled_grammar

    @classmethod
    def compile_key_events(cls, key_events):
        """
        Given a list of key_events, return a string representing the compiled
        key_events.
        """
        if key_events[0]["type"] == "function":
            # The key_event is a function reference.
            return key_events[0]["function"]
        else:
            # The key_events represents a string.
            compiled = []
            for key_event in key_events:
                compiled.append(cls.compile_key_event(key_event))

            # Convert list to string.
            return " ".join(compiled)

    @classmethod
    def compile_key_event(cls, key_event):
        """
        This is just a stub. Subclasses should implement the following behavior:

        Given a key event containing a key and a list of modifiers, return a
        string representing the compiled key event.
        """
        raise NotImplementedError()
