from django.urls import path
from . import views

urlpatterns = [
    path('api/search/', views.Search.as_view()),
    path('api/info/', views.Info.as_view()),
    path('api/login', views.Login.as_view()),
    path('api/login/available', views.GetAuthenticatedServices.as_view()),
    path('api/anime', views.GetRegisteredAnime.as_view()),
    path('api/anime/register', views.RegisterAnime.as_view()),
]