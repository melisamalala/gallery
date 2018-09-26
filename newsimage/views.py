
from django.shortcuts import render, redirect
from .models import Image,Location,tags

# Create your views here.


from django.http  import HttpResponse, Http404
import datetime as dt

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

def news_today(request):
    date = dt.date.today()
    return render(request, 'all-images/today-images.html', {"date": date,})


# View Function to present news from past days
def past_days_news(request, past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(news_today)

    return render(request, 'all-images/past-images.html', {"date": date})


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