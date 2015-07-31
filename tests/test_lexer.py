import unittest
import lexer

class TestLexer(unittest.TestCase):
    def test_letters(self):
        result = lexer.lex({"test": "abc"})
        expected = [{
            "key": "test",
            "tokens": [
                {
                    "modifiers": [],
                    "symbol": "a"
                },
                {
                    "modifiers": [],
                    "symbol": "b"
                },
                {
                    "modifiers": [],
                    "symbol": "c"
                }
            ]
        }]
        self.assertEqual(result, expected)

    def test_modifiers(self):
        result = lexer.lex({"test": "<ctrl>a<ctrl><shift>b"})
        expected = [{
            "key": "test",
            "tokens": [
                {
                    "modifiers": ["ctrl"],
                    "symbol": "a"
                },
                {
                    "modifiers": ["ctrl", "shift"],
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
                    "modifiers": [],
                    "symbol": "esc"
                },
                {
                    "modifiers": ["ctrl"],
                    "symbol": "tab"
                }
            ]
        }]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
