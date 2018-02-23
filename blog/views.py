from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

def lista_postow(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/lista_postow.html', {'posts': posts})

def szczegoly_postu(request, pk):
    # Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/szczegoly_postu.html', {'post': post})

def nowy_post(request):
    # Gdy prześlemy formularz, wracamy do tego samego widoku, ale tym razem mamy nieco więcej danych w zapytaniu (zmiennej request) - a dokładnie w request.POST.
    # dlatego musimy sprawdzić czy przychodzimy z POST, czy nie
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('szczegoly_postu', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/edycja_postu.html', {'form': form})

def edycja_postu(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('szczegoly_postu', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/edycja_postu.html', {'form': form})

# Create your views here.
