'''
'''

from rich.console import Console
from rich.theme import Theme
from rich.markdown import Markdown

# variables for the menus
custom_theme = Theme({
    "good": "green",
    "bad": "bold red",
    "warning": "bold yellow",
    "info": "blue"
})

console = Console(theme=custom_theme)