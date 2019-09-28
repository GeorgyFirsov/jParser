| id     | title  |
| ------ | ------ |
| reader | Reader |

### Overview

Instances of `Reader` class provide parsing of JSON 
behind really simple interface. It has only 2 public 
functions:
- `parse`
- `parse_file`

### Usage

To use this class you need to import `jParser.reader` module:
```python
from jParser.reader import Reader
```

After that you can user `Reader` class:
```python
reader = Reader()
data = reader.parse(
    '{"key1": "value1", "key2"; ["list_item1", true]}'
)

# Will print:
#   {"key1": "value1", "key2"; ["list_item1", True]}
print(data)
```

Or you can read parse a file:
```python
reader = Reader()
reader.parse_file('data.json')
```

### Return value

If function succeeds it returns a Python's `dict` or `list`. 
It depends on JSON content.

### Errors and exception safity

Instances of `Reader` are exception-safe. So no exception 
will leave functions of this class.

In case of errors the return value of `parse` and 
`parse_file` will be `None`.
