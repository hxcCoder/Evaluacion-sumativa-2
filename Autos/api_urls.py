from django.urls import path
from .views import lista_autos_api, detalle_auto_api

urlpatterns = [
    path("autos/", lista_autos_api, name="lista_autos_api"),
    path("autos/<int:id>/", detalle_auto_api, name="detalle_auto_api"),
]