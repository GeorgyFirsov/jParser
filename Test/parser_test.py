#
# Test/test_expectations.py
# jParser
#
# Written by Firsov Georgy
# Copyright © 2019 Firsov Georgy. All rights reserved.
# Licensed with GNU GPL v3
#

import unittest

from Utils.settings import data_location
from jParser.parser import parser
from jParser.lexer import lexer
from Test.test_expectations import *


class ParserTest(unittest.TestCase):
    def test_complicated_1(self):
        with open(data_location + 'test_example_1.json') as file:
            json = file.read()

        result = parser.parse(json, lexer=lexer)

        self.assertEqual(result, expected_1)

    def test_complicated_2(self):
        with open(data_location + 'test_example_2.json') as file:
            json = file.read()

        result = parser.parse(json, lexer=lexer)

        self.assertEqual(result, expected_2)

    def test_complicated_3(self):
        with open(data_location + 'test_example_3.json') as file:
            json = file.read()

        result = parser.parse(json, lexer=lexer)

        self.assertEqual(result, expected_3)

    def test_complicated_4(self):
        with open(data_location + 'test_example_4.json') as file:
            json = file.read()

        result = parser.parse(json, lexer=lexer)

        self.assertEqual(result, expected_4)

    def test_complicated_5(self):
        with open(data_location + 'test_example_5.json') as file:
            json = file.read()

        result = parser.parse(json, lexer=lexer)

        self.assertEqual(result, expected_5)

    def test_complicated_6(self):
        with open(data_location + 'test_example_6.json') as file:
            json = file.read()

        result = parser.parse(json, lexer=lexer)

        self.assertEqual(result, expected_6)

    def test_complicated_7(self):
        with open(data_location + 'test_example_7.json') as file:
            json = file.read()

        result = parser.parse(json, lexer=lexer)

        self.assertEqual(result, expected_7)


if __name__ == '__main__':
    unittest.main()
