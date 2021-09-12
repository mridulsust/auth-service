from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

# Create your tests here.
User = get_user_model()


class UserWithoutLoginTestCase(APITestCase):
    """
    Without login only User object creation is allowed.
    """
    username = "test_user"
    password = "1234pass"

    def setUp(self):
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password
        )

    def test_create_user(self):
        """
        Ensure we can create a new user object.
        """
        url = "/api/v1/users/"
        data = dict(username="john_doe", password="123456")
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(User.objects.last().username, "john_doe")

    def test_invalid_create_user(self):
        """
        Ensure we can create a new user object.
        """
        url = "/api/v1/users/"
        data = dict(username="john_doe")
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_user_without_login(self):
        """
        Ensure we are unable to retrieve user object without login.
        """
        url = f"/api/v1/users/{self.user.uuid}/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class UserWithLoginTestCase(APITestCase):
    username_1 = "test_user_1"
    password_1 = "1234pass"
    username_2 = "test_user_2"
    password_2 = "1234pass"

    def setUp(self):
        self.user_1 = User.objects.create_user(
            username=self.username_1,
            password=self.password_1
        )
        self.user_2 = User.objects.create_user(
            username=self.username_2,
            password=self.password_2
        )
        response = self.client.post(
            "/api/v1/authentications/login/",
            {
                'username': self.username_1,
                'password': self.password_1
            },
            format='json'
        )
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + response.data.get("access", ""))

    def test_do_not_retrieve_cross_user(self):
        """
        Ensure we can not retrieve cross user object.
        """
        url = f"/api/v1/users/{self.user_2.uuid}/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_do_not_update_cross_user(self):
        """
        Ensure we can not update cross user object.
        """
        url = f"/api/v1/users/{self.user_2.uuid}/"
        data = dict(first_name="john", last_name="doe")
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_do_not_delete_cross_user(self):
        """
        Ensure we can not delete cross user object.
        """
        url = f"/api/v1/users/{self.user_2.uuid}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_retrieve_user(self):
        """
        Ensure we can retrieve user object.
        """
        url = f"/api/v1/users/{self.user_1.uuid}/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_user(self):
        """
        Ensure we can update user object.
        """
        url = f"/api/v1/users/{self.user_1.uuid}/"
        data = dict(first_name="john", last_name="doe")
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_user(self):
        """
        Ensure we can delete user object.
        """
        url = f"/api/v1/users/{self.user_1.uuid}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
