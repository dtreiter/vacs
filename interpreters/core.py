import os
import sys
import tty
import importlib

import config
import modes
import utilities
from grammars.filter_compiled import grammar_filter

class CoreInterpreter():
    def __init__(self):
        # Holds all grammar rules that the interpreter will use.
        self.mode_grammar = {}
        self.mode_grammar_compiled = {}

    def load_grammars(self, filename):
        """
        Loads each compiled grammar from the subdirectories of the grammars
        directory.
        """
        grammars = {}
        directories = utilities.child_directories("grammars")
        for directory in directories:
            utilities.log("Loading grammar: '" + directory + "'", verbose=True)
            module = ".".join(["grammars", directory, filename])
            grammar = importlib.import_module(module)
            grammars[directory] = grammar.grammar

        return grammars

    def set_mode(self, mode, grammars, compiled_grammars):
        """
        Populates self.mode_grammar with each grammar specified by the mode.
        """
        if mode in modes.modes:
            self.mode_grammar.clear()
            # The list of grammars which make up this mode.
            mode_grammars = modes.modes[mode]
            for grammar in mode_grammars:
                # Add the rules from the grammar to self.mode_grammar.
                self.mode_grammar.update(grammars[grammar])
                self.mode_grammar_compiled.update(compiled_grammars[grammar])
        else:
            print("Unrecognized mode: " + mode)

    def read_input(self):
        """
        Reads continuously from standard input and processes each word.
        """
        fileno = sys.stdin.fileno()
        tty.setraw(fileno)
        while 1:
            data = os.read(0, 1024).lower()
            words = data.split(" ")
            self.process_words(words)

    def process_words(self, words):
        """
        Loops over each word, stopping if a word is not in mode_grammar. If the
        rule's value is a function, call the function with the rest of the
        words. Otherwise send the rule's value.
        """
        for index, word in enumerate(words):
            # Correct the word if it is in the grammar_filter.
            if word in grammar_filter:
                utilities.log(word + " => " + grammar_filter[word], verbose=True)
                word = grammar_filter[word]

            if word in self.mode_grammar_compiled:
                if callable(self.mode_grammar_compiled[word]):
                    try:
                        # Run the rest of the text through the function.
                        text = " ".join(words[index + 1:])
                        if text == "":
                            utilities.log("ERROR: No text provided for grammar function.")
                            break
                        result = self.mode_grammar_compiled[word](text)
                        keys = config.Parser.parse_string(result)
                        self.send_keystrokes(keys)
                        utilities.log(word + " (FUNCTION) -> " + result)
                        utilities.log("parsed: " + keys, verbose=True)
                    except:
                        utilities.log("ERROR: Unexpected error in grammar function")
                        utilities.log(str(sys.exc_info()[0]))
                    break
                else:
                    keys = self.mode_grammar_compiled[word]
                    self.send_keystrokes(keys)
                    utilities.log(word + " -> " + self.mode_grammar[word])
            else:
                utilities.log("Unrecognized rule: " + word)
                break

    def send_keystrokes(self, words):
        raise NotImplementedError()

    def interpret(self):
        utilities.log("Loading grammars...")
        grammars = self.load_grammars("grammar")
        compiled_grammars = self.load_grammars("grammar_compiled")
        self.set_mode("python", grammars, compiled_grammars)
        utilities.log("Loading complete.")
        self.read_input()
