from functions import *

hippie_expand = "<alt>/"

grammar = {
    "python": "python ",
    "pie": "py",
    "self": "self",
    "return": "return ",
    "from": "from ",
    "print": "print()<left>",
    "range": "range()<left>",
    "links": "len()<left>",
    "length": "len()<left>",
    "comment": "# ",
    "import": "import ",
    "hippie": hippie_expand,
    "function": "f" + hippie_expand,
    "condition": "if" + hippie_expand,
    "else": "else:<enter>",
    "value": "d<quote>" + hippie_expand,
    "loop": "frn" + hippie_expand,
    "luke": "frn" + hippie_expand,

    "magic": magic_case
}
