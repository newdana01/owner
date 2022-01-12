from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Actor(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    movie = models.ManyToManyField('movies.Movie',through='ActorMovie')

    class Meta:
        db_table = 'actors'

class ActorMovie(models.Model):
    actor = models.ForeignKey('Actor', on_delete=CASCADE)
    movie = models.ForeignKey('movies.Movie', on_delete=CASCADE)

    class Meta:
        db_table = 'actors_movies'