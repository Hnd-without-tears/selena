from rest_framework import serializers
from django.contrib.auth.models import User
# from .models import Post

class UserSerializer(serializers.ModelSerializer):
     class Meta:
         model = User
         fields = '__all__'