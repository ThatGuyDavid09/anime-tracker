from AnilistPython import Anilist
from pprint import pprint
import pyperclip

from wrappers import *
from test import test

anilist = Anilist()


pprint(anilist.extractID.anime("Code Geass"))
pyperclip.copy(str(anilist.extractID.anime("Code Geass")))