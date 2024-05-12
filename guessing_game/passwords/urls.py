from django.urls import path
from .views import *

urlpatterns = [
    path('', passwords, name='home'),
    path('thanks/', thanks, name='thanks')
]