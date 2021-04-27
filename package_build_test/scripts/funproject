#!/usr/bin/env python3
# build-in imports
import sys
from argparse import ArgumentParser

# third-party imports
from funproject import formal_greeting, informal_greeting

DESCRIPTION="""
usage: funproject [-h] formal informal
Basic Command-line for funproject program
positional arguments:
    formal - print formal greeting
    informal - print informal greeting
optional arguments:
       -h, --help  show this help message and exit
"""

def get_message(greeting_type):
    """
    Return greeting based on input
    """
    message = None
    if greeting_type == 'formal':
        message = formal_greeting()
    elif greeting_type == 'informal':
        message = informal_greeting()
    else:
        return DESCRIPTION
    return message


def main():
    """
    Very very simple command-line for our funproject
    """

    number_of_arguments = len(sys.argv)

    arguments_list = sys.argv
    if number_of_arguments != 2:
        print(DESCRIPTION)
        sys.exit(1)
    second_argument = arguments_list[1]
    message = get_message(second_argument)
    print(message)

if __name__ == '__main__':
    main()
