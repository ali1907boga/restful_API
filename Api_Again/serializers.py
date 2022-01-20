from rest_framework import serializers
from blog.models import *


class ArticleSerializers(serializers.ModelSerializer):

    #def get_author(self,obj):
       # return {
      #      'username':obj.author.username
     #   }
    #author = serializers.SerializerMethodField('get_author')


    #author = serializers.HyperlinkedIdentityField(view_name='api_again:user_detail')

    def get_author(self,obj):
        return {
            'username':obj.author.username
        }

    author = serializers.SerializerMethodField('get_author')
    class Meta:
        model = Article
        fields = '__all__'
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'