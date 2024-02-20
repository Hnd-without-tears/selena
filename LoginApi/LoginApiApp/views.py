# from django.shortcuts import render
# from rest_framework.decorators import api_view
from rest_framework.response import Response
# from.models import Users
from.serializers import UserSerializer
from rest_framework.exceptions import AuthenticationFailed
# from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
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
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.contrib.auth.hashers import make_password, check_password
# from .models import Users
# import datetime

# # Signup API endpoint
# @csrf_exempt
# def signup(request):
#     if request.method == 'POST':
#         # Get data from request
#         data = request.POST
        
#         # Check if username and email already exist
#         if Users.objects.filter(username=data['username']).exists() or Users.objects.filter(email=data['email']).exists():
#             return JsonResponse({'error': 'Username or email already exists'}, status=400)
        
#         # Create new user
#         user = Users(
#             username=data['username'],
#             password=make_password(data['password']),  # Hash the password
#             email=data['email'],
#             firstname=data.get('firstname', ''),
#             lastname=data.get('lastname', ''),
#             createdat=datetime.datetime.now(),
#             updatedat=datetime.datetime.now(),
#             role=data.get('role', '')
#         )
#         user.password = make_password(user.password)
#         user.save()
#         return JsonResponse({'message': 'User created successfully'}, status=201)
#     else:
#         return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

# # Login API endpoint
# @csrf_exempt
# def login(request):
#     if request.method == 'POST':
#         # Get data from request
#         data = request.POST
        
#         # Check if username exists
#         if Users.objects.filter(username=data['username']).exists():
#             user = Users.objects.get(username=data['username'])
#             # Check if password matches
#             if check_password(data['password'], user.password):
#                 return JsonResponse({'message': 'Login successful'}, status=200)
#             else:
#                 return JsonResponse({'error': 'Invalid password'}, status=401)
#         else:
#             return JsonResponse({'error': 'User does not exist'}, status=404)
#     else:
#         return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)


from rest_framework.views import APIView
import jwt, datetime

class SigninView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        
        user = User.objects.filter(email=email).first()
        
        if user is None:
            raise AuthenticationFailed("User does not exist")
        
        if not user.check_password(password):
            raise AuthenticationFailed("Invalid password!")
        
        # payload = {
        #     'id': user.id,
        #     'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        #     'iat': datetime.datetime.utcnow()
        # }
        
        # token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')
        
        # response = Response()
        
        # response.set_cookie(key='jwt', value=token, httponly=True)
        # response.data = {
        #     'jwt': token
        # }
        return Response({'message': 'success'})
    
    
    
class ViewUser(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
            
        if not token:
            raise AuthenticationFailed("unauthenticated")
            
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('unauthenticated!')
            
        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
            
        return Response(serializer.data)
    
    
class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'deleted successfully'
        }
        return response