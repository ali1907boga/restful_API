from rest_framework import serializers
from .models import *



class CommentSerializer(serializers.ModelSerializer):
    author1 = serializers.ReadOnlyField(source='author1.username')
    def get_likes(self,comment):
        return Like1.objects.filter(comment1=comment).count()
    likes = serializers.SerializerMethodField('get_likes')
    class Meta:
        model = Comment1
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like1
        fields = '__all__'