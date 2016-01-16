def snippet(key):
    return key + "<alt>/"


grammar = {
    "and": " and ",
    "cheese": "pip ",
    "comment": "# ",
    "false": "False",
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
    "true": "True",

    "also": snippet("vcei"),
    "condition": snippet("vcif"),
    "document": snippet("vcds"),
    "else": snippet("vces"),
    "function": snippet("vcfn"),
    "loop": snippet("vcfr"),
    "value": snippet("vcdv"),
}
