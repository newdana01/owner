from django.urls import path
from owners.views import DogView, OwnerView


urlpatterns = [
    path('', OwnerView.as_view()),
    path('/<int:owners_id>', DogView.as_view()),
]