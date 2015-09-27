import os
import importlib

import config
import lexer
import utilities

def compile_grammars():
    """
    Parses every grammar.py file in the subdirectories of the grammars
    directory. Writes out a grammar_compiled.py file in each subdirectory.
    """
    dirs = utilities.child_directories("grammars")
    for directory in dirs:
        utilities.log("Parsing grammar directory: '" + directory + "'")
        module = ".".join(["grammars", directory, "grammar"])
        grammar = importlib.import_module(module)
        compiled_grammar = config.Parser.parse(lexer.lex(grammar.grammar))
        grammar_path = os.path.join("grammars", directory, "grammar_compiled.py")
        with open(grammar_path, "w+") as output_file:
            utilities.dump_grammar(compiled_grammar, output_file)

def compile_filter():
    """
    Compiles the grammar filter. That is, it essentially reverses the
    grammar_filter dictionary. This makes it easy to look up a mistaken word as
    one of the keys of the compiled_filter dictionary.
    """
    grammar_filter = utilities.import_attribute("grammars.grammar_filter", "grammar_filter")
    compiled_filter = {}
    for key in grammar_filter:
        for value in grammar_filter[key]:
            compiled_filter[value] = key

    with open("./grammars/filter_compiled.py", "w+") as output_file:
        utilities.dump_filter(compiled_filter, output_file)


if __name__ == "__main__":
    compile_grammars()
