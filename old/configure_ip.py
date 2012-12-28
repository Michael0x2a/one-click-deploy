#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
configure_ip.py

Configures the laptop to connect to the robot (wirelessly or via ethernet, or 
to the internet without having to muck around with the settings. You MUST run 
this program as an administrator.

Usage:
    python configure_ip.py (wireless|ethernet|internet)
    python configure_ip.py --help
    python configure_ip.py --version

See <http://stackoverflow.com/q/7580834> for more information.
'''

from __future__ import print_function

import sys
import argparse

import utils

try:
    import win32api
except ImportError:
    utils.log('You need to install "pywin32", a 3rd-party Python module.', 'ERROR')
    utils.log('See http://sourceforge.net/projects/pywin32/', 'ERROR')
    utils.exit(-1)

try:
    import wmi
except ImportError:
    utils.log('You need to install "wmi", a 3rd-party Python module.', 'ERROR')
    utils.log('See http://pypi.python.org/pypi/WMI/', 'ERROR')
    utils.exit(-1)

__date__ = r'November 24, 2012 (version 3)'

__author__ = r'Michael Lee'
__email__ = r'michael.lee.0x2a@gmail.com'
__license__ = r'GPL'


def get_console_arguments():
    '''Gets options from the command line.'''
    if len(sys.argv) < 2 or ('--help' in sys.argv):
        print(__doc__)
        sys.exit(0)
    elif '--version' in sys.argv:
        print(__date__)
        sys.exit(0)
        
    option = sys.argv[1]
    if option not in ('wireless', 'ethernet', 'internet'):
        print(__doc__)
        sys.exit(0)
        
    return option
        
def _get_network_adaptor(args={}):
    nic_configs = wmi.WMI().Win32_NetworkAdapterConfiguration(**args)
    return nic_configs[0]

def _handle_return_code(code):
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
        72: "An error occured while accessing the registry for the requested information",
        73: "Invalid domain name",
        74: "Invalid host name",
        75: "No primary or secondary WINS server defined.",
        76: "Invalid file.",
        77: "Invalid system path",
        78: "File copy failed.",
        79: "Invalid security parameter.",
        80: "Unable to configure TCP/IP service.",
        81: "Unable to configure DHCP service.",
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
        100: "DHCP not enabled on adapter."
    }
    code = code[0]
    if code == 0:
        print('Success!')
    else:
        print('Error:', code)
        if code in error_codes:
            print(error_codes[code])
        else:
            print('Unknown error')
            
        # Special cases:
        if code in (81, -2147217405):
            print('Try running batch script as administrator?')
        if code in (-2147180508,):
            print('Is the "Network Connections Properties" window currently open?  Try closing it.')
        print('\nSee http://msdn.microsoft.com/en-us/library/aa390383%28v=VS.85%29.aspx',
              'or: http://msdn.microsoft.com/en-us/library/aa390378%28v=VS.85%29.aspx',
              '...for info on error codes.', sep='\n')
    
    return

def switch_to_internet(mac_address):
    nic = _get_network_adaptor({"MACAddress": mac_address})
    return_code = nic.EnableDHCP()
    _handle_return_code(return_code)
    return

def switch_to_robot(
        mac_address,
        ip,
        subnet_mask=u'255.255.255.0',
        gateway=u'10.29.76.1'):
    nic = _get_network_adaptor({"MACAddress": mac_address})
    return_code = nic.EnableStatic(IPAddress=[ip], SubnetMask=[subnet_mask])
    _handle_return_code(return_code)
    return

def main():
    command = get_console_arguments()
    print('Switching to {0}.\n'.format(command))
    if command == 'internet':
        switch_to_internet(WIRELESS_MAC)
    elif command == 'ethernet':
        switch_to_robot(ETHERNET_MAC, ETHERNET_IP)
    elif command == 'wireless':
        switch_to_robot(WIRELESS_MAC, WIRELESS_IP)
    return

if __name__ == '__main__':
    main()
