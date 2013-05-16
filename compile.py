#!/usr/bin/env python
'''
Contains code to generate a batch file which uses the compiler installed
with WindRiver and compiles the code in the target directory. Also
creates the makefile (using `makefile.py`
'''

import os
import os.path
import subprocess
import shutil

import makefile


class MissingWrmakefile(Exception):
    '''Each project should contain a `.wrmakefile` file created by
    the WindRiver IDE. Raise this exception if that file does
    not exist.'''
    pass


class CompilationError(Exception):
    '''Raise this error if the compiler was unable to compile the
    file.'''
    pass


def remove_old_files(options):
    '''Removes the folder containing the temporary build files'''
    path = os.path.join(
        options.repo_download_dir,
        options.build_target)
    if os.path.exists(path):
        shutil.rmtree(path)


def create_makefile(options):
    '''Creates a makefile, using the specified options and the 
    `.wrmakefile` file. Each WindRiver project has a unique 
    makefile'''
    wrmakefile_path = os.path.join(options.repo_download_dir, '.wrmakefile')
    if not os.path.isfile(wrmakefile_path):
        raise MissingWrmakefile('".wrmakefile" is missing from project.')
    make = makefile.generate_makefile(options)
    build_dir = '{0}/{1}'.format(
        options.repo_download_dir, options.build_target)
    path = build_dir + '/Makefile'
    if not os.path.exists(build_dir):
        os.makedirs(build_dir)
    with open(path, 'w') as handle:
        handle.write(make)


def create_compilation_file(options):
    '''Creates a batch file that will run the compiler. I'm 
    choosing not to run it from Python directly so that I
    don't have to debug how Python interfaces with Windows and
    various environment variables.'''
    working_dir = '{0}/{1}'.format(
        options.repo_download_dir,
        options.build_target)
    with open(r'resources/compile_bat.txt', 'r') as file:
        template = file.read()
    bat_file = template.format(
        windriver=options.windriver_install_dir,
        wind_base=options.wind_base,
        working_dir=working_dir)
    with open('compile.bat', 'w') as file:
        file.write(bat_file)


def run_compilation_file():
    '''Runs the batch file created by running `create_compilation_file`.
    This method will block until the batch file is finished running 
    (which can take up to a minute, at worst)'''
    process = subprocess.Popen(
        'compile.bat',
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=os.getcwd())
    stdout, stderr = process.communicate()
    with open('log.txt', 'w') as f:
        f.write('STDOUT:\n' + stdout + '\n\n\nSTDERR:\n' + stderr)
    no_recog = "'make' is not recognized"
    if stdout.startswith(no_recog) or stderr.startswith(no_recog):
        raise CompilationError(
            'Error: could not compile. Make sure the WindRiver ' +
            'install dir is configured properly, and all ' +
            'options are correctly set.')
    if stderr != '':
        error_message = 'Error: could not compile. See "log.txt" ' +\
                         'for full stack trace.\nStack Trace:\n{0}'
        error_message = error_message.format(stderr).replace('\n', '\n\n')
        raise CompilationError(error_message)


def remove_compilation_file():
    '''Removes the batch file created by 'create_compilation_file`'''
    os.remove('compile.bat')


def validate_compile(options):
    '''Confirms that the compiler successfully finished by checking
    for the presence of a binary executable.'''
    path = os.path.join(
        options.repo_download_dir,
        options.build_target,
        options.binary_name,
        'Debug',
        options.binary_name + '.out')
    if not os.path.isfile(path):
        raise CompilationError(
            'Error: final exe was not created. Compilation may ' +
            'have failed. See "log.txt"')


def compile_code(options):
    '''The "master function" of this entire module. It runs all the above
    functions in one step, in the proper order. Specifically, it cleans
    up (if it needs to) the results of any old compile, generates a makefile
    and compiles the program, validates to make sure it worked, and 
    remove any temporary or garbage files.'''
    remove_old_files(options)
    create_makefile(options)
    create_compilation_file(options)
    run_compilation_file()
    validate_compile(options)
    remove_compilation_file()
