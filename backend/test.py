from AnilistPython import Anilist
from pprint import pprint

from wrappers import *

anilist = Anilist()

def test():
    id = anilist.extractID.anime("Code Geass")["id"]
    pprint(anilist.extractInfo.anime(id))
    # pprint(anilist.getAnimeInfo("Code Geass"))