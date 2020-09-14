from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Post3, Coment3


def post(request):
    all_post = Post3.objects.all()
    context = {
        'all_post': all_post,
    }
    return render(request, 'post3/post.html', context)

def detail(request, id):
    post = get_object_or_404(Post3, id=id)
    all_coment = Coment3.objects.all()
    var = len(all_coment)
    context = {
        'var': var,
        'all_coment': all_coment,
        'post': post,
    }
    return render(request, 'post3/detail.html', context)
