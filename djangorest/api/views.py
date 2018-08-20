from django.shortcuts import render
from rest_framework import generics
from .serializers import DisorderSerializer, StorySerializer, BlogPostSerializer, LocalResourceSerializer
from .models import Disorder, Story, BlogPost, LocalResource

class CreateView(generics.ListCreateAPIView):
    queryset = Disorder.objects.all()
    serializer_class = DisorderSerializer

    def perform_create(self, serializer):
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Disorder.objects.all()
    serializer_class = DisorderSerializer

class StoryCreateView(generics.ListCreateAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer

    def perform_create(self, serializer):
        serializer.save()

class StoryDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer

class BlogPostCreateView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def perform_create(self, serializer):
        serializer.save()

class BlogPostDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class LocalResourceCreateView(generics.ListCreateAPIView):
    queryset=LocalResource.objects.all()
    serializer_class = LocalResourceSerializer

    def perform_create(self, serializer):
        serializer.save()

class LocalResourceDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LocalResource.objects.all()
    serializer_class = LocalResourceSerializer

