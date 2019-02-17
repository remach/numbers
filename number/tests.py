import datetime
import json
from django.test import TestCase, Client
from django.utils import timezone
from django.urls import reverse
from rest_framework.test import APIRequestFactory, APITestCase
from rest_framework import status
from .models import Number

#client = Client()
#factory = APIRequestFactory()
class NumberModelTests(TestCase):
    def test_was_published_recently_with_future_date(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_number = Number(pub_date=time)
        self.assertIs(future_number.was_published_recently(), False)

    