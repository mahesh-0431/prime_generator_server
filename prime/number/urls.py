from django.urls import path
from . import views

urlpatterns=[
    path('generate_primes/', views.generate_primes, name='generate_primes'),
]