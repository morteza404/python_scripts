from distutils.core import setup

setup(name='funproject',
      version='1.0',
      entry_points = {
        'console_scripts': ['mybinary=mymodule.command_line:cli']}
      )