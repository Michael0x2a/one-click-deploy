#!/usr/bin/env python
'''
This class provides a convenient interface for all the major functions
and tasks this program performs.
'''
import options
import repo
import compile
import deploy

def does_options_exist():
    return options.does_options_exist()

def create_default_options():
    options.create_default_options()
    
def get_options():
    return options.get_options()

def save_options(op):
    options.save_options(op)
    
def does_code_exist(op):
    repo.does_code_exist(op)
    
def get_download_choices(op):
    repo.get_download_choices(op)
    
def download_code(op):
    repo.download_source(op)
    
def compile_code(op):
    compile.compile_code(op)
    
def get_connection_options():
    return deploy.get_connection_options()

def deploy_code(op):
    deploy.deploy_code(op)
    
def restore_internet(op):
    deploy.restore_internet(op)