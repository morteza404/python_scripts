# Example Package

This is a simple example package. You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.

### how to use?

* create whl file

```bash
python3 setup.py bdist_wheel
```

* create venv

```bash
python3 -m venv venv
```

* activate venv

```bash
source venv/bin/activate
```

* install pkg from whl file

```bash
pip install morteza-0.0.1-py3-none-any.whl
``` 

* in python shell

```python
from example_pkg import example
example.choice_random_name()
```