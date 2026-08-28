from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.parsers import MultiPartParser, FormParser

from .models import UserProfile, Author
from .serializers import UserProfileSerializer, AuthorSerializer

class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    parser_classes = (MultiPartParser, FormParser)

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    parser_classes = (MultiPartParser, FormParser)
    