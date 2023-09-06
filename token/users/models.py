from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver 
from rest_framework.authtoken.models import Token  


class Article(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    email=models.CharField(max_length=2000)
    password=models.CharField(max_length=32)

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class News(models.Model):
    id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    content=models.CharField(max_length=2000)
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)

class Image(models.Model):
    id=models.IntegerField(primary_key=True)
    image = models.ImageField()

    def __str__(self):
        return str(self.image)


class ImageModel(models.Model):
    image=models.FilePathField()

    def __str__(self):
        return str(self.image)
