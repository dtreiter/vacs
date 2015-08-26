import argparse
import utilities
import compiler
import interpreter

def main():
    """
    Parse any command line arguments and do the corresponding task.
    If no arguments are provided, start the interpreter.
    """
    argument_parser = argparse.ArgumentParser(description="Voice Accessibility Control System")
    argument_parser.add_argument("--create-grammar",
                                 help="Create the files necessary for a new grammar",
                                 action="store")
    argument_parser.add_argument("--compile",
                                 help="Compile all grammar files",
                                 action="store_true")
    arguments = argument_parser.parse_args()

    if arguments.create_grammar:
        utilities.create_grammar(arguments.create_grammar)
    elif arguments.compile:
        compiler.compile_grammars()
    else:
        interpreter.interpret()


if __name__ == "__main__":
    main()
