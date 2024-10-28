
from django.urls import path

from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('courses/', views.index, name='courses-index'),
    path('golfcourses/<int:golfcourse_id>/', views.golfcourse_detail, name='golfcourse-detail'),
]
