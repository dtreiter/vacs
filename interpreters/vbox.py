import os
import sys

sys.path.insert(1, "..")
from parsers.vbox import VboxParser as parser
from core import CoreInterpreter

class VboxInterpreter(CoreInterpreter):
    def __init__(self):
        CoreInterpreter.__init__(self) # TODO Use super()
        self.parser = parser

    def send_keystrokes(self, keys):
        for scancode in keys.split(" "):
            os.system("VBoxManage controlvm SiftMri keyboardputscancode " + scancode)
