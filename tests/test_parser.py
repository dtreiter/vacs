import unittest
import parser

class TestParser(unittest.TestCase):
    def test_letters(self):
        result = parser.parse({"test": "abc"})
        expected = [{
            "identifier": "test",
            "type": "key_events",
            "value": [
                {
                    "modifiers": [],
                    "key": "a"
                },
                {
                    "modifiers": [],
                    "key": "b"
                },
                {
                    "modifiers": [],
                    "key": "c"
                }
            ]
        }]
        self.assertEqual(result, expected)

    def test_modifiers(self):
        result = parser.parse({"test": "<ctrl>a<alt>b"})
        expected = [{
            "identifier": "test",
            "type": "key_events",
            "value": [
                {
                    "modifiers": ["ctrl"],
                    "key": "a"
                },
                {
                    "modifiers": ["alt"],
                    "key": "b"
                }
            ]
        }]
        self.assertEqual(result, expected)

    def test_specials(self):
        result = parser.parse({"test": "<esc><ctrl><tab>"})
        expected = [{
            "identifier": "test",
            "type": "key_events",
            "value": [
                {
                    "modifiers": [],
                    "key": "esc"
                },
                {
                    "modifiers": ["ctrl"],
                    "key": "tab"
                }
            ]
        }]
        self.assertEqual(result, expected)

    def test_shift(self):
        result = parser.parse({"test": "A<shift><tab>"})
        expected = [{
            "identifier": "test",
            "type": "key_events",
            "value": [
                {
                    "modifiers": ["shift"],
                    "key": "a"
                },
                {
                    "modifiers": ["shift"],
                    "key": "tab"
                }
            ]
        }]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
