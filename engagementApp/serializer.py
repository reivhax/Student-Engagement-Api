from rest_framework import serializers
from .models import Articles
from favourites.serializer import CommentSerializer
from django.contrib.auth.models import User
from . import views


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    favourites = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True)
    # highlight = serializers.HyperlinkedIdentityField(
    #     view_name='users', format='html')

    def get_favourites(self, obj):
        return obj.favourites.count()

    class Meta:
        model = Articles
        fields = ('url', 'id', 'owner',
                  'title', 'content','image','category','author', 'favourites','comments')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # articles = serializers.HyperlinkedRelatedField(
    #     many=True, view_name='users', read_only=True)
    class Meta:
        model=User
        fields = ('url','id','username','articles')
