from django.test import TestCase
from restaurant.models import MenuItem

class MenuItemsViewTest(TestCase):
        
    def setup(self):
        MenuItem.objects.create(id=1, title="IceCream", price=80, inventory=100)
        MenuItem.objects.create(id=2, title="Coke", price=10, inventory=100)
        MenuItem.objects.create(id=3, title="Pepsi", price=10, inventory=100)
        MenuItem.objects.create(id=4, title="Sprite", price=10, inventory=100)

    def test_getall(self):
        
        response = self.client.get('/restaurant/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 4)
