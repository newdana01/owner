from django.urls import path

from actors.views import ActorView

urlpatterns = [
    path('', ActorView.as_view()),
    ]