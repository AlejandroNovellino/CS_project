import os
import subprocess
import asyncio
import pyrcrack

from get_nic import getnic
from rich.console import Console
from rich.prompt import Prompt


async def scan_for_targets(interface, console):
    """Scan for targets, return json."""
    airmon = pyrcrack.AirmonNg()

    async with airmon(interface) as mon:
        async with pyrcrack.AirodumpNg() as pdump:
            async for result in pdump(mon.monitor_interface):
                console.print(result.table)
                await asyncio.sleep(2)


def cleaning(selected_interface):
    print(f'\nCleaning ---------------------------------')
    print(f'Setting interface to managed mode')
    os.system(f'sudo airmon-ng stop {selected_interface}')
    print(f'Ended')

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

# select the interface
selected_interface = interfaces[selected_interface_index]
print(f'\nSelected interface {selected_interface}')
print(f'Interface changed to monitor mode')

'''
# put selected interface to monitor mode
os.system(f'sudo airmon-ng start {selected_interface}')
'''

 
# now scan the network
asyncio.run(scan_for_targets(selected_interface, console))

# user select the network to attack
print('\nSelect your network to attack (BSSID)')
network_to_attack = int(input())
print(f'\nSelected network to attack {network_to_attack}')

# closing so clean everything
#cleaning(selected_interface)
