'''
'''

from utils import *

# global vairable for selected interface
selected_interface = None

# sho welcome message
show_welcome()
# select the interface and set it to monitor mode
selected_interface = show_and_select_available_interfaces()

user_selected_option = 10000
while user_selected_option != 0:
    # show the main menu and let the user select what to do
    user_selected_option = show_menu()
    # select what attack to do
    select_attack(user_selected_option, selected_interface)

clean_interface(selected_interface)
show_goodbye()