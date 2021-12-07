#!/usr/bin/env python3
from django.test import TestCase
from django.contrib.auth.models import User

class SimpleTest(TestCase):
    def setUp(self):
     self.user = User.objects.create_superuser(username = 'testuser', password='password')
     
    def tearDown(self): 
      self.user.delete()
      
    def  test_add_blog_post(self):
      self.client.login(username = 'testuser', password='password')
      response = self.client.post('/admin/theblog/post/add/', {'title': 'XXX TITLE XXX', 'body': 'testing','title_tag': 'one' ,'author': self.user.id })
      self.assertEqual(response.status_code, 302)
      response = self.client.get('/')
      print(response.content)
      self.assertTrue('XXX TITLE XXX' in  str(response.content))
      