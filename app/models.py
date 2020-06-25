from django.db import models
from django.urls import reverse

# Create your models here.
class Gallery(models.Model):
    public=models.IntegerField()
    name=models.CharField(max_length=100)
    description=models.TextField(max_length=3000)
    root=models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("app:gallery",kwargs={'pk':self.pk})

class Pages(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to="pages")
    text=models.TextField(max_length=3000)
    human1_text = models.TextField(max_length=3000,blank=True)
    human1_image=models.ImageField(upload_to="pages",blank=True)
    human2_text = models.TextField(max_length=3000,blank=True)
    human2_image=models.ImageField(upload_to="pages",blank=True)
    dog1_text = models.TextField(max_length=3000,blank=True)
    dog1_image=models.ImageField(upload_to="pages",blank=True)
    dog2_text = models.TextField(max_length=3000,blank=True)
    dog2_image=models.ImageField(upload_to="pages",blank=True)
    dog3_text = models.TextField(max_length=3000,blank=True)
    dog3_image=models.ImageField(upload_to="pages",blank=True)
