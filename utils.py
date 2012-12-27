#!/usr/bin/env python

import sys
import os
import os.path
import ctypes

LOG_LEVEL = 'NORMAL'

def get(*path):
    return os.path.join(os.getcwd(), *path)
    
def split_ip(team_number):
    num = int(team_number, 10)
    top = num // 100
    bottom = num % 100
    return top, bottom
    
def get_ip(form, team_number):
    top, bottom = split_ip(team_number)
    top = str(top)
    bottom = str(bottom)
    return form.format(top, bottom)

def echo(text, color='white'):
    colors = {
        'black': 0,
        'dark_blue': 1,
        'dark_green': 2,
        'dark_cyan': 3,
        'dark_red': 4,
        'dark_purple': 5,
        'dark_yellow': 6,
        'light_gray': 7,
        'dark_gray': 8,
        'blue': 9,
        'green': 10,
        'cyan': 11,
        'red': 12,
        'purple': 13,
        'yellow': 14,
        'white': 15
    }
    ctypes.windll.Kernel32.GetStdHandle.restype = ctypes.c_ulong
    h = ctypes.windll.Kernel32.GetStdHandle(ctypes.c_ulong(0xfffffff5))
    ctypes.windll.Kernel32.SetConsoleTextAttribute(h, colors[color])
    print text
    ctypes.windll.Kernel32.SetConsoleTextAttribute(h, colors['light_gray'])
    
def log(text, level='NORMAL'):
    levels = {
        'INFO': (0, 'white'),
        'DEBUG': (1, 'white'),
        'NORMAL': (2, 'green'),
        'ALERT': (3, 'cyan'),
        'ERROR': (4, 'red')
    }
    rank, color = levels[level]
    log_rank, _ = levels[LOG_LEVEL]
    if rank >= log_rank:
        echo(text, color)
        
def exit(error=0):
    echo('Press [Enter] to end the program', 'cyan')
    raw_input()
    sys.exit(0)