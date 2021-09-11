from django.urls import path

from .views import CustomTokenObtainPairView, CustomTokenRefreshView

app_name = "auth_service.authentications"

urlpatterns = [
    path(
        "login/",
        view=CustomTokenObtainPairView.as_view(),
        name="login"
    ),
    path(
        "refresh-token/",
        view=CustomTokenRefreshView.as_view(),
        name="refresh-token"
    ),
]
