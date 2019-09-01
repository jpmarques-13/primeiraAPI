#incomplete

from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status

from django.contrib.auth import get_user_model
from testeAPI.models import BlogPost

#automated
#new/blank db
from testeAPI.models import BlogPost
class BlogAPITestCase(APITestCase):
    def setUP(self):
        user = User(username = 'testcfeuser',
                    email='test@test.com')
        user.set_password("akin2010")
        user.save
        blog_post = BlogPost.objects.create(user=user_obj,
                                            title='new title',
                                            content='some_randon_content')


    def test_single_post(self):
        post_count = BlogPost.objects.count()
        self.assertEqual(post_count,1)

    def test_get_list(self):
        data = {}
        url = api_reverse("api-testando:post-create")
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
