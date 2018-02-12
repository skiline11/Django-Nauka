from django.shortcuts import render

def lista_postow(request):
    return render(request, 'blog/post_list.html', {})

# Create your views here.
