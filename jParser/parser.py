#
# jParser/parser.py
# jParser
#
# Written by Firsov Georgy
# Copyright © 2019 Firsov Georgy. All rights reserved.
# Licensed with GNU GPL v3
#

from ply import yacc

from Utils.settings import debug
from Utils.trace import trace
import jParser.lexer

# This tuple was declared in lexer.py. It is necessary
# to include it for parser generator (yacc).
tokens = jParser.lexer.tokens


class YaccSyntaxError(BaseException):
    """Class describes syntax error.
    It contains info about wrong
    statement position
    """

    def __init__(self, lineno):
        self.__lineno = lineno

    def what(self):
        return 'Syntax error at line {}'.format(self.__lineno)


###############################################################
#              Here comes grammar implementation              #

def p_json(p):
    """json : dict
            | list
            | empty
    """
    trace('p_json: {}', p[1])
    p[0] = p[1]


def p_dict_pairs(p):
    """dict : '{' pairs '}'
    """
    trace('p_dict_pairs: transform_to_dict({})', p[2])
    p[0] = transform_to_dict(p[2])


def p_dict_empty(p):
    """dict : '{' '}'
    """
    trace('p_dict_empty')
    p[0] = {}


def p_list_values(p):
    """list : '[' values ']'
    """
    trace('p_list_values: transform_to_list({})', p[2])
    p[0] = transform_to_list(p[2])


def p_list_empty(p):
    """list : '[' ']'
    """
    trace('p_list_empty')
    p[0] = []


def p_pairs_pl(p):
    """pairs : pair ',' pairs
    """
    trace('p_pairs_pl: ({}, {})', p[1], p[3])
    p[0] = (p[1], p[3])


def p_pairs_sg(p):
    """pairs : pair
    """
    trace('p_pairs_sg: ({}, None)', p[1])
    p[0] = (p[1], None)


def p_pair(p):
    """pair : key ':' value
    """
    trace('p_pair: ({}, {})', p[1], p[3])
    p[0] = (p[1], p[3])


def p_key_str(p):
    """key : STRING
    """
    trace('p_key_str: {}', p[1])
    p[0] = remove_surrounding_quotes(p[1])


def p_key_id(p):
    """key : ID
    """
    trace('p_key_id: {}', p[1])
    p[0] = p[1]


def p_values_pl(p):
    """values : value ',' values
    """
    trace('p_values_pl: ({}, {})', p[1], p[3])
    p[0] = (p[1], p[3])


def p_values_sg(p):
    """values : value
    """
    trace('p_values_sg: ({}, None)', p[1])
    p[0] = (p[1], None)


def p_value_cont(p):
    """value : dict
             | list
    """
    trace('p_value_cont: {}', p[1])
    p[0] = p[1]


def p_value_str(p):
    """value : STRING
    """
    trace('p_value_str: {}', p[1])
    p[0] = remove_surrounding_quotes(p[1])


def p_value_num(p):
    """value : NUMBER
    """
    trace('p_value_num: {}', p[1])
    p[0] = transform_to_number(p[1])


def p_value_id(p):
    """value : ID
    """
    trace('p_value_id: {}', p[1])
    p[0] = p[1]


def p_value_bool(p):
    """value : TRUE
             | FALSE
    """
    trace('p_value_bool')
    p[0] = transform_to_bool(p[1])


def p_empty(p):
    """empty :
    """
    trace('p_empty')
    p[0] = None

#                End of grammar implementation                #
###############################################################


# Error handler
def p_error(p):
    if not p:
        print('Done. End of file.')
    else:
        print(p.value)
        raise YaccSyntaxError(p.lineno)


def transform_to_list(values: tuple) -> list:
    """Transforms tuple with parsed values
    to list.

    :param values: tuple of values of
                   following format:
        (value_1, (value_2, ... (value_n, (value_m, None)) ... ))
    Each value is string, list or dict.
    """
    assert (values is not None)
    assert (len(values))  # Empty tuples can not be here

    result = list()
    current = values

    while current is not None:
        result.append(current[0])
        current = current[1]

    return result


def transform_to_dict(pairs: tuple) -> dict:
    """Transforms tuple with parsed values
    to dict.

    :param pairs: tuple of values of
                  following format:
        (pair_1, (pair_1, ... (pair_n, (pair_m, None)) ... ))
    Each pair is a tuple of kind: (string, value)
    """
    assert (pairs is not None)
    assert (len(pairs))  # Empty tuples can not be here

    result = {}
    current = pairs

    while current is not None:
        key, value = current[0]
        result[key] = value
        current = current[1]

    return result


def transform_to_number(value: str):
    """Returns an integer if value represents
    integer value, otherwise returns float.
    In case of error returns 0
    """
    try:
        try:
            return int(value)
        except ValueError:
            return float(value)
    except TypeError:
        return 0


def transform_to_bool(value: str) -> bool:
    """Transforms string values 'true' and
    'false' to their Python equivalents.
    """
    return value == 'true'


def remove_surrounding_quotes(string: str) -> str:
    """Removes outer quotes from string:
        "string" -> string

    :param string: string with quotes.
                   May not contain them, so
                   firstly check their existence
    """
    if not string.startswith('"') or \
       not string.endswith('"'):
        return string

    return string[1:-1]


# Parser object. It will be used in Reader to parse JSON from input.
parser = yacc.yacc(debug=debug)
