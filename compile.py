#!/usr/bin/env python

import sys
import os
import os.path
import subprocess
import shutil
import StringIO

import makefile

class MissingWrmakefile(Exception): pass
class CompilationError(Exception): pass

def remove_old_files(options):
    path = os.path.join(
        options.repo_download_dir,
        options.build_target)
    if os.path.exists(path):
        shutil.rmtree(path)

def create_makefile(options):
    if not os.path.isfile(os.path.join(options.repo_download_dir, '.wrmakefile')):
        raise MissingWrmakefile('".wrmakefile" is missing from project.')
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
    p = subprocess.Popen(
        'compile.bat',
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=os.getcwd())
    stdout, stderr = p.communicate()
    with open('log.txt', 'w') as f:
        f.write('STDOUT:\n' + stdout + '\n\n\nSTDERR:\n' + stderr)
    if stdout.startswith("'make' is not recognized") or stderr.startswith("'make' is not recognized"):
        raise CompilationError('Error: could not compile. Make sure the WindRiver install dir is configured properly, and all options are correctly set.')
    if stderr != '':
        raise CompilationError('Error: could not compile. See "log.txt" for full stack trace.\nStack Trace:\n{0}'.format(stderr).replace('\n', '\n\n'))
        
    
def remove_compilation_file():
    os.remove('compile.bat')
    
def validate_compile(options):
    path = os.path.join(
        options.repo_download_dir,
        options.build_target,
        options.binary_name,
        'Debug',
        options.binary_name + '.out')
    if not os.path.isfile(path):
        raise CompilationError('Error: final exe was not created. Compilation may have failed. See "log.txt"')
    
def compile_code(options):
    remove_old_files(options)
    create_makefile(options)
    create_compilation_file(options)
    run_compilation_file()
    validate_compile(options)
    remove_compilation_file()
    