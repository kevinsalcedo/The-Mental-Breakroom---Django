from django.shortcuts import render
from rest_framework import generics
from .serializers import DisorderSerializer, StorySerializer, BlogPostSerializer
from .models import Disorder, Story, BlogPost

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

class BlogPostDetailsView(generics.ListAPIView):
    serializer_class = BlogPostSerializer

    def get_queryset(self):
        queryset = BlogPost.objects.all()
        disorderId = self.request.query_params.get('disorder', None)
        if disorderId is not None:
            queryset = queryset.filter(blogpost__disorder=disorderId)
        return queryset

