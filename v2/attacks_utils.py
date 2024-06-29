'''
Utils functions for the attack
'''

import os

from subprocess import DEVNULL, STDOUT, check_call, call
from time import sleep
from get_nic import getnic
from simple_term_menu import TerminalMenu

from constants import console 


def set_monitor_mode(selected_interface, specified_channel=None):
    '''
    '''
    # set the sepecified channel
    channel = ''
    if specified_channel:
        channel = f' {specified_channel}'

    console.print(f'[info]Preparing interface #################################################')
    # kill conlicting networks methods 
    os.system(f'airmon-ng check kill')
    # stop the interface
    os.system(f'sudo airmon-ng stop {selected_interface}')
    # put selected interface to monitor mode
    os.system(f'sudo airmon-ng start {selected_interface}{channel}')
    console.print(f'[good]Interface changed to monitor mode')
    console.print(f'[info]Interface prepared #################################################')
    sleep(2)



def show_and_select_available_interfaces():
    '''
    '''
    # get the interfaces
    with console.status("[bold green]Getting avaliable interfaces...") as status:
        console.log(status)
        # get avalible interfaces
        interfaces = getnic.interfaces()
    # construct the menu
    interfaces_menu = TerminalMenu(interfaces)
    # show the options and get the selected interface
    selected_interface_index = interfaces_menu.show()
    # get interface 
    selected_interface = interfaces[selected_interface_index]
    # show selected interface
    console.print("Selected interface: ", selected_interface) 
    sleep(2)
    # set to monitor mode
    set_monitor_mode(selected_interface)
    # retuirn the seleted interface
    return selected_interface

#########################################################################################

def show_available_networks(selected_interface):
    '''
    '''
    # call the function to see avalible networks
    call(['xterm', '-e', f'sudo airodump-ng --band a {selected_interface}'])


def monitor_selected_network(selected_interface, selected_network, selected_channel):
    '''
    '''
    # call the function to monitor selected network
    call(['xterm', '-e', f'sudo airodump-ng --band a -c {selected_channel} --bssid {selected_network} {selected_interface}'])


def clean_interface(selected_interface):
    '''
    '''
    console.print(f'[info]Clean interface #################################################')
    with console.status("[bold green]Working on cleaning...") as status:
        console.log(status)
        console.print(f'[info]Setting interface to managed mode')
        # kill subprocess
        os.system(f'sudo airmon-ng check kill')
        # stop the monitor mode
        os.system(f'sudo airmon-ng stop {selected_interface}')
        # restart the network manager
        os.system(f'sudo service NetworkManager restart')
    console.print('[good]Cleaning finished')
    sleep(2)

#############################################################################


