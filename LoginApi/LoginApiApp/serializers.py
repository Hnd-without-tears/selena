from rest_framework import serializers
from django.contrib.auth.models import User
# from .models import Post

class UserSerializer(serializers.ModelSerializer):
     class Meta:
         model = User
         fields = '__all__'
         
         extra_kwargs = {
             'password': {'write_only': True}
         }
         
def create(self, validate_date):
    password = validate_date.pop('password', None)
    instance = self.Meta.model(+ +validate_date)
    if password is not None:
        instance.set_password(password)
    instance.save()
    return instance     
