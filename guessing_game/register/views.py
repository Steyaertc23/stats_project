from django.shortcuts import redirect, render
from .forms import SignUpForm
from django.contrib.auth.models import User
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

def check_if_password_exist(password:str):
    password_copy = password
    for user in User.objects.all()[2:-1]:
            for pw in user.guesspasswordmodel_set.all():
                if password_copy == pw:
                    return check_if_password_exist(generate())
    return password_copy
# Create your views here.
def login(request):
    return redirect('login')

def new_account(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            random_passwords = [check_if_password_exist(generate()) for _ in range(5)]
            for password in random_passwords:
                request.user.guesspasswordmodel_set.create(pw=password)

            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form':form})