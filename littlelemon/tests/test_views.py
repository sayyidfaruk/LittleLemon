from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializer import MenuSerializer
from rest_framework.test import APIClient

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Bruschetta", price=10, inventory=50)

    def test_getall(self):
        client = APIClient()
        menus = Menu.objects.all()
        serialized_menus = MenuSerializer(menus, many=True)
        response = client.get('/restaurant/menu/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serialized_menus.data)