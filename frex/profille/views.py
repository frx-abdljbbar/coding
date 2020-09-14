from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile
from .forms import ProfileForm, UserForm

def profile(request, slug):
    profile = get_object_or_404(Profile, slug=slug)
    #profile = Profile.objects.get(slug=slug)
    context = {
        'profile': profile,
    }
    return render(request, 'profile/profile.html', context)

def edit_profile(request, slug):
    profile = get_object_or_404(Profile, slug=slug)
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        user_form = UserForm(request.POST, instance=request.user)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            new_profile = profile_form.save(commit=False)
            #new_profile.user = request.user
            new_profile.save()
            return redirect("http://127.0.0.1:8000/profile/%s" % slug)
    else:
        profile_form = ProfileForm(instance=profile)
        user_form = UserForm(instance=request.user)
    context = {
        'profile_form': profile_form,
        'user_form': user_form
    }
    return render(request, 'profile/edit_profile.html', context)
