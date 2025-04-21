from django.test import TestCase
from api.models import Order , User
from django.urls import reverse

# Create your tests here.
class UserOrderTestCase(TestCase):
    def setUp(self):
        user1 = User.objects.create_user(username='user1',password='test1')
        Order.objects.create(user=user1)


    def test_user_only_authenticated(self):
        user= User.objects.get(username='user1')
        self.client.force_login(user)
        response = self.client.get(reverse('user-orders'))

        assert response.status_code == 200
        data = response.json()
        print(data)