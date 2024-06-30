'''
'''

from rich.markdown import Markdown
from simple_term_menu import TerminalMenu

from constants import console 

from attacks import *

def show_welcome():
    '''
    Show the welcome markdown
    '''
    console.clear()
    with open("welcome.md") as readme:
        markdown = Markdown(readme.read())
    console.print(markdown)


def show_goodbye():
    '''
    Show the goodbye markdown 
    '''
    console.clear()
    with open("goodbye.md") as readme:
        markdown = Markdown(readme.read())
    console.print(markdown)


def show_menu():
    '''
    Show the menu and options
    '''
    console.clear()
    with open("instructions.md") as readme:
        markdown = Markdown(readme.read())
    console.print(markdown)
    console.print()
    # menu options
    options = [
        'Exit',
        'Single target attack',
        'All targets attack',
        'Inteligent attack'
    ]
    # construct the menu
    options_menu = TerminalMenu(options)
    # show the options and get the selected interface
    selected_option_index = options_menu.show()
    # show selected interface
    console.print("Selected option: ", options[selected_option_index])
    # return the selected interface
    return selected_option_index

def select_attack(selected_option_index, selected_interface):
    '''
    Select the attack thanks to the option selected by user
    '''

    match selected_option_index:
        # single target attack
        case 0:
            pass
        # single target attack
        case 1:
            single_target_attack(selected_interface)
        # all targets attack
        case 2:
            all_targets_attack(selected_interface)
        case 3: 
            all_targets_attack_logistic_regression(selected_interface)

    return selected_option_index
            
