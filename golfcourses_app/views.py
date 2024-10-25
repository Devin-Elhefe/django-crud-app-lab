from django.shortcuts import render

from django.http import HttpResponse

class Course:
    
    def __init__(self, name, description):
        self.name = name
        self.description = description



courses = [
    Course('Augusta National', 'The Masters Tournament'),
    Course('Pebble Beach', 'One of the best coastal golf resorts in the world'),
    Course('TPC Sawgrass', 'The Players Championship'),
    Course('Emirates Golf Club', 'Omega Dubai Desert Classic')
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def courses_index(request):
    return render(request, 'courses/index.html', {'courses': courses})



