from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

# Create your tests here.
from django.test import TestCase
from .models import Disorder

class ModelTestCase(TestCase):
    def setUp(self):
        self.disorder_name = "TestDisorder"
        self.disorder = Disorder(name=self.disorder_name)

    def test_model_can_create_a_disorder(self):
        old_count = Disorder.objects.count()
        self.disorder.save()
        new_count = Disorder.objects.count()
        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.disorder_data = {'name' : 'Depression'}
        self.response = self.client.post(reverse('create'), self.disorder_data, format="json")

    def test_api_can_create_a_disorder(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_disorder(self):
        disorder = Disorder.objects.get()
        response = self.client.get(reverse('details', kwargs={'pk':disorder.id}), format="json")

    def test_api_can_update_disorder(self):
        change_disorder = {'name': 'Something new'}
        res = self.client.put(reverse('details', kwargs={'pk':disorder.id}), change_disorder, format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_disorder(self):
        disorder = Disorder.objects.get()
        response = self.client.delete(reverse('details', kwargs={'pk': disorder.id}), format='json', follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
