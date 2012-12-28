#!/usr/bin/env python

import ftplib

import configure_ip
import utils
    
def set_ip_address(options):
    utils.log('Setting IP Address')
    wireless_ip = utils.get_ip('10.{0}.{1}.42', options.team_number)
    ethernet_ip = utils.get_ip('10.{0}.{1}.6', options.team_number)

    if options.wireless_mac_address != '[None]':
        configure_ip.switch_to_robot(
            options.wireless_mac_address,
            wireless_ip)
    if options.ethernet_mac_address != '[None]':
        configure_ip.switch_to_robot(
            options.ethernet_mac_address,
            ethernet_ip)
    
def connect_to_network(options):
    utils.echo("Please connect to network {0}.".format(options.robot_network_name), 'red')
    utils.echo('Hit [enter] when done.', 'red')
    
def transfer_file(options):
    utils.log('Transfering code to robot')
    target_ip = utils.get_ip('10.{0}.{1}.2', options.team_number)
    ftp = ftplib.FTP(target_ip)
    binary = utils.get(
        options.download_target, 
        options.build_target, 
        options.binary_name,
        r'Debug',
        options.binary_name + r'.out')
    command = 'STOR {0}'.format(binary)
    ftp.storbinary(command, open(binary, 'rb'))
    
def restore_internet(options):
    utils.log('Restoring access to internet')
    if options.wireless_mac_address != '[None]':
        configure_ip.switch_to_internet(options.wireless_mac_address)
    if options.ethernet_mac_address != '[None]':
        configure_ip.switch_to_internet(options.ethernet_mac_address)
    
def deploy(options):
    set_ip_address(options)
    connect_to_network(options)
    transfer_file(options)
    #restore_internet(options)
    pass
    
    