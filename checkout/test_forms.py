from django.test import TestCase
from .forms import MakePaymentForm


class TestsFormsForCheckoutApp(TestCase):

    def test_card_payment(self):
        """Tests if a user is able to make a payment"""
        form = MakePaymentForm(
            {
                'credit_card_number': '4242424242424242',
                'cvv': '111',
                'expiry_month': '1',
                'expiry_year': '2022',
            })
        self.assertFalse(form.is_valid())
