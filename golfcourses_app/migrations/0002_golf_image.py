# Generated by Django 4.2.16 on 2024-10-28 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('golfcourses_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='golf',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/golfcourses/'),
        ),
    ]