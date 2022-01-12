from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=45)
    release_date = models.DateField(auto_now=False, auto_now_add=False)
    running_time = models.PositiveIntegerField()

    class Meta:
        db_table = 'movies'