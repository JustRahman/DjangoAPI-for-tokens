from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from .serializers import NewsSerializer,ImageSerializer,ArticleSerializer,ImageSerializerAV
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from .models import Article,News,Image,ImageModel
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import viewsets
from rest_framework import generics

# Create your views here.

class UserListView(APIView):
    queryset=Article.objects.all()
    serializer_class = ArticleSerializer

    def get_queryset(self):
        return Article.objects.filter(name=self.request.user.pk).all()
    def get(self,request):
        allBooks=Article.objects.all().values()
        return Response({"Message":"List of Users", "Users List":allBooks})

    def post(self,request):
        print('qqq data is : ',request.data)
        serializer_obj=ArticleSerializer(data=request.data)
        if(serializer_obj.is_valid()):

            Article.objects.create(id=serializer_obj.data.get("id"),
                            name=serializer_obj.data.get("name"),
                            age=serializer_obj.data.get("age"),
                            email=serializer_obj.data.get("email"),
                            password=serializer_obj.data.get("password")
                            )

        book=Article.objects.all().filter(id=request.data["id"]).values()
        return Response({"Message":"New User Added!", "User":book})

class CustomAuthToken(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            
        })

class NewsApiView(APIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [
        permissions.AllowAny]
    def get(self,request):
        allNews=News.objects.all().values()
        return Response({"Message":"List of News", "News List":allNews})

    def post(self,request):
        print('Request data is : ',request.data)
        serializer_obj=NewsSerializer(data=request.data)
        if(serializer_obj.is_valid()):

            News.objects.create(id=serializer_obj.data.get("id"),
                            title=serializer_obj.data.get("title"),
                            description=serializer_obj.data.get("description"),
                            content=serializer_obj.data.get("content"),
                            image_url = serializer_obj.data.get("image_url"),   
                            )

        news=News.objects.all().filter(id=request.data["id"]).values()
        return Response({"Message":"New Book Added!", "Book":news})

class ImageApiView(APIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [
        permissions.AllowAny]

    def get(self,request):
        allNews=Image.objects.all().values()
        return Response({"Message":"List of News", "News List":allNews})

    def post(self,request):
        print('Request data is : ',request.data)
        serializer_obj=ImageSerializer(data=request.data)
        if(serializer_obj.is_valid()):

            Image.objects.create(id=serializer_obj.data.get("id"),
                            image=serializer_obj.data.get("image")
                            
                            )

        news=Image.objects.all().filter(id=request.data["id"]).values()
        return Response({"Message":"New Book Added!", "Book":news})

class ImageAV(generics.ListCreateAPIView):
    queryset = ImageModel.objects.all()
    serializer_class = ImageSerializerAV

 

   
