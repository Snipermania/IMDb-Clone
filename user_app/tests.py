'''from django.contrib.auth.models import User
from django.urls import reverse


from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

class RegisterTestCase(APITestCase):
    
    def test_register(self):
        data={
            "username":"Test",
            "email":"Test@gmail.com",
            "password":"12345",
            "password1":"12345"
        }
        
        response=self.client.post(reverse('register'),data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
    '''