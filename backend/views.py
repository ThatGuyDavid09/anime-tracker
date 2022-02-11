from AnilistPython import Anilist
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView


# Create your views here.
class Search(APIView):
    def get(self, request: Request, format=None):
        try:
            search_query = request.query_params["query"]
        except:
            return Response({"status": "error", "'message": "A query parameter is required."}, status=400)

        anilist = Anilist()
        anime_info = anilist.extractID.anime(search_query)["data"]["Page"]["media"]
        return Response({"status": "success", "amount": len(anime_info), "items": anime_info}, status=200)
