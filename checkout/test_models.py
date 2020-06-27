from django.test import TestCase
from .models import Order, OrderLineItem
from products.models import Product
from django.utils import timezone

class TestModelsForCheckoutApp(TestCase):
    def test_buy_product(self):
        """To test the Order model works by collecting the correct information from the user """
        date_now = timezone.now()
        order = Order(full_name="John Doe", phone_number="0192837465", country="Nigeria", postcode="987654", 
                            town_or_city="Calabar", street_address1="Raeburn", street_address2="Road", 
                            county="Nigeriashire", date=date_now )
        self.assertEqual(order.full_name, "John Doe")
        self.assertEqual(order.phone_number, "0192837465")
        self.assertEqual(order.country, "Nigeria")
        self.assertEqual(order.postcode, "987654")
        self.assertEqual(order.town_or_city, "Calabar")
        self.assertEqual(order.street_address1, "Raeburn")
        self.assertEqual(order.street_address2, "Road")
        self.assertEqual(order.county, "Nigeriashire")
        self.assertEqual(order.date, date_now )