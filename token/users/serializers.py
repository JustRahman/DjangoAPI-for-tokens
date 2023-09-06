from rest_framework import serializers
from .models import Article,News,Image,ImageModel
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article 
        fields ='__all__'

class NewsSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(label="Enter News Id")
    title=serializers.CharField(label="Enter News Title")
    description=serializers.CharField(label="Enter description ")
    content=serializers.CharField(label="Enter content ")
    image_url = serializers.ImageField(required=False)
    class Meta:
        model = News
        fields = ['id', 'title', 'description', 'content','image_url']

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image','id']

class ImageSerializerAV(serializers.ModelSerializer):
    image = serializers.FilePathField(path=(os.path.join(BASE_DIR, 'mediafiles')))
    class Meta:
        model = ImageModel
        fields = ['image','id']