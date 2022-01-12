import json

from django.http.response import JsonResponse
from django.views import View

from movies.models import Movie

# Create your views here.
class MovieView(View):
    def post(self, request):
        movie_data = json.loads(request.body)

        movie = Movie(
            title = movie_data['title'],
            release_date = movie_data['release_date'], 
            running_time = movie_data['running_time']
        )

        movie.save()

        return JsonResponse({'movie_id': movie.id}, status = 201)


    def get(self, request):
        movies = Movie.objects.all()

        result = [
            {
                'title': movie.title,
                'running_time': movie.running_time,
                'actors': [{'name': actor.name} for actor in movie.actor_set.all()]
            } for movie in movies
        ]

        return JsonResponse({'movies': result}, status=200)
