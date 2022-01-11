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
        
    def get(self, request):
        owners = Owner.objects.all()

        result = []
        for index, owner in enumerate(owners):
            result.append(
                {   
                    'name': owner.name,
                    'age': owner.age,
                    'email': owner.email
                }
            )

            if owner.related_dog.all().exists():
                dog_result = []
                for dog in owner.related_dog.all():
                    dog_result.append(
                        {
                            'dog_name': dog.name,
                            'dog_age': dog.age
                        }
                    )
                result[index]['dog'] = dog_result
                print(index)
                print(result)

        return JsonResponse({'owners':result}, status=200)

class DogView(View):
    def post(self, request, owners_id):
        data = json.loads(request.body)

        try:
            owner = Owner.objects.get(id=owners_id)
            Dog.objects.create(
                name=data["name"], age=data["age"], owner_id=owner.id
                )
        except Owner.DoesNotExist:
            return JsonResponse({'message':'Owner does not exists.'}, status=400)
        else: 
            return JsonResponse({'message':'SUCCESS'},status=201)

    def get(self, request, owners_id):
        dogs = Dog.objects.filter(owner=owners_id)

        result = []

        for dog in dogs:
            result.append(
                {
                    'name': dog.name,
                    'age': dog.age,
                    'owner_name': dog.owner.name       
                }
            )

        return JsonResponse({'dogs': result}, status=200)