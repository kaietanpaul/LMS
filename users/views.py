from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from . import forms
from django.urls import reverse_lazy


def registration_view(request):
    form = forms.RegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()

            return redirect(reverse_lazy('home:home'))
    return render(request, 'users/registration.html', {'form': form})
