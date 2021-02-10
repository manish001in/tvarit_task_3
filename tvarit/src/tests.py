# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, RequestFactory
import json
from . import views

class UserTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    # Returns true for normal non teen numbers
    def tests_accurate_numbers(self):
        request = self.factory.put('/sum', '[1, 2, 3]', content_type='application/json')

        response = json.loads(views.number_sum(request).content)
        self.assertEqual(response['status'], 200)
        self.assertEqual(response['result'], 6)

    # Returns true for non numeric numbers. 
    def test_non_numeric(self):         
        request = self.factory.put('/sum', '[1, "a", 3]', content_type='application/json')

        response = json.loads(views.number_sum(request).content)        
        self.assertEqual(response['status'], 400)
        self.assertEqual(response['error'], "All inputs must be numeric")

    # Returns true for not exactly 3 numbers provided as input. 
    def test_non_3_number(self):         
        request = self.factory.put('/sum', '[1, 2]', content_type='application/json')

        response = json.loads(views.number_sum(request).content)        
        self.assertEqual(response['status'], 400)
        self.assertEqual(response['error'], "Exactly 3 numbers are required")
   
    # Returns true for non 15,16 teen number where teen number is considered 0. 
    def test_teen_non_15_16_numbers(self): 
        request = self.factory.put('/sum', '[1, 2, 13]', content_type='application/json')

        response = json.loads(views.number_sum(request).content)        
        self.assertEqual(response['status'], 200)
        self.assertEqual(response['result'], 3)

    # Returns true for 15,16 teen number where the number is considered as its actual value. 
    def test_teen_15_16_numbers(self): 
        request = self.factory.put('/sum', '[1, 3, 15]', content_type='application/json')

        response = json.loads(views.number_sum(request).content)        
        self.assertEqual(response['status'], 200)
        self.assertEqual(response['result'], 19)

    # Returns true if the request is not of put method. 
    def test_invalid_method(self): 
        request = self.factory.post('/sum', '[1, 3, 15]', content_type='application/json')

        response = json.loads(views.number_sum(request).content)        
        self.assertEqual(response['status'], 500)
        self.assertEqual(response['error'], "Invalid request method")