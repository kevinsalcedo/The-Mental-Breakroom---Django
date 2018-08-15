from rest_framework import serializers
from .models import Disorder, Story, BlogPost

class DisorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disorder
        fields = ('id', 'name')

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ('id', 'title', 'content', 'date_created', 'date_modified', 'author', 'disorder')
        read_only_fields = ('date_created', 'date_modified')

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ('d', 'title', 'content', 'date_created', 'author')
        read_only_fields = ('date_created')
