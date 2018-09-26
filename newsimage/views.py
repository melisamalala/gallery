
from django.shortcuts import render, redirect

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

