# Python Package Setup

This is a basic package that creates distribution `setup.py` files based on necessary parameters. This read-me file is bare-bones right now and will be updated with more information and usage examples shortly.

See a brief demonstration:

[![asciicast](https://asciinema.org/a/481971.svg)](https://asciinema.org/a/481971)
----

Install with `pip install packagesetup`.

Import:

```python
import packagesetup as ps
```

Functions:

`ps.create_setup_file()` --> creates a `setup.py` based on parameters.
`ps.create_blank_setup_file()` --> creates a `setup.py` with no parameters but with placeholder values.
