#
# example.py
# jParser
#
# Written by Firsov Georgy
# Copyright © 2019 Firsov Georgy. All rights reserved.
# Licensed with GNU GPL v3
#

from jParser.reader import Reader

json = '{                                   ' \
       '    "line1": ["text11", "text12"],  ' \
       '    "line2": {                      ' \
       '                "line21": "text21", ' \
       '                "line22": "text22"  ' \
       '             },                     ' \
       '    "line3": "text3"                ' \
       '}                                   '

if __name__ == '__main__':
    reader = Reader()
    res = reader.parse(json)

    print('Result:')
    print(res)
