#!/usr/bin/env python

import os
import shutil
#import django.core.validators as validators
#import django.core.exceptions as exceptions

import pysvn

#class InvalidUrl(Exception): pass
#class InaccessibleUrl(Exception): pass
class InvalidRevision(Exception): pass

def does_code_exist(options):
    return os.path.exists(options.repo_download_dir)

def remove_old(options):
    if os.path.exists(options.repo_download_dir):
        shutil.rmtree(options.repo_download_dir)
 
''' 
def validate_url(url):
    malformed_val = validators.URLValidator(verify_exists=False)
    accessable_val = validators.URLValidator(verify_exists=True)
    ValidationError = exceptions.ValidationError
    try:
        malformed_val(url)
    except ValidationError:
        raise InvalidUrl('Source code url is malformed or missing')
    try:
        accessable_val(url)
    except ValidationError:
        raise InaccessibleUrl('Source code url cannot be reached')
    
def validate_revision(url, revision):
    if revision.lower() == 'latest':
        return
    try:
        revision = int(revision)
    except ValueError:
        raise InvalidRevision('Revision is not a number')
    client = pysvn.Client()
    latest = client.info(url).revision.number
    if revision > latest:
        raise InvalidRevision('Revision too high -- does not exist (type "latest" to get the latest revision)')
'''

def download_source(options):
    #validate_url(options.repo_target_url)
    #validate_revision(options.repo_target_url, options.repo_target_revision)
    
    client = pysvn.Client()
    
    if options.repo_target_revision.lower() == 'latest':
        client.checkout(
            options.repo_target_url,
            options.repo_download_dir)
    else:
        client.checkout(
            options.repo_target_url,
            options.repo_download_dir,
            revision = pysvn.Revision(
                pysvn.opt_revision_kind.number,
                int(options.repo_target_revision)))
                
def get_download_choices(options):
    output = [('Main Branch', '', options.repo_target_url)]
    raise Exception("Not yet implemented")
    return output
    
    