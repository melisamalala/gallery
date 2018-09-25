from django.test import TestCase

# Create your tests here.
from .models import Location, tags, Image

class LocationTestClass(TestCase):

    #Set up method the test for location and instantiating the location object


    def setUp(self):
        self.nairobi = Location(name = 'Nairobi')

    #Testing instance

    def test_instance(self):

        self.assertTrue(isinstance(self.nairobi, Location))

    #Testing Save method

    def test_save_method(self):
        self.nairobi.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)

    #Testing Delete method for deleting the classes Location and Tags

    def tearDown(self):
        Location.objects.all().delete()
        tags.objects.all().delete()
        Image.objects.all.delete()


class ImageTestClass(TestCase):

      # Set up method the test for images and instantiating the location object

    def setUp(self):
        self. = Location(name='Nairobi')



