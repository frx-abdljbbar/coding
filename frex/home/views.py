from django.shortcuts import render, get_object_or_404, redirect, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import login, authenticate
from .models import Home
from profille.models import Profile

def home(request):
    home = Home.objects.all()
    context = {
        'home': home,
    }
    return render(request, 'home/home.html', context)

def signup(request):
    form = UserRegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            print(request, user)
            slug = user.username
            return redirect("http://127.0.0.1:8000/profile/%s" % slug)

    context = {
        'form': form,
    }
    return render(request, 'registration/signup.html', context)
