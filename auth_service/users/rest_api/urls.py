from django.urls import path

from .views import UserListCreateAPIView, UserRetrieveUpdateDeleteAPIView

app_name = "auth_service.users"


urlpatterns = [
    path("",
         UserListCreateAPIView.as_view(),
         name="user-list-create"
    ),
    path("<uuid:uuid>/",
         UserRetrieveUpdateDeleteAPIView.as_view(),
         name="user-retrieve-update-delete"
    ),
]
