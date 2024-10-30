# Generated by Django 4.2.16 on 2024-10-30 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('golfcourses_app', '0004_golfsnacks'),
    ]

    operations = [
        migrations.AddField(
            model_name='golfsnacks',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='golfcourses_app.golf'),
        ),
        migrations.AlterField(
            model_name='golfsnacks',
            name='date',
            field=models.DateField(verbose_name='Golf Date'),
        ),
    ]
