from django.test import TestCase
from .models import Product


# Create your tests here.
class ProductTest(TestCase):
    """
    Test will be defined here to run against the Product models
    """
    def test_product(self):
        product = Product(name='Product1', description='product description',
                          price='20', image='test.png')
        self.assertEqual(product.name, 'Product1')
        self.assertEqual(product.description, 'product description')
        self.assertEqual(product.price, '20')
        self.assertEqual(product.image, 'test.png')
