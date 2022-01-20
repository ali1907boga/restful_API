from django.shortcuts import render
from django.shortcuts import render
from blog.models import *
from rest_framework.generics import *
from rest_framework import serializers
from .serializers import *
from django.contrib.auth.models import User
from .permissions import *
from rest_framework.authentication import BasicAuthentication


class All_Api(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers
    permission_classes = [IsAuthorOrReadOnly,]
    authentication_classes = [BasicAuthentication,]


class Article_Detail(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]

class User_Detail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer




