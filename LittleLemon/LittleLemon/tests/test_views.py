from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from Restaurant.models import Menu
from Restaurant.serializers import MenuItemSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class MenuViewTest(TestCase):
    def setUp(self):
        # Create a user and obtain a token
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)

        # Add a few test instances of the Menu model
        Menu.objects.create(Title='IceCream', Price='20.13', Inventory='30')
        Menu.objects.create(Title='Burger', Price='10.50', Inventory='25')
        Menu.objects.create(Title='Pizza', Price='15.99', Inventory='40')

    def test_getall(self):
        # Authenticate the client using the obtained token
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

        # Retrieve all Menu objects
        url = reverse('menu-list')
        response = client.get(url)

        # Serialize the data
        menus = Menu.objects.all()
        serializer = MenuItemSerializer(menus, many=True)

        # Check if the serialized data equals the response data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
