import os
import pyperclip
from pprint import pprint

from hulu import Hulu

from backend.apis.funimation import Funimation

hu = Hulu()
pprint(hu.get_shows())
