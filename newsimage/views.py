
from django.shortcuts import render, redirect
from .models import Image,Location,tags

# Create your views here.


from django.http  import HttpResponse, Http404
import datetime as dt

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

# Search for an image
def search_image(request):
        if 'image' in request.GET and request.GET["image"]:
            search_term = request.GET.get("image")
            searched_images = Image.search_image(search_term)
            message = f"{search_term}"

            return render(request, 'all-news/search.html', {"message": message, "images": searched_images})

        else:
            message = "You haven't searched for any image"
            return render(request, 'all-images/search.html', {"message": message})


#         Viewing a single picture
def image(request, image_id):
    try:
        image = Image.objects.get(id = image_id)

    except DoesNotExist:
        raise Http404()


    return render(request, 'all-images/image.html', {"image": image})