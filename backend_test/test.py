import os

import tmdbsimple as tmdb

tmdb.API_KEY = os.environ["TMDB_API_KEY"]
# pprint(response["results"][0])
# print(s['name'], s['id'], s['first_air_date'], s['popularity'])
