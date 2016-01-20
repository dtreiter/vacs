import os
import sys
import tty
import importlib
import re
import traceback

import config
import lexer # TODO Reorganize to remove dependency.
import modes
import utilities

class WordBuffer():
    """
    This class implements an iterator for parsing a phrase which may contain
    punctuation. It's used to return each word separate from its punctuation for
    plain grammar rules using `next`, but leave the punctuation unaltered for
    grammar functions using `get_all`.
    """

    def __init__(self, words):
        if (words == " "):
            # This exists specifically to accommodate typing alongside
            # speaking. This lets the user map the spacebar key.
            self.words = [" "]
        else:
            self.words = words.split(" ")
            # Remove any empty string words. This can happen when the phrase
            # begins with the space. The leading space will simply be ignored.
            self.words = [word for word in self.words if word]

    def __iter__(self):
        return self

    def next(self):
        """
        Returns each word or punctuation mark individually.
        """
        if len(self.words) == 0:
            raise StopIteration()
        word = self.words.pop(0)
        if re.match("[,.:;\-_/\"]$", word):
            return word
        else:
            split_words = re.split("([,.:;\-_/\"])", word)
            # Remove any empty string words. This can happen when the word which
            # gets split consists of only punctuation.
            split_words = [word for word in split_words if word]
            self.words = split_words[1:] + self.words
            return split_words[0]

    def get_all(self):
        """
        Returns the rest of the words without breaking them apart by
        punctuation.
        """
        all_words = " ".join(self.words)
        self.words = []
        return all_words

class BaseInterpreter():
    def __init__(self):
        self.aliases = {}
        self.grammars = {}
        self.compiled_grammars = {}
        # Holds all grammar rules that the interpreter will use.
        self.mode_grammar = {}
        self.mode_grammar_compiled = {}
        self.mode = config.DEFAULT_MODE

    def load_aliases(self):
        """
        Compiles the grammar aliases. That is, it essentially reverses the
        aliases dictionary. This makes it easy to look up a mistaken word as
        one of the keys of the compiled_aliases dictionary.
        """
        aliases = utilities.import_attribute("grammars.aliases", "aliases")
        compiled_aliases = {}
        for key in aliases:
            for value in aliases[key]:
                compiled_aliases[value] = key

        return compiled_aliases

    def clear_grammar_cache(self):
        """
        Since grammars are just Python modules, Python will cache them in
        `sys.modules` once they've been imported. This function will clear the
        cache so changes in grammars can be reloaded.
        """
        grammars = utilities.get_grammar_names()
        for grammar in grammars:
            module = ".".join(["grammars", grammar])
            del sys.modules[module]

    def load_grammars(self, parse):
        """
        Loads each compiled grammar from the subdirectories of the grammars
        directory.
        """
        # TODO don't call load grammars twice. Just modify self.grammars and
        # self.grammars_compiled directly
        grammars = {}
        grammar_names = utilities.get_grammar_names()
        for grammar_name in grammar_names:
            module = ".".join(["grammars", grammar_name])
            grammar = importlib.import_module(module)
            if parse:
                utilities.log("Parsing grammar: '" + grammar_name + "'", verbose=True)
                grammars[grammar_name] = config.Parser.parse(lexer.lex(grammar.grammar))
            elif not parse:
                grammars[grammar_name] = grammar.grammar

        return grammars

    def load_all(self):
        """
        Loads all of the grammars and aliases.
        """
        self.aliases = self.load_aliases()
        self.grammars = self.load_grammars(parse=False)
        self.compiled_grammars = self.load_grammars(parse=True)

    def set_mode(self, mode):
        """
        Populates self.mode_grammar with each grammar specified by the mode.
        """
        if mode in modes.modes:
            self.mode_grammar.clear()
            self.mode_grammar_compiled.clear()
            # The list of grammars which make up this mode.
            mode_grammars = modes.modes[mode]
            for grammar in mode_grammars:
                # Add the rules from the grammar to self.mode_grammar.
                self.mode_grammar.update(self.grammars[grammar])
                self.mode_grammar_compiled.update(self.compiled_grammars[grammar])
        else:
            utilities.log("Unrecognized mode: " + mode)

    def reinitialize(self):
        """
        Reloads all of the grammars to repopulate the mode_grammar.
        """
        self.clear_grammar_cache()
        self.load_all()
        self.set_mode(self.mode)

    def read_input(self):
        """
        Reads continuously from standard input and processes each word.
        """
        fileno = sys.stdin.fileno()
        tty.setraw(fileno)
        while 1:
            text = os.read(0, 1024).lower()
            self.process_text(text)

    def process_text(self, text):
        """
        Loops over each word, stopping if a word is not in mode_grammar. If the
        rule's value is a function, call the function with the rest of the
        words. Otherwise send the rule's value.
        """
        words = WordBuffer(text)
        for word in words:
            # Correct the word if it is in the aliases.
            if word in self.aliases:
                utilities.log(word + " => " + self.aliases[word], verbose=True)
                word = self.aliases[word]

            if word in self.mode_grammar_compiled:
                if callable(self.mode_grammar_compiled[word]):
                    try:
                        # Run the rest of the text through the function.
                        rest = words.get_all()
                        if rest == "":
                            utilities.log("ERROR: No text provided for grammar function.")
                            break
                        result = self.mode_grammar_compiled[word](rest)
                        if isinstance(result, str) and result != "":
                            keys = config.Parser.parse_string(result)
                            self.send_keystrokes(keys)
                            utilities.log(word + "(<phrase>) -> " + result)
                            utilities.log("parsed: " + keys, verbose=True)
                        else:
                            utilities.log(word + "(<phrase>)")
                    except:
                        utilities.log("ERROR: Unexpected error in grammar function")
                        utilities.log(traceback.format_exc())
                        utilities.log(str(sys.exc_info()[0]))
                    break
                else:
                    keys = self.mode_grammar_compiled[word]
                    self.send_keystrokes(keys)
                    try:
                        utilities.log(word + " -> " + self.mode_grammar[word])
                    except:
                        utilities.log("UNPRINTABLE GRAMMAR RULE", verbose=True)
            else:
                utilities.log("Unrecognized rule: " + word)
                break

    def send_keystrokes(self, words):
        raise NotImplementedError()

    def interpret(self):
        utilities.log("Loading grammars...")
        self.load_all()
        self.set_mode(config.DEFAULT_MODE)
        utilities.log("Loading complete.")
        self.read_input()
