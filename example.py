#
# example.py
# jParser
#
# Written by Firsov Georgy
# Copyright © 2019 Firsov Georgy. All rights reserved.
# Licensed with GNU GPL v3
#

from jParser.reader import Reader

json = '{                                   \n\
           "line1": ["text11", "text12"],   \n\
           "line2": {                       \n\
                       "line21": "text21",  \n\
                       "line22": "text22"   \n\
                    },                      \n\
           "line3": "text3"                 \n\
       }'

if __name__ == '__main__':
    reader = Reader()
    res = reader.parse(json)

    print('Result:')
    print(res)
