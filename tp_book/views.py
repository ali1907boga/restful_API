from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework import permissions
from rest_framework import generics,permissions



class GetAllData(APIView):
    def get(self,request):
        query = Book.objects.all()
        serializers = BookSerializer(query,many=True,context={'request':request})
        return Response(serializers.data,status=status.HTTP_200_OK)


class GetFavData(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
        query = Book.objects.filter(fav=True)
        serializers = BookSerializer(query,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)

class UpdateFvaData(APIView):

    def get(self,request,pk):
        query = Book.objects.get(pk=pk)
        serializer = BookSerializer(query)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request,pk):
        query = Book.objects.get(pk=pk)
        serializer = BookSerializer(query,data=request.data)# har vaght az request.data estefade kardi bayad is_valid estefade koni.
        if serializer.is_valid():
            serializer.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


class PostModel(APIView):
    def post(self,request):
        serializers = BookSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)


class Update(APIView):
    def put(self,request,pk):
        query = Book.objects.get(pk=pk)
        serializers = BookSerializer(query,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_200_OK)

class SearchData(APIView):

    def get(self,request):
        search = request.GET['name']
        query = Book.objects.filter(name__icontains=search)
        serializers = BookSerializer(query,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)

class DeleteUpdateGet(APIView):

    def delete(self,request,pk):
        query = Book.objects.get(pk=pk)
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self,request,pk):
        query = Book.objects.get(pk=pk)
        serializers = BookSerializer(query,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)

    def get(self,request,pk):

        query = Book.objects.get(pk=pk)
        serializers = BookSerializer(query)
        return Response(serializers.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def allapi(request):
    if request.method == 'GET':
        query = Book.objects.all().order_by('-created_at')
        serializers = BookSerializer(query,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)

@api_view(['POST'])
def PostApi(request):
    if request.method == 'POST':
        serializers = BookSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','DELETE','GET'])
def update_delete_get(request,pk):
    if request.method == 'PUT':
        query = Book.objects.get(pk=pk)
        serializers = BookSerializer(query,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)

    if request.method == 'DELETE':
        query = Book.objects.get(pk=pk)
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        query = Book.objects.get(pk=pk)
        serializers = BookSerializer(query)
        return Response(serializers.data,status=status.HTTP_200_OK)



class BookList(APIView):
    def get(self,request):
        query = Book.objects.all()
        serializers  = BookSerializer(query,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)



class JournalistList(APIView):
    def get(self, request):
        query = Journalist.objects.all()
        serializers = JournalistSerializer(query, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


