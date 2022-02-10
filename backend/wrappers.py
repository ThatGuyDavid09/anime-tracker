class Anime:
    def __init__(self, json):
        self.name_romaji = json["name_romaji"]
        self.name_english = json["name_english"]
        self.starting_time = json["starting_time"]
        self.ending_time = json["ending_time"]
        self.cover_image = json["cover_image"]
        self.banner_image = json["banner_image"]
        self.airing_format = json["airing_format"]
        self.airing_status = json["airing_status"]
        self.airing_episodes = json["airing_episodes"]
        self.season = json["season"]
        self.desc = json["desc"]
        self.average_score = json["average_score"]
        self.genres = json["genres"]
        self.next_airing_ep = json["next_airing_ep"]

class Character:
    def __init__(self, json):
        self.first_name = json["first_name"]
        self.last_name = json["last_name"]
        self.native_name = json["native_name"] 
        self.desc = json["desc"] 
        self.image = json["image"]