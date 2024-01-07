from django.test import TestCase
from Restaurant.models import Menu

# Create a test case for the Menu model


class MenuTest(TestCase):
    # Test the creation of a new menu item
    def test_create_menu_item(self):
        # Create a new menu item with the given attributes
        menu_item = Menu.objects.create(
            Title='IceCream', Price='20.13', Inventory='30')
        # Assert that the menu item was created successfully
        self.assertEqual(menu_item.Title, 'IceCream')
        self.assertEqual(menu_item.Price, '20.13')
        self.assertEqual(menu_item.Inventory, '30')
