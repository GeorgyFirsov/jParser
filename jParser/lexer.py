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

# This tuple contains all tokens, that can be in JSON-file
tokens = (
    'STRING',
)

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

# Spaces and tabs are not recognized as tokens or literals
t_ignore = ' \t'

# New line escape sequence
r_newline = r'\n+'


# This function counts lines
@lex.TOKEN(r_newline)
def t_newline(t):
    t.lexer.lineno += len(t.value)


# Error handler
def t_error(t):
    print(f'Illegal character: {t.value[0]} at ({t.lineno}, {t.lexpos})')


# Lexer object that will be passed to parser.
lexer = lex.lex(debug=debug)
