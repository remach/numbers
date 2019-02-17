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

# Create your tests here.
class CreateNewNumberRestTests(APITestCase):
    def setUp(self):
        self.valid_payload = {
        "value": 333,
        "description_text": '__test',
        "unit": "руб",
        "link": "http://budget.mos.ru/",
        "pub_date": datetime.datetime.now().isoformat()
        }
        

        self.invalid_payload = {
        'name': '',
        'age': 4,
        'breed': 'Pamerion',
        'color': 'White'
        }

    def test_create_valid_numbers(self):
        response = self.client.post(
        reverse('Number-list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_numbers(self):
        response = self.client.post(
            reverse('Number-list'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    