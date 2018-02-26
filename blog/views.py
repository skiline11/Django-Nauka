from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required

def lista_postow(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/lista_postow.html', {'posts': posts})

def szczegoly_postu(request, pk):
    # Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/szczegoly_postu.html', {'post': post})

@login_required
def nowy_post(request):
    # Gdy prześlemy formularz, wracamy do tego samego widoku, ale tym razem mamy nieco więcej danych w zapytaniu (zmiennej request) - a dokładnie w request.POST.
    # dlatego musimy sprawdzić czy przychodzimy z POST, czy nie
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('szczegoly_postu', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/edycja_postu.html', {'form': form, 'nazwa': 'Nowy post'})

@login_required
def edycja_postu(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('szczegoly_postu', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/edycja_postu.html', {'form': form, 'nazwa': "Edycja postu"})

@login_required
def lista_wersji_roboczych(request):
    posty = Post.objects.filter(published_date__isnull=True).order_by('-created_date')
    return render(request, 'blog/robocze.html', {'posty': posty})

@login_required
def publikacja_postu(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('szczegoly_postu', pk=pk)

@login_required
def usuwanie_postu(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('lista_postow')


def dodawanie_komentarza(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/dodawanie_komentarza.html', {'form': form})
# Create your views here.


@login_required
def zatwierdzanie_komentarza(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('szczegoly_postu', pk=comment.post.pk)

@login_required
def usuwanie_komentarza(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('szczegoly_postu', pk=comment.post.pk)