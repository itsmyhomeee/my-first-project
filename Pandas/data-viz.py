import pandas as pd
from pandasgui import show

from pandasgui.datasets import all_datasets

print(show(**all_datasets))