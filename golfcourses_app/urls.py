
from django.urls import path

from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('courses/', views.index, name='courses-index'),
    path('golfcourses/<int:golfcourse_id>/', views.golfcourse_detail, name='golfcourse-detail'),
    path('courses/create/', views.CourseCreate.as_view(), name='course-create'),
    path('golfcourses/<int:pk>/update/', views.CourseUpdate.as_view(), name='course-update'),
    path('golfcourses/<int:pk>/delete/', views.CourseDelete.as_view(), name='course-delete'),
    path('golfcourses/<int:golfcourse_id>/add_snack/', views.add_golfsnacks, name='add-golfsnacks'),
]
