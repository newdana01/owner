import json

from django.http.response import JsonResponse
from django.views import View

from actors.models import Actor
from movies.models import Movie

# Create your views here.


class ActorView(View):
    def post(self, request):
        actor_data = json.loads(request.body)

        m = Movie.objects.get(pk=actor_data['movie_id'])
        actor = Actor(
            first_name = actor_data['first_name'],
            last_name = actor_data['last_name'],
            date_of_birth = actor_data['date_of_birth']
        )

        actor.save()
        actor.movie.add(m)

        return JsonResponse({'actor_id': actor.id}, status=201)

    def get(self, request):
        actors = Actor.objects.all()
        result = [
            {
                'first_name': actor.first_name,
                'last_name': actor.last_name,
                'filmography': [{'title': movie.title} for movie in actor.movie.all()]
            } for actor in actors
        ]

        return JsonResponse({'actors': result}, status=200)
