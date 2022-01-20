from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView
from .serializers import *
from blog.models import Article
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser

class ArticleList(ListAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetail(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAdminUser,]

class UserList(ListAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer