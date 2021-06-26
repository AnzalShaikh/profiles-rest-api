from rest_framework.response import Response
from rest_framework import viewsets
from profiles_api import serializers
from profiles_api import models




class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()