#
# Test/lexer_test.py
# jParser
#
# Written by Firsov Georgy
# Copyright © 2019 Firsov Georgy. All rights reserved.
# Licensed with GNU GPL v3
#

import unittest

from Utils.settings import data_location
from jParser.lexer import lexer


class LexerTest(unittest.TestCase):
    def test_tokenize(self):

        with open(data_location + 'lexer_test.json') as file:
            json = file.read()

        lexer.input(json)

        result = [token.type for token in lexer]
        expected = [
            '{', 'STRING', ':', '{', 'STRING', ':', 'STRING',
            ',', 'STRING', ':', 'NUMBER', ',', 'STRING',
            ':', 'ID', '}', '}'
        ]

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
