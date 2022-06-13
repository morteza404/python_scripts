#!/usr/bin/env python3
"""module docstring
"""
import shlex
import subprocess

cmd = "tail -n 10 /var/log/syslog"
args = shlex.split(cmd)
process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()
process.wait()
print(stdout.decode("utf-8"))
print(stderr.decode("utf-8"))

