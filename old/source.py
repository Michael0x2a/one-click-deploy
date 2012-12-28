#!/usr/bin/env python

import os
import os
import shutil

import utils

# 3rd-party modules:
try:
    import pysvn
except ImportError:
    utils.log('You need to install "pysvn", a 3rd-party Python module.', 'ERROR')
    utils.log('See http://pysvn.tigris.org', 'ERROR')
    utils.exit(-1)
    
def clear(options):
    if os.path.exists(options.download_target):
        utils.log('Removing old code')
        shutil.rmtree(utils.get(options.download_target))
    
def transfer_source(options):
    utils.log('Downloading files from {0}'.format(options.download_url))
    client = pysvn.Client()
    
    if options.download_revision.lower() == 'latest':
        client.checkout(options.download_url, utils.get(options.download_target))
    else:
        client.checkout(options.download_url, utils.get(options.download_target), 
                        revision=pysvn.Revision(pysvn.opt_revision_kind.number, 
                                                int(options.download_revision)))
    
def add_makefile(options):
    utils.log('Adding makefile')
    target_path = utils.get(options.download_target, options.build_target)
    makefile_path = utils.get(options.download_target, options.build_target, r'Makefile')
    if not os.path.exists(target_path):
        os.makedirs(target_path)
    if not os.path.isfile(makefile_path):
        shutil.copyfile(utils.get(r'resources', r'Makefile'), makefile_path)
    
def download_code(options):
    clear(options)
    transfer_source(options)
    add_makefile(options)
