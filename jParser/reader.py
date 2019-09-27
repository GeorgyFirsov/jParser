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
from jParser.parser import parser, YaccSyntaxError
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
        """Receives json as a string and returns
        corresponding dict or list.
        """
        try:
            return self.__parser.parse(json, lexer=lexer, debug=debug)

        except LexError:
            print('LexError caught. See description above.\n')
            return None
        except YaccSyntaxError as error:
            print(error.what())
            return None

    def parse_file(self, json_file: str):
        """Receives a name of file with json as
        a string and returns corresponding dict or list.
        In case of error returns None.
        """
        try:
            with open(json_file, 'r') as file:
                try:
                    return self.__parser.parse(
                        file.read(), lexer=lexer, debug=debug
                    )

                except LexError:
                    print('LexError caught. See description above.\n')
                    return None
                except YaccSyntaxError as error:
                    print(error.what())
                    return None

        except FileNotFoundError:
            print("File doesn't exist")
            return None
        except PermissionError:
            print("File cannot be opened: access denied")
            return None
