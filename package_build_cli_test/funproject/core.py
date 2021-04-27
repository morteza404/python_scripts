#!/usr/bin/env python3

from random import choice

def formal_greeting():
    greeting_messages = ["Hey", "whats life!", "whats up!"]
    return choice(greeting_messages)

def informal_greeting():
    greeting_messages = ["good morning", "nice to meet you", "how have you been?"]
    return choice(greeting_messages)