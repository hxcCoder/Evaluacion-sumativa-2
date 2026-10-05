from django.urls import path
from .views import lista_autos_api

urlpatterns = [
    path("autos/", lista_autos_api, name="lista_autos_api"),
]