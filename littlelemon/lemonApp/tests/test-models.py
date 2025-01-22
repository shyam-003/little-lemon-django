from django.test import TestCase
from lemonApp.models import Menu

# Create your tests here.
class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream - $80.00 (100 in stock)")