import json

import pyperclip
from AnilistPython import Anilist
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView

from backend.apis.crunchyroll import Crunchyroll, LoginError
from backend.apis.funimation import Funimation


def generate_error_response(message, status_code=400):
    return Response({"status": "error", "message": message}, status=status_code)


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


class CrunchyrollLogin(APIView):
    def post(self, request: Request, format=None):
        # print(request.body.decode('utf-8'))
        # print(request.POST)
        try:
            email = request.POST["email"]
            # print(email)
            password = request.POST["password"]
            # print(password)
        except:
            return generate_error_response("An email and password are required.")

        try:
            cr = Crunchyroll(email, password)
        except LoginError as e:
            return generate_error_response("Login credentials invalid", 401)
        # print(request.POST["test"])

        with open("backend/database/logins.json", "r+", encoding='utf-8') as json_file:
            str_content = json_file.read()
            data = json.loads(str_content)
            data["CRUNCHYROLL_EMAIL"] = email
            data["CRUNCHYROLL_PSWD"] = password
            json_file.seek(0)
            json.dump(data, json_file)

        return Response({"status": "success"}, status=200)

class FunimationLogin(APIView):
    def post(self, request: Request, format=None):
        # print(request.body.decode('utf-8'))
        # print(request.POST)
        try:
            email = request.POST["email"]
            # print(email)
            password = request.POST["password"]
            # print(password)
        except:
            return generate_error_response("An email and password are required.")

        try:
            fn = Funimation(email, password)
        except LoginError as e:
            return generate_error_response("Login credentials invalid", 401)
        # print(request.POST["test"])

        with open("backend/database/logins.json", "r+", encoding='utf-8') as json_file:
            str_content = json_file.read()
            data = json.loads(str_content)
            data["FUNIMATION_EMAIL"] = email
            data["FUNIMATION_PSWD"] = password
            json_file.seek(0)
            json.dump(data, json_file)

        return Response({"status": "success"}, status=200)
