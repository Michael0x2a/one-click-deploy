#!/usr/bin/env python
'''
This is a tool meant to help FRC teams easily download their C++ code from their repository,
compile it, deploy it to the robot, and modify IP address settings. This tools is primarily
meant to assist those who don't know much about using WindRiver/mucking around with IP Addresses.

You must run this program in administrator mode if you want to deploy code. 

See readme.md for more information.

Warning: this is in a very pre-Alpha stage, and may not function reliably.
'''

__prog__ = 'One Click Deploy'
__author__ = 'Michael Lee (michael.lee.0x2a@gmail.com)'
__license__ = '''The MIT License (MIT)
Copyright (c) 2012 The Spartabots

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
__version__ = 'December 29, 2012 (version 4)'

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