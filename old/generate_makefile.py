#!/usr/bin/env python

import os
import utils

# I need...
# The project root directory
# CPP_PROJECT_ROOT_DIR --> options.download_target
# 
# The workspace root directory
# CPP_PROJECT_WS_ROOT_DIR --> utils.get('.')
#
# The project name
# CPP_PROJECT_NAME --> options.binary_name

def get_wrmakefile(options):
    with open(utils.get(options.download_target, r'.wrmakefile'), 'r') as f:
        wrmakefile = f.read()
    return wrmakefile
    
def generate_headers():
    with open(utils.get(r'resources', r'makefile_header.txt'), 'r') as f:
        header = f.read()
    return header
    
def generate_common(options):
    with open(utils.get(r'resources', r'makefile_common.txt'), 'r') as f:
        common = f.read()
    return common

def generate_individual(options):
    def get_cpp_files(options):
        file_names = []
        for root, dirs, files in os.walk(options.download_target):
            base = ''
            if root != options.download_target:
                base = root[2:] + r'/'
            file_names += [base + f[:-4] for f in files if f[-4:] == '.cpp']
        file_names.sort()
        return file_names
    
    individual = []
    files = get_cpp_files(options)
    
    with open(utils.get(r'resources', r'makefile_individual.txt'), 'r') as f:
        template = f.read()
    
    for file in files:
        individual.append(template.replace('{filename}', file))
    return '\n'.join(individual)
        
def replace_placeholders(makefile):
    makefile = makefile.format(
        project_name=utils.get(options.binary_name),
        project_directory=utils.get(options.download_target),
        workspace_directory=utils.get('.'))
    return makefile
    
def generate_makefile(options):
    print generate_individual(options)
    