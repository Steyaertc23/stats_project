from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import GuessPasswordForm


# Create your views here.

@login_required(login_url='/auth')
def home(request):
    current_user = request.user.pk
    
    return HttpResponse(f"<h1>{current_user}</h1>")


@login_required(login_url='/auth')
def passwords(request):
    if request.method == 'POST':
        ...
    else:
        first_form = GuessPasswordForm()
        second_form = GuessPasswordForm()
        third_form = GuessPasswordForm()
        fourth_form = GuessPasswordForm()
        fifth_form = GuessPasswordForm()

        if not first_form.is_valid() and not second_form.is_valid()  and not third_form.is_valid()  and not fourth_form.is_valid()  and not fifth_form.is_valid():
            pass
        first = first_form.cleaned_data['guess']
        second = second_form.cleaned_data['guess']
        third = third_form.cleaned_data['guess']
        fourth = fourth_form.cleaned_data['guess']
        fifth = fifth_form.cleaned_data['guess']
        return redirect('thanks')