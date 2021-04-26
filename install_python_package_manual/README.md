#### for more detail go [here](https://docs.python.org/3/distutils/introduction.html#distutils-simple-example)

If all you want to do is distribute a module called foo, contained in a file foo.py, then your setup script can be as simple as this:

```python
from distutils.core import setup
setup(name='foo',
      version='1.0',
      py_modules=['foo'],
      )
```

To create a source distribution for this module, you would create a setup script, setup.py, containing the above code, and run this command from a terminal:

```
python setup.py sdist
```
If an end-user wishes to install your foo module, all they have to do is download foo-1.0.tar.gz (or .zip), unpack it, and—from the foo-1.0 directory—run

```
python setup.py install
```

the foo module add to python installed packages and appear in pip freeze list.

```
pip freeze
```

so we can uinstall this package by using:

```
pip uninstall foo
```