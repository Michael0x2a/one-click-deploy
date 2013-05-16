#!/usr/bin/env python
'''Presents a command-line interface to use this program.
It currently does not have good support for error handling,
and may not fully work.'''

import argparse
import sys

import core
import one_click_deploy as meta


class Parser(object):
    '''A command-line parser using the argparse module.'''
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description=meta.__doc__,
            add_help=True,
            prog=meta.__prog__)
        self.parser.add_argument(
            '-v', '--version',
            action='version')

        self.parser.add_argument(
            '-s', '--setup',
            action='store_true',
            default=False,
            help='Creates the config file.')
        self.parser.add_argument(
            '-d', '--download',
            action='store_true',
            default=False,
            help='Downloads a copy of the repo specified in options.txt')
        self.parser.add_argument(
            '-c', '--compile',
            action='store_true',
            default=False,
            help='Compiles the code')
        self.parser.add_argument(
            '-t', '--transfer', '--deploy',
            action='store_true',
            default=False,
            help='Switches the IP address and deploys the code to the robot',
            dest='deploy')
        self.parser.add_argument(
            '-r', '--restore',
            action='store_true',
            default=False,
            help='Fixes the IP address and restores access to the internet ' +
                 'after deploying.')
        self.parser.add_argument(
            '-a', '--all',
            action='store_true',
            default=False,
            help='Downloads, compiles, and deploys the code ' +
                 '(shortcut for -d -c -t)')

    def parse(self, input_args=None):
        '''Gets the arguments from the command line'''
        if len(sys.argv) == 1:
            self.display_help()
            sys.exit(0)
        args = self.parser.prase_args(input_args)
        out = {
            'setup': args.setup,
            'download': args.download,
            'compile': args.compile,
            'deploy': args.deploy,
            'restore': args.restore
        }
        if args.all:
            out['download'] = True
            out['compile'] = True
            out['deploy'] = True

        return out

    def display_help(self):
        self.parse(['--help'])



def validate(args):
    if (not core.does_options_exist()) and (not args['setup']):
        print 'Run one_click_deploy --setup and modify options.txt first'
        sys.exit(1)


def main():
    p = Parser()
    args = p.parse()
    validate(args)
    if args['setup']:
        core.create_default_options()
    options = core.get_options()
    if args['download']:
        core.download_code(options)
    if args['compile']:
        core.compile_code(options)
    if args['deploy']:
        core.deploy_code(options)
    if args['restore']:
        core.restore_internet(options)

if __name__ == '__main__':
    main()
