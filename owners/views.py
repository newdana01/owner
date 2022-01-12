import json

from django.http import JsonResponse
from django.views import View

from owners.models import Dog, Owner

# Create your views here.
class OwnerView(View):
    def post(self, request):
        data = json.loads(request.body)
        
        owner = Owner.objects.create(
            name=data["name"], email=data["email"], age=data["age"]
            )

        return JsonResponse({'owner_id':owner.id},status=201)
        
    def get(self, request):
        owners = Owner.objects.all()

        # 2중 list comprehension
        result = [
            {
                'name': owner.name,
                'age': owner.age,
                'email': owner.email,
                'dogs': [{'name':dog.name, 'age': dog.age} for dog in owner.related_dog.all()]
            }
            for owner in owners]

        # for owner in owners:
        #     result.append(
        #         {   
        #             'name': owner.name,
        #             'age': owner.age,
        #             'email': owner.email,
        #             'dogs': [{'name':dog.name, 'age': dog.age} for dog in owner.related_dog.all()]
        #         }
        #     )

        return JsonResponse({'owners':result}, status=200)

class DogView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            owner = Owner.objects.get(id=data["owner_id"])
            dog = Dog.objects.create(
                name=data["name"], age=data["age"], owner_id=owner.id
                )
        except Owner.DoesNotExist:
            return JsonResponse({'message':'Owner does not exists.'}, status=400)
        else: 
            return JsonResponse({'dog_id': dog.id},status=201)

    def get(self, request):
        dogs = Dog.objects.all()

        result = []

        for dog in dogs:
            result.append(
                {
                    'name': dog.name,
                    'age': dog.age,
                    'owner' :
                    {
                        'name': dog.owner.name,
                        'age': dog.owner.age
                    }
                }
            )

        return JsonResponse({'dogs': result}, status=200)