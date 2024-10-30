from django.contrib import admin

# Register your models here.
from .models import Golf, GolfSnacks

admin.site.register(Golf)
admin.site.register(GolfSnacks)