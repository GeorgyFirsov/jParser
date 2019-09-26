#
# main.py
# jParser
#
# Written by Firsov Georgy
# Copyright © 2019 Firsov Georgy. All rights reserved.
# Licensed with GNU GPL v3
#

from jParser.reader import Reader

if __name__ == '__main__':
    reader = Reader()
    res = reader.parse(
        '{                 '
        '   "line1": [],   '
        '   "line2": {},   '
        '   "line3": "khl" '
        '}                 '
    )

    print(f'Result: {res, type(res)}')
