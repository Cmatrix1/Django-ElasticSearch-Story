from rest_framework import serializers
from .models import StoryModel, TagModel



class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagModel
        fields = ('id', 'title')


class StorySerializer(serializers.ModelSerializer):
    tag = TagSerializer(many=True)
    class Meta:
        model = StoryModel
        fields = ('id',
                 'title',
                #  'link',
                #  'content',
                #  'slug',
                 'tag',
                #  'created_at',
                #  'updated_at'
                )