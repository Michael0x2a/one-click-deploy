#!/usr/bin/env python
'''
The code used in this file was adapted from ucpp
'''

import os
import os.path


def get_cpp_files(code_dir):
    os.chdir(code_dir)
    file_names = []
    for root, dirs, files in os.walk('.'):
        base = ''
        if root != '.':
            base = root[2:] + r'/'
            base = base.replace('\\', '/')
        file_names += [base + f[:-4] for f in files if f[-4:] == '.cpp']
    os.chdir('..')
    file_names.sort()
    return file_names


def get_wrmakefile(options):
    wr_path = os.path.join(options.repo_download_dir, '.wrmakefile')
    with open(wr_path, 'r') as f:
        wrmakefile = f.read()
    return wrmakefile


def generate_headers(options):
    with open(os.path.join('resources', 'makefile_header.txt'), 'r') as f:
        header = f.read()
    return header


def generate_common(options):
    with open(os.path.join('resources', 'makefile_common.txt'), 'r') as f:
        common = f.read()
    return common


def generate_individual(files, options):
    individual = []

    with open(os.path.join('resources', 'makefile_individual.txt'), 'r') as f:
        template = f.read()

    for file in files:
        individual.append(template.replace('{filename}', file))

    return '\n'.join(individual)


def generate_linking(files, options):
    link_section = ['', 'OBJECTS_{project_name}_partialImage =']
    object_line = '\t {project_name}_partialImage/$(MODE_DIR)/Objects/' + \
                  '{project_directory}/{file}.o \\'
    first = True
    for file in files:
        if first:
            link_section[1] += object_line.replace('{file}', file)
            first = False
            continue
        link_section.append(object_line.replace('{file}', file))
    link_section[-1] = link_section[-1][:-2]
    link_section.append('')
    with open(os.path.join('resources', 'makefile_linking.txt'), 'r') as f:
        linking = f.read()
    link_section.append(linking)
    return '\n'.join(link_section)


def generate_dep_files(files, options):
    dep_section = ['force :\n\nDEP_FILES := \\']
    line = []
    template = "{project_name}_partialImage/$(MODE_DIR)/Objects/" + \
               "{project_name}/{file}.d "
    x = 0
    for file in files:
        this = template.replace('{file}', file)
        line.append(this)
        x += 1
        if x == 3:
            line.append('\\')
            dep_section.append('	' + ''.join(line))
            x = 0
    if x == 0:
        dep_section[-1] = dep_section[-1][:-2]
    dep_section.append('-include $(DEP_FILES)\n')
    return '\n'.join(dep_section)


def replace_placeholders(makefile, options):
    makefile = makefile.format(
        absolute_workspace_directory=os.getcwd(),
        project_name=options.binary_name,
        project_directory=options.repo_download_dir,
        workspace_directory='.')
    return makefile


def generate_makefile(options):
    files = get_cpp_files(options.repo_download_dir)

    header = generate_headers(options)
    common = generate_common(options)
    individual = generate_individual(files, options)
    link = generate_linking(files, options)
    dep_files = generate_dep_files(files, options)
    wrmakefile = get_wrmakefile(options)

    generated = common + individual + link + dep_files
    makefile = header + wrmakefile.replace('%IDE_GENERATED%', generated)

    makefile = replace_placeholders(makefile, options)
    return makefile
