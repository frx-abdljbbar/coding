from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Post1, Coment1


def post(request):
    all_post = Post1.objects.all()
    context = {
        'all_post': all_post,
    }
    return render(request, 'post1/post.html', context)

def detail(request, id):
    post = get_object_or_404(Post1, id=id)
    all_coment = Coment1.objects.all()
    var = len(all_coment)
    context = {
        'post': post,
        'var': var,
        'all_coment': all_coment,
    }
    return render(request, 'post1/detail.html', context)
