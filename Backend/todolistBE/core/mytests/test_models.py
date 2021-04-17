from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


def sample_user(email='test@gmail.com',password='1234'):
    """create sample user """
    return get_user_model().objects.create_user(email,password)


class Modeltests(TestCase):
    def test_create_user_with_email_successful(self):
        email = 'test@gmail.com'
        password = 'test123'
        user = get_user_model().objects.create_user(
        email = email,
        password = password
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_tag_str(self):
        """test the tag string representation"""
        tag = models.Tag.objects.create(
        user = sample_user(),
        name = 'Vegan'
        )

        self.assertEqual(str(tag),tag.name)
