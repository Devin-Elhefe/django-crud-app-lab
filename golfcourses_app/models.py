from django.db import models

from django.urls import reverse
# Create your models here.

class Golf(models.Model):
    name= models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    image = models.ImageField(upload_to='images/golfcourses/', null=True, blank=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("golfcourse-detail", kwargs={"golfcourse_id": self.id})
    
SNACKS = (
    ('C', 'Chips'),
    ('G', 'Glizzy'),
    ('B', 'Burger'),
)

class GolfSnacks(models.Model):
    date = models.DateField('Golf Date')
    snacks = models.CharField(
        max_length=1,
        choices=SNACKS,
        default=SNACKS[0][0]
    )
    
    course = models.ForeignKey(Golf, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f"{self.get_snack_display()} on {self.date}"