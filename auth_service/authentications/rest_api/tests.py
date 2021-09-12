from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

# Create your tests here.
User = get_user_model()


class UserWithLoginTestCase(APITestCase):
    username = "test_user"
    password = "1234pass"

    def setUp(self):
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password
        )

    def test_successful_login(self):
        response = self.client.post(
            "/api/v1/authentications/login/",
            {
                'username': self.username,
                'password': self.password
            },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unsuccessful_login(self):
        response = self.client.post(
            "/api/v1/authentications/login/",
            {
                'username': "invalid",
                'password': "invalid"
            },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
