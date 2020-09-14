from django.shortcuts import render, get_object_or_404
from .models import Post, Coment
from .forms import ComentForm
from profille.models import Profile
def add_coment(request):
    if request.method == 'POST':
        form = ComentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ComentForm()
    context = {
        'form': form,
    }
    return render(request, 'post/detail.html', context)

def post(request):
    all_post = Post.objects.all()
    context = {
        'all_post': all_post,
    }
    return render(request, 'post/post.html', context)

def detail(request, id):
    post = get_object_or_404(Post, id=id)
    all_coment = Coment.objects.all()
    var = len(all_coment)
    profile = Profile.objects.all()
    context = {
        'profile': profile,
        'post': post,
        'var': var,
        'all_coment': all_coment,
    }
    return render(request, 'post/detail.html', context)
