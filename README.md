# jParser 

[![Version][]]() [![Tests][]]() [![License][]]()

[Version]: https://img.shields.io/badge/Version-v1.0-blue
[Tests]: https://img.shields.io/badge/Tests-passed-brightgreen
[License]: https://img.shields.io/badge/License-GNU%20GPL%20v.3-blue
[PEP8]: https://www.python.org/dev/peps/pep-0008/
[PEP484]: https://www.python.org/dev/peps/pep-0484/

This module is a JSON parser written with Python's PLY library. PLY provides implementation of Lex and Yacc from \*nix systems on Python. My module makes Python's list or dict from JSON string or file.

## Usage

Usage is not such complicated:
```python
from jParser.reader import Reader

...

reader = Reader()
reader.parse(json_string)     # String with JSON-like data
reader.parse_file(json_file)  # Path to file with JSON
```

## Example

Consider following JSON:
```json
{
    "employee": {
        "name":    ["Bob", "Johnson"],
        "salary":  56000,
        "married": false
    }
}
```

It transforms into a dict shown below:
```python
{
    "employee":
        {
            "name":    ["Bob", "Johnson"],
            "salary":  56000,
            "married": False
        }
}
```

## Contribution

First of all, thanks for taking time for contributing :)

> ⚠ **Attention\!** If you don't follow [code guidelines](#Code-guidelines), your pull-request will be declined anyway. Carefully read PEP conventions. It is highly required to make our code cleaner and more understandable.

The only way you can contribute is:
- fork this repo to your GitHub
- make some changes and improvements
- make pull request to this main repo

> 👉 **Note**: All the pull-requests will be strictly checked and reviewed before being accepted or declined. All external pull-requests have the same scrutiny for quality, coding standards, performance, globalization, accessibility, and compatibility as those of me.

#### Code guidelines

Code should match following set of guidelines:
- [PEP8][]
- [PEP484][]
