#!/usr/bin/env python

import sys
import os
import re
import ftplib
import socket
import subprocess

import wmi


class ConnectionError(Exception):
    pass


class NotWindows(Exception):
    pass


class NetworkConnectionError(Exception):
    pass


def get_network_adapter_obj(mac_address):
    mac_address = mac_address.replace('-', ':')
    nic_configs = wmi.WMI().Win32_NetworkAdapterConfiguration(MACAddress=mac_address)
    return nic_configs[0]


def handle_error_code(code):
    error_codes = {
        0: "Successful completion, no reboot required.",
        1: "Successful completion, reboot required.",
        64: "Method not supported on this platform.",
        65: "Unknown failure.",
        66: "Invalid subnet mask.",
        67: "An error occured while processing an instance that was returned.",
        68: "Invalid input parameter.",
        69: "More then five gateways specified.",
        70: "Invalid IP address.",
        71: "Invalid gateway IP address",
        72: "An error occured while accessing the registry for " +
            "the requested information",
        73: "Invalid domain name",
        74: "Invalid host name",
        75: "No primary or secondary WINS server defined.",
        76: "Invalid file.",
        77: "Invalid system path",
        78: "File copy failed.",
        79: "Invalid security parameter.",
        80: "Unable to configure TCP/IP service.",
        81: "Unable to configure DHCP service.\nTry running program as " +
            "an administrator?",
        82: "Unable to renew DHCP lease.",
        83: "Unable to release DHCP lease.",
        84: "IP not enabled on adapter.",
        85: "IPX not enabled on adapter.",
        86: "Frame or network number bounds error.",
        87: "Invalid frame type.",
        88: "Invalid network number.",
        89: "Duplicate network number.",
        90: "Parameter out of bounds.",
        91: "Access denied.",
        92: "Out of memory.",
        93: "Already exists.",
        94: "Path, file, or object not found.",
        95: "Unable to notify service.",
        96: "Unable to notify DNS service.",
        97: "Interface not configurable.",
        98: "Not all DHCP leases could be released or renewed.",
        100: "DHCP not enabled on adapter.",
        -2147180508: "Try running program as an administrator?\nIs the " +
            "'Network Connections Properties currently open? Try closing it."
    }
    code = code[0]
    if code == 0:
        return
    else:
        if code not in error_codes:
            code = -1
            message = 'Unknown error.\nTry running program as = + \
                administrator.\nSee ' + \
                'http://msdn.microsoft.com/en-us/library/' + \
                'aa390383%28v=VS.85%29.aspx' + \
                '\nor: ' + \
                'http://msdn.microsoft.com/en-us/library/' + \
                'aa390378%28v=VS.85%29.aspx' + \
                '\n...for info on error codes.'
        if code in error_codes:
            message = error_codes[code]
        raise ConnectionError('Error code {0}: {1}'.format(code, message))


def switch_to_internet(mac_address):
    nic = get_network_adapter_obj(mac_address)
    return_code = nic.EnableDHCP()
    handle_error_code(return_code)


def switch_to_robot(mac_address, ip_address, subnet_mask='255.0.0.0'):
    nic = get_network_adapter_obj(mac_address)
    return_code = nic.EnableStatic(
        IPAddress=[ip_address], SubnetMask=[subnet_mask])
    handle_error_code(return_code)


def split_team_number(team_number):
    num = int(team_number, 10)
    top = str(num // 100)
    bottom = str(num % 100)
    return top, bottom


def get_robot_ip(form, team_number):
    top, bottom = split_ip(team_number)
    return '10.{0}.{1}.2'.format(top, bottom)


def get_connection_options():
    if sys.platform != 'win32':
        raise NotWindows(
            "Could not enumerate mac addresses. " +
            "This program is currently windows only")

    pattern = re.compile(r'\"(.+)\",\"(.+)\",\"(.+)\",\"(.+)\"')
    ethernet = {}
    wireless = {}
    command = 'getmac /v /fo CSV /nh'
    # Gets MAC addresses in verbose format, in CSV form, with no headers.
    for line in os.popen(command):
        out = pattern.match(line)
        components = out.groups()
        connection_name = components[0]
        network_adapter = components[1]
        physical_address = components[2]
        transport_name = components[3]
        name = connection_name.lower()
        if 'ethernet' in name:
            ethernet[network_adapter] = physical_address
        elif 'wi-fi' in name or 'wifi' in name or 'wireless' in name:
            wireless[network_adapter] = physical_address
    connections = {
        'ethernet': ethernet,
        'wireless': wireless
    }
    return connections


def restore_internet(options):
    if options.wireless_mac_address.lower() != 'none':
        switch_to_internet(options.wireless_mac_address)


def connect_to_robot(options):
    top, bottom = split_team_number(options.team_number)
    if options.wireless_mac_address.lower() != 'none':
        switch_to_robot(
            options.wireless_mac_address, '10.{0}.{1}.42'.format(top, bottom))
    if options.ethernet_mac_address.lower() != 'none':
        switch_to_robot(
            options.ethernet_mac_address, '10.{0}.{1}.6'.format(top, bottom))

    p = subprocess.Popen(
        'netsh wlan connect {0}'.format(options.robot_network_name),
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=os.getcwd())
    stdout, stderr = p.communicate()
    if not 'Connection request was completed successfully.' in stdout:
        raise NetworkConnectionError(
            'Unable to connect to {0}. Please manually connect.'.format(
                options.robot_network_name))


def deploy_code(options):
    top, bottom = split_team_number(options.team_number)
    ip = '10.{0}.{1}.2'.format(top, bottom)
    try:
        ftp = ftplib.FTP(ip)
    except socket.error:
        raise ConnectionError(
            'Could not connect to robot. Check your team number, robot ' +
            'network name, adapters, and ip addresses')
    ftp.login()
    binary = os.path.join(
        options.repo_download_dir,
        options.build_target,
        options.binary_name,
        'Debug',
        options.binary_name + '.out')
    command = 'STOR ni-rt/system/FRC_UserProgram.out'
    ftp.storbinary(command, open(binary, 'rb'))
