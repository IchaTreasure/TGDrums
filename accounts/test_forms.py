from django.test import TestCase
from .forms import UserRegistrationForm, UserLoginForm


class TestsFormsForAccountsApp(TestCase):

    def test_user_can_register_and_create_an_account(self):
        """Tests if a user is able to registrater/ create an account"""
        form = UserRegistrationForm(
            {
                'email': 'afang@gmail.com', 
                'username': 'User1', 
                'password1': 'User1Registration', 
                'password2': 'User1Registration'
            })
        self.assertTrue(form.is_valid())

        
