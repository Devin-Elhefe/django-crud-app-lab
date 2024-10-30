from django.shortcuts import render, redirect
from .models import Golf, GolfSnacks

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.http import HttpResponse

from .forms import GolfSnacksForm

def golfcourse_detail(request, golfcourse_id):
    golfcourses_from_db = Golf.objects.get(id=golfcourse_id)
    snacks = GolfSnacks.objects.filter(course=golfcourses_from_db)
    form = GolfSnacksForm()
    return render(request, 'golfcourses/detail.html', {'golf': golfcourses_from_db, 'snacks': snacks,'form': form})

def add_golfsnacks(request, golfcourse_id):
    golf = Golf.objects.get(id=golfcourse_id)
    form = GolfSnacksForm(request.POST)
    
    if form.is_valid():
        new_snack = form.save(commit=False)
        new_snack.course = golf
        new_snack.save()
        
    return redirect('golfcourse-detail', golfcourse_id=golfcourse_id)

class CourseCreate(CreateView):
    model = Golf
    fields = ['name', 'description']
    template_name = 'main_app/golf_form.html'

class CourseUpdate(UpdateView):
    model = Golf
    fields = ['name', 'description']
    template_name = 'main_app/golf_form.html'
    
class CourseDelete(DeleteView):
    model = Golf
    template_name = 'main_app/golf_confirm_delete.html'
    success_url = '/courses/'



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





