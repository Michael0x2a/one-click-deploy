#!/usr/bin/env python

import utils

class Options(dict):
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__

class InvalidConfigFile(Exception): pass
    
def get_config_values():
    utils.log('Obtaining config values')
    op = Options()
    with open(utils.get(r'config.txt')) as f:
        for line in f:
            if line.startswith('#'):
                continue
            line = line.strip()
            if line == '':
                continue
            if r'=' not in line:
                raise InvalidConfigFile('"{0}" is invalid'.format(raw_line))
            key, value = line.split('=')
            key = key.strip()
            value = value.strip()
            if value in (r'?', ''):
                raise InvalidConfigFile('"{0}" is invalid'.format(raw_line))
            op[key] = value
    return op
    

    