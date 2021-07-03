#!/usr/bin/env python3

import configparser

read_config = configparser.ConfigParser()
read_config.read("object-server.conf")

bind_ip = read_config.get("DEFAULT", "bind_ip")
bind_port = read_config.get("DEFAULT", "bind_port")
pipeline = read_config.get("pipeline:main","pipeline")
use = read_config.get("app:object-server","use")

print(bind_ip)
print(bind_port)
print(pipeline)
print(use)