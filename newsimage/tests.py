from django.test import TestCase

# Create your tests here.
from .models import Location, tags

class LocationTestClass(TestCase):

    #Set up method the test for location and instantiating the location object


    def setUp(self):
        self.nairobi = Location(name = 'Nairobi')

    #Testing instance

    def test_instance(self):

        self.assertTrue(isinstance(self.nairobi, Location))


