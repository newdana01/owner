from django.db.models.query_utils import Q
from django.http import JsonResponse
from django.views import View
import json

from owners.models import Dog, Owner

# Create your views here.
class OwnerView(View):
    def post(self, request):
        data = json.loads(request.body)
        
        Owner.objects.create(
            name=data["name"], email=data["email"], age=data["age"]
            )

        return JsonResponse({'message':'SUCCESS'},status=201)

class DogView(View):
    def post(self, request, owners_id):
        data = json.loads(request.body)

        Dog.objects.create(
            name=data["name"], age=data["age"], owner_id=owners_id
            )

        return JsonResponse({'message':'SUCCESS'},status=201)
