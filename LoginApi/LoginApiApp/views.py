# from django.shortcuts import render
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from.models import Users
# from.serializers import UserSerializer
# from rest_framework.authtoken.models import Token
# from django.contrib.auth.models import User
# from django.shortcuts import get_object_or_404
# # from.models import Post
# # from .serializers import PostSerializer

# # Create your views here.

# @api_view(['POST'])
# def login(request):
#     user = get_object_or_404(User, username=request.data['username'])
#     if not user.check_password(request.data['password']):
#         return Response({"detail": "Not found."}, status=404)
#     token, created = Token.objects.get_or_create(user=User)
#     serializer = UserSerializer(instance=User)
#     # return Response({'success': 'the login was created successful'})
#     return Response({"token": token.key, "user": serializer.data})


# @api_view(['POST'])
# def signup(request):
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         user = User.objects.get(username=request.data['username'])
#         user.set_password(request.data['password'])
#         user.save()
#         token = Token.objects.create(user=User)
#         return Response({"token": token.key, "user": serializer.data})
#     return Response(serializer.errors, status=400)


# from rest_framework.decorators import authentication_classes, permission_classes
# from rest_framework.authentication import SessionAuthentication, TokenAuthentication
# from rest_framework.permissions import IsAuthenticated


# @api_view(['GET'])
# @authentication_classes([SessionAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def test_token(request):
#     return Response("passed for {}".format(request.user.email))





# Import necessary modules
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
from .models import Users
import datetime

# Signup API endpoint
@csrf_exempt
def signup(request):
    if request.method == 'POST':
        # Get data from request
        data = request.POST
        
        # Check if username and email already exist
        if Users.objects.filter(username=data['username']).exists() or Users.objects.filter(email=data['email']).exists():
            return JsonResponse({'error': 'Username or email already exists'}, status=400)
        
        # Create new user
        user = Users(
            username=data['username'],
            password=make_password(data['password']),  # Hash the password
            email=data['email'],
            firstname=data.get('firstname', ''),
            lastname=data.get('lastname', ''),
            createdat=datetime.datetime.now(),
            updatedat=datetime.datetime.now(),
            role=data.get('role', '')
        )
        user.save()
        return JsonResponse({'message': 'User created successfully'}, status=201)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

# Login API endpoint
@csrf_exempt
def login(request):
    if request.method == 'POST':
        # Get data from request
        data = request.POST
        
        # Check if username exists
        if Users.objects.filter(username=data['username']).exists():
            user = Users.objects.get(username=data['username'])
            # Check if password matches
            if check_password(data['password'], user.password):
                return JsonResponse({'message': 'Login successful'}, status=200)
            else:
                return JsonResponse({'error': 'Invalid password'}, status=401)
        else:
            return JsonResponse({'error': 'User does not exist'}, status=404)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
