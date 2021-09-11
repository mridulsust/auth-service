from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Custom TokenObtainPairView.

    Takes a set of user credentials and returns an access and refresh JSON web
    token pair to prove the authentication of those credentials.
    """
    pass


class CustomTokenRefreshView(TokenRefreshView):
    """
    Custom TokenRefreshView.

    Takes a refresh type JSON web token and returns an access type JSON web
    token if the refresh token is valid.
    """
    pass
