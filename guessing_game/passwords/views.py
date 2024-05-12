from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import GuessPasswordForm
from django.contrib.auth.models import User


# Create your views here.

# @login_required(login_url='/auth')
# def home(request):
#     current_user = request.user.pk
#     user = User.objects.all()[current_user-1]
#     user.guesspasswordmodel_set.create(pw='1111')
#     test = user.guesspasswordmodel_set.get(pk=1)

#     return HttpResponse(f"<h1>{test}</h1>")


@login_required(login_url='/auth')
def passwords(request):
    first_form = GuessPasswordForm()
    second_form = GuessPasswordForm()
    third_form = GuessPasswordForm()
    fourth_form = GuessPasswordForm()
    fifth_form = GuessPasswordForm()
    if request.method == 'POST':
        user = User.objects.get(pk=request.user.pk)
        if  first_form.is_valid() and  second_form.is_valid()  and  third_form.is_valid()  and  fourth_form.is_valid()  and  fifth_form.is_valid():
            first = first_form.cleaned_data['guess']
            second = second_form.cleaned_data['guess']
            third = third_form.cleaned_data['guess']
            fourth = fourth_form.cleaned_data['guess']
            fifth = fifth_form.cleaned_data['guess']
            user.passwordguess_set.create(guess=first)
            user.passwordguess_set.create(guess=second)
            user.passwordguess_set.create(guess=third)
            user.passwordguess_set.create(guess=fourth)
            user.passwordguess_set.create(guess=fifth)
            return redirect('thanks')
    else:
        return render(request, 'passwords/passwords.html', {'first':first_form, 'second':second_form, 'third':third_form, 'fourth':fourth_form, 'fifth':fifth_form})
    

def thanks(request):
    user = User.objects.get(pk=request.user.pk)
    user.is_active = False
    user.save()
    return render(request, 'passwords/thanks.html')