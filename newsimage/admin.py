from django.contrib import admin

# Register your models here.
from .models import Location,tags, Image

admin.site.register(Location)
admin.site.register(tags)
admin.site.register(Image)