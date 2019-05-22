def snippet(key):
    return key + "<alt>/"

grammar = {
    "another": "<esc>A;<enter>",
    "canvas": "canvas",
    "console": "<ctrl>J",
    "constant": "const ",
    "finish": "<esc>A;<esc>",
    "javascript": ".js",
    "js": "js",
    "log": "console.log();<left><left>",
    "new": "new ",
    "node": "node ",
    "package": "npm ",
    "regular": "//<left>",
    "this": "this",
    "declare": "var ",

    "function": snippet("vcfn"),
    "method": snippet("vcmt"),
    "object": snippet("vcob")
}
