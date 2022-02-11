from django.db import models


# Create your models here.
class Anime(models.Model):
    anime_anilist_id = models.IntegerField()
