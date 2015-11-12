#!/usr/bin/env python
# she bangs well...
"""Unix Python Cli Template.

Usage:
  cli_template.py test this <name>...
  cli_template.py more test <x> <y>
  cli_template.py (-h | --help)
  cli_template.py --interactive
  cli_template.py --version

Options:
  -h --help        Show this screen.
  -i --interactive    Goes into interactive mode
  -v --version     Show version.
"""

from docopt import docopt  # for nifty arg parsing
# for the docopt syntax check http://docopt.org/
import readline
import completer  # for tab completion

import sys


# sweet sweet colors
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'


def help_text(rest):
    print "this is a help text in interactive mode"
    return ''


def config(rest):
    print "configuration options"
    return 'inside'


def exit_program(rest):
    print "exiting from interactive mode"
    sys.exit(0)
    return ''


def other(rest):
    print "other"
    return 'menu'


COMMANDS = {
    'menu': {
        'help': help_text,
        'config': config,
        'exit': exit_program
        },
    'inside': {
        'help': help_text,
        'other': other,
        'exit': exit_program
        }
    }
DEFAULT_MODE = 'menu'
comp = completer.Completer(DEFAULT_MODE, COMMANDS)
readline.set_completer_delims(' \t\n;')
readline.parse_and_bind("tab:complete")
readline.set_completer(comp.complete)


def interactive_loop():
    while 1:
        sys.stdout.write(HEADER+comp.mode+OKGREEN+" > "+ENDC)
        user_input = raw_input()
        splitted_command = user_input.partition(' ')
        command, rest = splitted_command[0], splitted_command[2]
        if command in COMMANDS[comp.mode].keys():
            next_mode = COMMANDS[comp.mode][command](rest)
            if next_mode != '':
                comp.mode = next_mode


if __name__ == '__main__':
    arguments = docopt(__doc__, version='Unix Cli Template 0.1')
    print "Going to print a debug of the arguments passed"
    # returns a dictionary/hash with the options filled by the user
    print(arguments)
    print "End of printing"
    """
    For instance:
    python cli_template.py test this bob #will return

    {'--help': False,
    '--version': False,
    '<name>': ['bob'],
    '<x>': None,
    '<y>': None,
    'more': False,
    'test': True,
    'this': True}
    """
    # here goes the parsing of arguments
    if arguments['--interactive'] is True:
        print "Entering interactive mode, press <TAB> for completion"
        interactive_loop()
