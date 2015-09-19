import os
import sys
import tty
import importlib

import modes
import utilities

class CoreInterpreter():
    def __init__(self):
        # Holds all grammar rules that the interpreter will use.
        self.mode_grammar = {}
        self.parser = None

    def load_grammars(self):
        """
        Loads each compiled grammar from the subdirectories of the grammars
        directory.
        """
        grammars = {}
        directories = utilities.child_directories("grammars")
        for directory in directories:
            print("Loading grammar: '" + directory + "'")
            module = ".".join(["grammars", directory, "grammar_compiled"])
            grammar = importlib.import_module(module)
            grammars[directory] = grammar.grammar

        return grammars

    def set_mode(self, mode, grammars):
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
            if word in self.mode_grammar:
                if callable(self.mode_grammar[word]):
                    # Run the rest of the text through the function.
                    text = " ".join(words[index + 1:])
                    try:
                        result = self.mode_grammar[word](text)
                        keys = self.parser.parse_string(result)
                        self.send_keystrokes(keys)
                        print("FUNCTION " + word + " -> " + keys + "\r")
                    except:
                        print("ERROR: Unexpected error in grammar function" + "\r")
                        print(str(sys.exc_info()[0]) + "\r")
                    break
                else:
                    keys = self.mode_grammar[word]
                    self.send_keystrokes(keys)
                    # The \r is needed when outputting in raw mode.
                    print(word + " -> " + self.mode_grammar[word] + "\r")
            else:
                print("Unrecognized rule: " + word + "\r")
                break

    def send_keystrokes(self, words):
        raise NotImplementedError()

    def interpret(self):
        grammars = self.load_grammars()
        self.set_mode("python", grammars)
        self.read_input()
