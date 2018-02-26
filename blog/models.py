from django.db import models
from django.utils import timezone

# Uwaga !!!
# Zawsze po stworzeniu nowego modelu nleży wykonać migracje :
#   python manage.py makemigrations blog

class Post(models.Model):
    author =            models.ForeignKey('auth.User')
    title =             models.CharField(max_length=200)
    text =              models.TextField()
    created_date =      models.DateTimeField(default=timezone.now)
    published_date =    models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        # Uwaga: Używamy tutaj .comments, co odnosi się do 'related_name' w modelu Comment
        # dzięki temu możemy zliczyć komentarze które są powiązane z tym postem i mają approved_comment ustawione na True
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    # "related_name" pozwala nam na dostęp do komentarzy z poziomu modelu Post
    post =              models.ForeignKey('blog.Post', related_name='comments')
    author =            models.CharField(max_length=200)
    text =              models.TextField()
    created_date =      models.DateTimeField(default=timezone.now)
    approved_comment =  models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

# Create your models here.
