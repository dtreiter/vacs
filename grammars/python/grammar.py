from functions import *

def snippet(key):
    return key + "<alt>/"


grammar = {
    "comment": "# ",
    "document": "<quote><quote><quote><enter><enter><quote><quote><quote><up>",
    "else": "else:<enter>",
    "from": "from ",
    "hippie": "<alt>/",
    "import": "import ",
    "length": "len()<left>",
    "pie": "py",
    "print": "print()<left>",
    "python": "python ",
    "range": "range()<left>",
    "return": "return ",
    "self": "self",

    "condition": snippet("if"),
    "function": snippet("f"),
    "loop": snippet("frn"),
    "value": snippet("d<quote>"),

    "magic": magic_case
}
