#
# Test/reader_test.py
# jParser
#
# Written by Firsov Georgy
# Copyright © 2019 Firsov Georgy. All rights reserved.
# Licensed with GNU GPL v3
#

import unittest

from jParser.reader import Reader
from Utils.settings import data_location
from Test.test_expectations import expected_7


class ReaderTest(unittest.TestCase):
    def test_str(self):
        json = '{                                   \n\
                   "line1": ["text11", "text12"],   \n\
                   "line2": {                       \n\
                               "line21": "text21",  \n\
                               "line22": "text22"   \n\
                            },                      \n\
                   "line3": "text3"                 \n\
               }'

        expected = {"line1": ["text11", "text12"], "line2": {"line21": "text21", "line22": "text22"}, "line3": "text3"}

        reader = Reader()
        self.assertEqual(expected, reader.parse(json))

    def test_file(self):
        reader = Reader()
        self.assertEqual(expected_7, reader.parse_file(data_location + 'test_example_7.json'))


if __name__ == '__main__':
    unittest.main()
