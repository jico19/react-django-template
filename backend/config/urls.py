from django.contrib import admin
from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)


urlpatterns = [
    path('admin/', admin.site.urls),

    # jwt views
    path('login/', TokenObtainPairView.as_view(), name="get_token"),
    path('get/refresh/token', TokenRefreshView.as_view(), name="get_refresh_token"),
]
