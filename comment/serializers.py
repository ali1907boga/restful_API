from rest_framework import serializers
from .models import *

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    author_id = serializers.ReadOnlyField(source='author.id')

    def get_likes(self,i):
       # return Like.objects.filter(comment=comment).count()
        return Like.objects.filter(comment_id=i).count()
    likes = serializers.SerializerMethodField('get_likes')
    class Meta:
        model = Comment
        fields = '__all__'


class LikerSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model = Like
        fields = '__all__'

