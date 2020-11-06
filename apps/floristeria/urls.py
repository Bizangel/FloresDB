from django.urls import path
from apps.floristeria.views import index

urlpatterns = [
    path('', index),
]
