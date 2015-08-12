import os
import importlib
import lexer
import parser
import utilities

def compile_grammars():
    """
    Parses every grammar.py file in the subdirectories of the grammars
    directory. Writes out a grammar_compiled.py file in each subdirectory.
    """
    dirs = utilities.child_directories("grammars")
    for directory in dirs:
        print("Parsing grammar directory: '" + directory + "'")
        module = ".".join(["grammars", directory, "grammar"])
        grammar = importlib.import_module(module)
        compiled_grammar = parser.parse(lexer.lex(grammar.grammar))
        grammar_path = os.path.join("grammars", directory, "grammar_compiled.py")
        with open(grammar_path, "w+") as output_file:
            utilities.dump_grammar(compiled_grammar, output_file)

if __name__ == "__main__":
    compile_grammars()
