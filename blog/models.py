from django.db import models
from tinymce.models import HTMLField
from django.template.defaultfilters import slugify
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.shortcuts import render, get_object_or_404

User = get_user_model()

class Category(models.Model):
    title = models.CharField(max_length=20)

    @property
    def slug(self):
        return slugify(self.title)

    def get_absolute_url(self):
        return reverse('blog:blog_title', kwargs={'pk': self.pk, 'slug': self.slug})

    def __str__(self):
        return self.title

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()




class Post(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    content = HTMLField()
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default = 0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-details',kwargs={
            'id': self.id
        })

    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey(Post, related_name='comments', on_delete = models.CASCADE)
    def __str__(self):
        return self.user.username
