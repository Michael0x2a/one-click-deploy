#!/usr/bin/env python

import sys
import os
import os.path
import subprocess

import makefile

def create_makefile(options):
    m = makefile.generate_makefile(options)
    build_dir = '{0}/{1}'.format(options.repo_download_dir, options.build_target)
    path = build_dir + '/Makefile'
    if not os.path.exists(build_dir):
        os.makedirs(build_dir)
    with open(path, 'w') as f:
        f.write(m)
    
def create_compilation_file(options):
    with open(r'resources/compile_bat.txt', 'r') as f:
        template = f.read()
    bat_file = template.format(
        windriver = options.windriver_install_dir,
        wind_base = options.wind_base,
        working_dir = '{0}/{1}'.format(options.repo_download_dir, options.build_target))
    with open('compile.bat', 'w') as f:
        f.write(bat_file)
    
def run_compilation_file():
    with open('log.txt', 'w') as f:
        subprocess.call(
            'compile.bat',
            shell=True,
            stdout=f,
            cwd=os.getcwd())
    
def remove_compilation_file():
    os.remove('compile.bat')
    
def compile_code(options):
    create_makefile(options)
    create_compilation_file(options)
    run_compilation_file()
    remove_compilation_file()
    