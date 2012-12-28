#!/usr/bin/env python

import os.path
import shutil

class Options(dict):
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    
class InvalidConfigFile(Exception): pass
class ConfigurationMissing(Exception): pass

def parse_options(raw_text):
    op = Options()
    for line in raw_text.split('\n'):
        line = line.strip()
        if line.startswith('#') or line == '':
            continue
        if '=' not in line:
            raise InvalidConfigFile('"{0}" is invalid'.format(line))
        
        key, value = line.split('=')
        key, value = key.strip(), value.strip()
        if value in ('?', ''):
            value = ''
            
        op[key] = value
    return op

def get_default():
    with open(r'resources/default_options.txt') as f:
        raw_text = f.read()
    return raw_text
    
def does_options_exist():
    return os.path.isfile('options.txt')
    
def create_default_options():
    raw_text = get_default()
    with open('options.txt', 'w') as f:
        f.write(raw_text)
    
def get_options():
    if os.path.isfile('options.txt'):
        with open('options.txt') as f:
            raw_text = f.read() 
    else:
        raise ConfigurationMissing('options.txt is missing')
    return parse_options(raw_text)
    
def save_options(options):
    if not does_options_exist():
        create_default_options()
    with open('resources/default_options.txt') as f:
        actual = f.read().split('\n')
    out = []
    for line in actual:
        line = line.strip()
        if line.startswith('#') or line == '':
            out.append(line)
            continue
        key, value = line.split('=')
        key, value = key.strip(), value.strip()
        if key in options:
            value = options[key].strip()
        out.append('{0} = {1}'.format(key, value))
    with open('options.txt', 'w') as f:
        f.write('\n'.join(out))
        