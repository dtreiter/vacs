import unittest
import lexer

class TestLexer(unittest.TestCase):
    def test_letters(self):
        result = lexer.lex({"test": "abc"})
        expected = [{
            "key": "test",
            "tokens": [
                {
                    "type": "symbol",
                    "modifiers": [],
                    "symbol": "a"
                },
                {
                    "type": "symbol",
                    "modifiers": [],
                    "symbol": "b"
                },
                {
                    "type": "symbol",
                    "modifiers": [],
                    "symbol": "c"
                }
            ]
        }]
        self.assertEqual(result, expected)

    def test_modifiers(self):
        result = lexer.lex({"test": "<ctrl>a<alt>b"})
        expected = [{
            "key": "test",
            "tokens": [
                {
                    "type": "symbol",
                    "modifiers": ["ctrl"],
                    "symbol": "a"
                },
                {
                    "type": "symbol",
                    "modifiers": ["alt"],
                    "symbol": "b"
                }
            ]
        }]
        self.assertEqual(result, expected)

    def test_specials(self):
        result = lexer.lex({"test": "<esc><ctrl><tab>"})
        expected = [{
            "key": "test",
            "tokens": [
                {
                    "type": "symbol",
                    "modifiers": [],
                    "symbol": "esc"
                },
                {
                    "type": "symbol",
                    "modifiers": ["ctrl"],
                    "symbol": "tab"
                }
            ]
        }]
        self.assertEqual(result, expected)

    def test_shift(self):
        result = lexer.lex({"test": "A<shift><tab>"})
        expected = [{
            "key": "test",
            "tokens": [
                {
                    "type": "symbol",
                    "modifiers": ["shift"],
                    "symbol": "a"
                },
                {
                    "type": "symbol",
                    "modifiers": ["shift"],
                    "symbol": "tab"
                }
            ]
        }]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
