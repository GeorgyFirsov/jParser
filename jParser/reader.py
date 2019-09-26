#
# jParser/reader.py
# jParser
#
# Written by Firsov Georgy
# Copyright © 2019 Firsov Georgy. All rights reserved.
# Licensed with GNU GPL v3
#

from ply.lex import LexError

from jParser.lexer import lexer
from jParser.parser import parser
from Utils.settings import debug


class Reader(object):
    """Class hides some ugly lexer and parser
    work from endpoint user. Usage is
    extremely simple: call method parse
    with JSON represented as string or
    method parse_file with the name of file
    to parse JSON from file.
    """

    def __init__(self):
        self.__parser = parser

    def parse(self, json: str):
        try:
            return self.__parser.parse(json, lexer=lexer, debug=debug)
        except LexError:
            print('LexError caught. See description above.\n')
            return None

    def parse_file(self, json_file: str):
        with open(json_file, 'r') as file:
            try:
                return self.__parser.parse(
                    file.read(), lexer=lexer, debug=debug
                )
            except LexError:
                print('LexError caught. See description above.\n')
                return None
