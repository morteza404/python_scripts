#!/usr/bin/env python3

import six

message = "python2" if six.PY2  else "python3"

print(message)
