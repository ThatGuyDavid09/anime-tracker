from django.urls import path
from . import views

urlpatterns = [
    path('api/search/', views.Search.as_view()),
    path('api/info/', views.Info.as_view()),
    path('api/login/crunchyroll', views.CrunchyrollLogin.as_view()),
    path('api/login/funimation', views.FunimationLogin.as_view()),
]