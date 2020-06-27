from django.test import TestCase
from django.urls import reverse
from .forms import UserLoginForm
from django.contrib.auth.models import User
from checkout.models import Order, OrderLineItem
from django.utils import timezone

class TestViewsForAccountsApp(TestCase):
    def test_home_page(self):
        """Tests if homepage is rendered correctly"""
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "home.html")

    def test_login_page(self):
        """Tests to check if the login page is rendered correctly and also checking that it is reversed properly"""
        page = self.client.get("/accounts/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")
        reverse_page = self.client.post(reverse('index'))
        self.assertEqual(reverse_page.status_code, 200)

    def test_registration_page(self):
        """Tests to check if the registration page is rendered correctly"""
        page = self.client.get("/accounts/register/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "register.html")