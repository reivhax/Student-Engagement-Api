from rest_framework import serializers
from .models import Favourite, Comments


class FavouriteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Favourite
        fields = ('user_uuid', 'article')


class CommentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Comments
        fields = ('user_uuid', 'comment', 'display_name', 'article')
