from django.db import models

# Create your models here.

class Golf(models.Model):
    name= models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    image = models.ImageField(upload_to='images/golfcourses/', null=True, blank=True)
    featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name