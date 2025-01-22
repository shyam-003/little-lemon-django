
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from lemonApp.models import Menu
from lemonApp.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu_item_1 = Menu.objects.create(title="Pizza", price=12.5, inventory=50)
        self.menu_item_2 = Menu.objects.create(title="Burger", price=8.0, inventory=30)
        self.menu_item_3 = Menu.objects.create(title="Ice Cream", price=5.0, inventory=100)
        
    def test_get_all_items(self):
        response = self.client.get('/lemonapp/menu/')
        
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)