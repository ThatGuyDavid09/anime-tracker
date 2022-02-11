import json
from json import JSONDecodeError

import pyperclip
from AnilistPython import Anilist
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView

from backend.apis.crunchyroll import Crunchyroll, LoginError
from backend.apis.funimation import Funimation
from backend.models import Anime


def generate_error_response(message, status_code=400):
    return Response({"status": "error", "message": message}, status=status_code)


SERVICES = ["crunchyroll, funimation"]


# Create your views here.
class Search(APIView):
    def get(self, request: Request, format=None):
        try:
            search_query = request.query_params["query"]
        except:
            return generate_error_response("A query parameter is required")

        anilist = Anilist()
        anime_info = anilist.extractID.anime(search_query)["data"]["Page"]["media"]
        return Response({"status": "success", "amount": len(anime_info), "items": anime_info}, status=200)


class Info(APIView):
    def get(self, request: Request, format=None):
        try:
            search_id = request.query_params["id"]
        except:
            return generate_error_response("An id parameter is required.")

        anilist = Anilist()
        anime = anilist.extractInfo.anime(search_id)["data"]["Media"]
        return Response({"status": "success", "result": anime}, status=200)


class Login(APIView):
    def post(self, request: Request, format=None):
        # print(request.body.decode('utf-8'))
        # print(request.POST)
        try:
            service = request.POST["service"].lower()
            email = request.POST["email"]
            # print(email)
            password = request.POST["password"]
            # print(password)
        except:
            return generate_error_response("An email and password, and service are required.")

        try:
            if service == "crunchyroll":
                _ = Crunchyroll(email, password)
            elif service == "funimation":
                _ = Funimation(email, password)
            else:
                return generate_error_response("Invalid service. Currently support " + ", ".join(SERVICES))
        except LoginError as e:
            return generate_error_response("Login credentials invalid", 401)
        # print(request.POST["test"])

        with open("backend/data/logins.json", "r+", encoding='utf-8') as json_file:
            str_content = json_file.read()
            try:
                data = json.loads(str_content)
            except JSONDecodeError:
                data = {}
            data[service.upper() + "_EMAIL"] = email
            data[service.upper() + "_PSWD"] = password
            json_file.seek(0)
            json.dump(data, json_file)

        return Response({"status": "success"}, status=200)


class GetAuthenticatedServices(APIView):
    def get(self, request: Request, format=None):
        data = {"status": "success", "services": []}
        with open("backend/data/logins.json", "r+", encoding='utf-8') as json_file:
            str_content = json_file.read()
            try:
                data = json.loads(str_content)
            except JSONDecodeError:
                return Response(data)
            for service in SERVICES:
                try:
                    _ = data[service.upper() + "_PSWD"]
                    data["services"].append(service)
                except KeyError:
                    continue


class RegisterAnime(APIView):
    def post(self, request: Request, format=None):
        try:
            anime_id = request.POST["anime_id"].lower()
            # print(password)
        except:
            return generate_error_response("An anime_id is required.")

        anime = Anime(anilist_id=anime_id)
        anime.save()


class GetRegisteredAnime(APIView):
    def get(self, request: Request, format=None):
        anilist = Anilist()
        return Response({"status": "success", "count": len(Anime.objects.all()), "anime": [anilist.extractInfo.anime(anime.anime_anilist_id)["data"]["Media"] for anime in Anime.objects.all()]})
