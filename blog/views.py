from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def lista_postow(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/lista_postow.html', {'posts': posts})

def szczegoly_postu(request, pk):
    # Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/szczegoly_postu.html', {'post': post})

# Create your views here.
