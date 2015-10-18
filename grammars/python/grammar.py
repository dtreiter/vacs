from functions import *

def snippet(key):
    return key + "<alt>/"


grammar = {
    "and": " and ",
    "comment": "# ",
    "from": "from ",
    "hippie": "<alt>/",
    "import": "import ",
    "initialize": "__init__",
    "length": "len()<left>",
    "magic": "____<left><left>",
    "or": " or ",
    "pie": "py",
    "print": "print()<left>",
    "python": "python ",
    "range": "range()<left>",
    "return": "return ",
    "self": "self",

    "also": snippet("vcei"),
    "condition": snippet("vcif"),
    "document": snippet("vcds"),
    "else": snippet("vces"),
    "function": snippet("vcfn"),
    "loop": snippet("vcfr"),
    "value": snippet("vcdv"),
}
