from rest_framework import serializers
from .models import Book,Journalist

class BookSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Book
        fields = '__all__'


class JournalistSerializer(serializers.ModelSerializer):
    #book = serializers.StringRelatedField(many=True,read_only=True)
    book = BookSerializer(many=True,read_only=True)
    class Meta:
        model = Journalist
        fields = '__all__'