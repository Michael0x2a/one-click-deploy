#!/usr/bin/env python

import os
import shutil
import re
import urlparse
import urllib2

import pysvn

class InvalidUrl(Exception): pass
class InaccessibleUrl(Exception): pass
class InvalidRevision(Exception): pass

def does_code_exist(options):
    return os.path.exists(options.repo_download_dir)

def remove_old(options):
    if os.path.exists(options.repo_download_dir):
        shutil.rmtree(options.repo_download_dir)

def validate_url(url):
    try:
        code = urllib2.urlopen(url).code
    except ValueError:
        raise InvalidUrl('Source code url is malformed or missing')
    except urllib2.HTTPError as e:
        raise InaccessibleUrl('Source code url cannot be reached: {0} is returning an "{1}" error'.format(url, str(e)))
    
def validate_revision(revision):
    if revision.lower() == 'latest':
        return
    try:
        revision = int(revision)
    except ValueError:
        raise InvalidRevision('Revision is not a number')

def download_source(options):
    validate_url(options.repo_target_url)
    validate_revision(options.repo_target_revision)
    
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
    
    