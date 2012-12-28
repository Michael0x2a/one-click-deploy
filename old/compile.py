#!/usr/bin/env python

import sys
import os
import subprocess
    
import utils

def generate_compile_file(options):
    utils.log('Generating temporary compilation file')
    with open(utils.get(r'resources', r'template'), 'r') as f:
        template = f.read()
    bat_file = template.format(
        windriver=options.windriver_install_dir, 
        wind_base=options.wind_base, 
        working_dir=utils.get(options.download_target, options.build_target))
    with open(r'compile.bat', 'w') as f:
        f.write(bat_file)
        
def run_compile_file():
    utils.log('Starting compilation')
    p = subprocess.Popen(
        utils.get(r'compile.bat'), 
        shell=True, 
        stdout=sys.__stdout__, 
        cwd=os.getcwd())
        
def remove_compile_file():
    utils.log('Deleting temporary compilation file')
    os.remove(utils.get(r'compile.bat'))
    
def compile(options):
    generate_compile_file(options)
    run_compile_file()
    remove_compile_file()

    