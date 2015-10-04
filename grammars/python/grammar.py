from functions import *

def snippet(key):
    return key + "<alt>/"


grammar = {
    "and": " and ",
    "comment": "# ",
    "document": "<quote><quote><quote><enter><enter><quote><quote><quote><up>",
    "from": "from ",
    "hippie": "<alt>/",
    "import": "import ",
    "length": "len()<left>",
    "or": " or ",
    "pie": "py",
    "print": "print()<left>",
    "python": "python ",
    "range": "range()<left>",
    "return": "return ",
    "self": "self",

    "also": snippet("vcei"),
    "condition": snippet("vcif"),
    "else": snippet("vces"),
    "function": snippet("vcfn"),
    "loop": snippet("vcfr"),
    "value": snippet("vcdv"),

    "magic": magic_case
}
