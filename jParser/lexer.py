#
# jParser/lexer.py
# jParser
#
# Written by Firsov Georgy
# Copyright © 2019 Firsov Georgy. All rights reserved.
# Licensed with GNU GPL v3
#

from ply import lex

from Utils.settings import debug

# These reserved words will be recognized "as-is"
reserved = {
    'true': 'TRUE',
    'false': 'FALSE',
}

# This tuple contains all tokens, that can be in JSON-file
tokens = (
    'STRING',
    'NUMBER',
    'ID',
) + tuple(reserved.values())

# It is a tuple with all literals (symbols, which are
# not tokens, but can be in JSON-file). They will be
# recognized "as-is".
literals = (
    '{', '}',
    '[', ']',
    ',', ':',
)

# String is any sequence of characters surrounded with
# double quotes with only condition: no internal quotes allowed
t_STRING = r'"[^"]*"'

# Number is any combination of digits with one dot (or without it)
t_NUMBER = r'(-){0,1}([0-9]+\.{0,1}[0-9]+|[0-9]+)'

# Id is any combination of letters, digits, dashes and underscores
# in any order of any length. The only condition: first symbol
# should be a letter.
r_ID = r'[A-Za-z][A-Za-z0-9_\-]*'

# Spaces and tabs are not recognized as tokens or literals
t_ignore = ' \t'

# New line escape sequence
r_newline = r'\n+'


# This function counts lines
@lex.TOKEN(r_newline)
def t_newline(t):
    t.lexer.lineno += len(t.value)


@lex.TOKEN(r_ID)
def t_ID(t):
    t.type = reserved.get(t.value, 'ID')
    return t


# Error handler
def t_error(t):
    print(f'Illegal character: {t.value[0]} at ({t.lineno}, {t.lexpos})')


# Lexer object that will be passed to parser.
lexer = lex.lex(debug=debug)
