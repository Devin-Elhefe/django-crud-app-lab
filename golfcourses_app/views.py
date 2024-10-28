from django.shortcuts import render
from .models import Golf

from django.http import HttpResponse

def golfcourse_detail(request, golfcourse_id):
    golfcourses_from_db = Golf.objects.get(id=golfcourse_id)

    return render(request, 'golfcourses/detail.html', {'golfcourse': golfcourses_from_db})









#     def __init__(self, name, description):
#         self.name = name
#         self.description = description



# courses = [
#     Course('Augusta National', 'The Masters Tournament'),
#     Course('Pebble Beach', 'One of the best coastal golf resorts in the world'),
#     Course('TPC Sawgrass', 'The Players Championship'),
#     Course('Emirates Golf Club', 'Omega Dubai Desert Classic')
# ]


def home(request):
    featured_courses = Golf.objects.filter(featured=True)
    return render(request, 'home.html', {'courses': featured_courses})

def about(request):
    return render(request, 'about.html')

def index(request):
    courses = Golf.objects.all() 
    return render(request, 'golfcourses/index.html', {'courses': courses})

def golfcourse_detail(request, golfcourse_id):
    golfcourse = Golf.objects.get(id=golfcourse_id)
    return render(request, 'golfcourses/detail.html', {'golf': golfcourse})



