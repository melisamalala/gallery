from django.db import models

# Create your models here.
import datetime as dt

class Location(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()


class tags(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_tags(self):
        self.save()

    def delete_tags(self):
        self.delete()

class Image(models.Model):
    image=models.ImageField(upload_to='picture/')
    name = models.CharField(max_length=60)
    description=models.TextField()
    location=models.ManyToManyField(Location, blank=True)
    tags=models.ManyToManyField(tags, blank=True)

    def __str__(self):
        return self.name


    def save_image(self):
        self.save()


    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(self):


    @classmethod
    def get_image_by_id(self):


    @classmethod
    def search_image(self):


    @classmethod
    def filter_image_by_id(self):