'''
'''

from rich.console import Console
from rich.theme import Theme

from sklearn.cluster import KMeans

# variables for the menus
custom_theme = Theme({
    "good": "green",
    "bad": "bold red",
    "warning": "bold yellow",
    "info": "blue"
})

console = Console(theme=custom_theme)

# kmeans model
kmeans = KMeans(n_clusters=2, random_state=42, n_init="auto")