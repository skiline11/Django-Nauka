from django import forms
#importujemy nasz model wpisu
from .models import Post, Comment

class PostForm(forms.ModelForm):

    #wskazujemy jaki model ma być wykorzystany, i jakie pola ma obsługiwać nasz formularz
    class Meta:
        model = Post
        fields = ('title', 'text')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text')
