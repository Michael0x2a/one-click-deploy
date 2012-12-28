#!/usr/bin/env python
'''
one_click_deploy.py

Downloads, compiles, and deploys the robot code in one click. Assumes that WindRiver has been
properly installed, and that the config.txt file has been properly set.

Usage:
    python one_click_deploy.py
'''

import sys
import os.path
import ftplib

try:
    import win32com.shell.shell as shell
except ImportError:
    utils.log('You need to install "pywin32", a 3rd-party Python module.', 'ERROR')
    utils.log('See http://sourceforge.net/projects/pywin32/', 'ERROR')
    utils.exit(-1)

import configure
import source
import generate_makefile
import compile
import deploy
import utils

__date__ = r'December 26, 2012 (version 1)'

__author__ = r'Michael Lee'
__email__ = r'michael.lee.0x2a@gmail.com'
__license__ = r'GPL'


def run_confirmation():
    utils.echo('Please confirm that you have completely configured "config.txt"', 'cyan')
    utils.echo('Press [Enter] when ready to proceed', 'cyan')
    raw_input()

def main():
    utils.log('Starting one_click_deploy')
    run_confirmation()
    
    options = configure.get_config_values()
    #source.download_code(options)
    generate_makefile.generate_makefile(options)
    #compile.compile(options)
    #deploy.deploy(options)
    
    utils.log('Done!')
    
if __name__ == '__main__':
    main()