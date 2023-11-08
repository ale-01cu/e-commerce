from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

class RecommendationSystemTest(APITestCase):
    def test_recommendedProductsAPI(self):
        url = reverse('recommended-products', args=[1])
        response = self.client.get(
            url,
            format='json'
        )
        print(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)