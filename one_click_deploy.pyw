#!/usr/bin/env python
'''
one-click-deploy

This is a tool meant to help FRC teams easily download their C++ code from their repository,
compile it, deploy it to the robot, and modify IP address settings. This tools is primarily
meant to assist those who don't know much about using WindRiver/mucking around with IP Addresses.

You must run this program in administrator mode if you want to deploy code. 

See readme.md for more information.

Warning: this is in a very pre-Alpha stage, and may not function reliably.

Usage:

To use the GUI, simply double-click and open the file.

To use the program from the command line, first run:

    one-click-deploy --setup
    
...then modify "options.txt" accordingly. The arguments you can then use are listed below.
'''

__prog__ = 'one-click-deploy'
__author__ = 'Michael Lee (michael.lee.0x2a@gmail.com)'
__license__ = 'MIT'
__version__ = 'December 28, 2012 (version 2)'

import sys

import console
import gui

def main():
    if len(sys.argv) == 1:
        gui.main()
    else:
        console.main()
        
if __name__ == '__main__':
    main()