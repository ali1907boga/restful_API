from django.shortcuts import render
from rest_framework import generics,permissions,mixins
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentRetrieveDestroy(generics.RetrieveDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def delete(self, request, *args, **kwargs):
        comment = Comment.objects.filter(pk=kwargs['pk'],author=self.request.user)
        if comment.exists():
            return self.destroy(request,*args,**kwargs)
        else:
            raise ValidationError('this comment does not belong to you')

class SendLike(generics.CreateAPIView,mixins.DestroyModelMixin):
    serializer_class = LikerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        comment = Comment.objects.get(pk=self.kwargs['pk'])
        return Like.objects.filter(liker=user,comment=comment)

    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise serializer.ValidationError('you are already liked this exist')
        serializer.save(liker=self.request.user,comment=Comment.objects.get(pk=self.kwargs['pk']))# add in user_list

    def delete(self,request,*args,**kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError('you have never liked this comment')