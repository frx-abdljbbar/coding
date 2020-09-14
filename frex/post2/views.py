from django.shortcuts import render, get_object_or_404
from .models import Post2, Coment2
# Create your views here.

def post(request):
    all_post = Post2.objects.all()
    context = {
        'all_post': all_post,
    }
    return render(request, 'post2/post.html', context)

def detail(request, id):
    post = get_object_or_404(Post2, id=id)
    all_coment = Coment2.objects.all()
    var = len(all_coment)
    context = {
        'post': post,
        'var': var,
        'all_coment': all_coment,
    }
    return render(request, 'post2/detail.html', context)
