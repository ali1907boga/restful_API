from django.shortcuts import render
from .models import *
from rest_framework.generics import *
from rest_framework import mixins
from .serializers import CommentSerializer,LikeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError




class All_Comment(ListCreateAPIView):

    queryset = Comment1.objects.all()
    serializer_class = CommentSerializer
    def perform_create(self, serializer):
        serializer.save(author1=self.request.user)


class CommentRetrieveDestroy(RetrieveDestroyAPIView):
    queryset = Comment1.objects.all()
    serializer_class = CommentSerializer

    def delete(self, request, *args, **kwargs):
        comment = Comment1.objects.filter(pk=kwargs['pk'],author1=self.request.user)
        if comment.exists():
            return self.destroy(request,*args,**kwargs)
        raise ValidationError('this comment not own you.')

class DeleteUpdateGet(APIView):

    def delete(self,request,pk):
        query = Comment1.objects.filter(pk=pk,author1=self.request.user)
        if query.exists():
            query.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        raise ValidationError('not you comment')


@api_view(['POST'])
def sendlike(request,pk):
    user = request.user
    comment = Comment1.objects.get(pk=pk)
    query = Like1.objects.filter(liker1=user,comment1=comment)
    serializers = LikeSerializer(data=request.data)
    if serializers.is_valid():
        if query.exists():
            raise ValidationError('like past')
        serializers.save(liker=request.user,comment1=Comment1.objects.get(pk=pk))
        return Response(serializers.data,status=status.HTTP_200_OK)



class SendLike(CreateAPIView,mixins.DestroyModelMixin):
    serializer_class = LikeSerializer

    def get_queryset(self):
        user = self.request.user
        comment = Comment1.objects.get(pk=self.kwargs['pk'])
        return Like1.objects.filter(liker1=user,comment1=comment)

    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise ValidationError('you liked this comment in past')
        serializer.save(liker1=self.request.user,comment1=Comment1.objects.get(pk=self.kwargs['pk']))#ADD MOKNAD METHOD performe_create haman kar add kardan ra mikonad
    def delete(self,request,*args,**kwargs):
        like = Like1.objects.filter(liker1=request.user,comment1=Comment1.objects.get(pk=self.kwargs['pk']))
        if like.exists():
            like.delete()
        raise ValidationError('this is not your like')







class Posst(APIView):#input data in browsable_api json exampe {"text1":"something"} text1 field name in model.py
    def post(self,request):
        serializers = CommentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save(author1=self.request.user)
            return Response(serializers.data,status=status.HTTP_201_CREATED)



class Sendlike(APIView):
    def post(self,request,pk):
        user = self.request.user
        comment = Comment1.objects.get(pk=pk)
        like = Like1.objects.filter(liker1=user,comment1=comment)
        serializers = LikeSerializer(data=request.data)
        if serializers.is_valid() & like.exists():
            print('xx')
            raise ValidationError('you like past time this comment')
        elif serializers.is_valid():
            serializers.save(Like1.objects.filter(liker1=user,comment1=comment))
            return Response(serializers.data,status=status.HTTP_200_OK)

