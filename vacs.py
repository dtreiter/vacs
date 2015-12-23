import argparse

import config
import compiler
import utilities

def main():
    """
    Parse any command line arguments and do the corresponding task.
    If no arguments are provided, start the interpreter.
    """
    argument_parser = argparse.ArgumentParser(description="Voice Accessibility Control System")
    argument_parser.add_argument("connection_type",
                                 help="Where vacs should send key strokes to",
                                 default="vbox",
                                 choices=["vbox", "tmux"],
                                 action="store")
    argument_parser.add_argument("connection_name",
                                 help="The session or VM name",
                                 default="vacs",
                                 action="store")
    argument_parser.add_argument("--verbose",
                                 help="Enable verbose logging",
                                 action="store_true")
    arguments = argument_parser.parse_args()

    utilities.set_connection(arguments.connection_type, arguments.connection_name)

    if arguments.verbose:
        utilities.set_verbose(True)
    interpreter = config.Interpreter()
    interpreter.interpret()


if __name__ == "__main__":
    main()
