import os
import sys

sys.path.insert(1, "..")
from parsers.tmux import TmuxParser as parser
from core import CoreInterpreter

class TmuxInterpreter(CoreInterpreter):
    def __init__(self):
        CoreInterpreter.__init__(self) # TODO Use super()
        self.parser = parser

    def send_keystrokes(self, keys):
        os.system("tmux send-keys " + keys)
