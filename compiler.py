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

def compile_aliases():
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

    with open("./grammars/aliases_compiled.py", "w+") as output_file:
        utilities.dump_aliases(compiled_aliases, output_file)


if __name__ == "__main__":
    compile_grammars()
