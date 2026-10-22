
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # Aplicación web
    path("", include("core.urls")),
    path("autos/", include("Autos.urls")),
    path("precios/", include("Precios.urls")),

    # API REST de autos
    path("api/", include("Autos.api_urls")),

    # Autenticación JWT
    path(
        "api/token/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        "api/token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),

    # Administración
    path("admin/", admin.site.urls),
]
