import argparse

import globals
import utilities

def main():
    """
    Parse any command line arguments and start the interpreter.
    """
    argument_parser = argparse.ArgumentParser(description="Voice Accessibility Control System")
    argument_parser.add_argument("target_type",
                                 help="Where vacs should send key strokes to",
                                 default="vbox",
                                 choices=["vbox", "tmux"],
                                 action="store")
    argument_parser.add_argument("target_name",
                                 help="The tmux session or VM name",
                                 default="vacs",
                                 action="store")
    argument_parser.add_argument("--verbose",
                                 help="Enable verbose logging",
                                 action="store_true")
    arguments = argument_parser.parse_args()

    if arguments.verbose:
        utilities.set_verbose(True)

    utilities.set_target(arguments.target_type, arguments.target_name)
    globals.Interpreter.interpret()


if __name__ == "__main__":
    main()
