# jParser 

[![Version][]]() [![Tests][]]() [![License][]]()

[Version]: https://img.shields.io/badge/Version-v1.0-blue
[Tests]: https://img.shields.io/badge/Tests-passed-brightgreen
[License]: https://img.shields.io/badge/License-GNU%20GPL%20v.3-blue

This module is a JSON parser written with Python's PLY library. PLY provides implementation of Lex and Yacc from \*nix systems on Python. My module makes Python's list or dict from JSON string or file.

### Usage

Usage is not such complicated:
```python
from jParser.reader import Reader

...

reader = Reader()
reader.parse(json_string)     # String with JSON-like data
reader.parse_file(json_file)  # Path to file with JSON
```

### Example

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
