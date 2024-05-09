from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import  LoginRequiredMixin, UserPassesTestMixin
from time import time
from random import randint, seed

def generate():
    seed(time())
    random = randint(0, 9999)
    if random >= 1000:
        return str(random)
    elif random >= 100:
        return f"0{random}"
    elif random >= 10:
        return f"00{random}"
    else:
        return f"000{random}"

# Create your views here.
class GeneratePasswords(LoginRequiredMixin, UserPassesTestMixin, View):
    ...

