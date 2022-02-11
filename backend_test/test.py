import os
import pyperclip
from pprint import pprint

import difflib

import tmdbsimple as tmdb

from backend_test.apis.funimation import Funimation

tmdb.API_KEY = os.environ["TMDB_API_KEY"]
# pprint(response["results"][0])
# print(s['name'], s['id'], s['first_air_date'], s['popularity'])
