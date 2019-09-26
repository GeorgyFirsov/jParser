#
# jParser/parser.py
# jParser
#
# Written by Firsov Georgy
# Copyright © 2019 Firsov Georgy. All rights reserved.
# Licensed with GNU GPL v3
#

from warnings import warn

from ply import yacc

from Utils.settings import debug, raise_warnings
from Utils.trace import trace
import jParser.lexer

# This tuple was declared in lexer.py. It is necessary
# to include it for parser generator (yacc).
tokens = jParser.lexer.tokens


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
    trace('p_pairs_sg: ({},)', p[1])
    # Do not remove comma! Here I need to have a tuple
    p[0] = (p[1],)


def p_pair(p):
    """pair : STRING ':' value
    """
    trace('p_pair: ({}, {})', p[1], p[3])
    p[0] = (p[1], p[3])


def p_values_pl(p):
    """values : value ',' values
    """
    trace('p_values_pl: ({}, {})', p[1], p[3])
    p[0] = (p[1], p[3])


def p_values_sg(p):
    """values : value
    """
    trace('p_values_sg: ({},)', p[1])
    # Do not remove comma! Here I need to have a tuple
    p[0] = (p[1],)


def p_value(p):
    """value : STRING
             | dict
             | list
    """
    trace('p_value: {}', p[1])
    p[0] = p[1]


def p_empty(p):
    """empty :
    """
    p[0] = None

#                End of grammar implementation                #
###############################################################


# Error handler.
def p_error(p):
    if not p:
        print('Done. End of file.')
    else:
        print('Syntax error.')


def transform_to_list(values: tuple) -> list:
    """Transforms tuple with parsed values
    to list.

    :param values: tuple of values of
    following format:
        (value_1, (value_2, ... (value_n, (value_m)) ... ))
    Each value is string, list or dict.
    """
    if raise_warnings:
        warn("Currently not implemented")
    return list()


def transform_to_dict(pairs: tuple) -> dict:
    """Transforms tuple with parsed values
    to dict.

    :param pairs: tuple of values of
    following format:
        (pair_1, (pair_1, ... (pair_n, (pair_m)) ... ))
    Each pair is a tuple of kind: (string, value)
    """
    if raise_warnings:
        warn("Currently not implemented")
    return dict()


# Parser object. It will be used in Reader to parse JSON from input.
parser = yacc.yacc(debug=debug)
