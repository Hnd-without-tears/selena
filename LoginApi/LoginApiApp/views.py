from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from.models import Users
from.serializers import UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
# from.models import Post
# from .serializers import PostSerializer

# Create your views here.

@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({"detail": "Not found."}, status=404)
    token, created = Token.objects.get_or_create(user=User)
    serializer = UserSerializer(instance=User)
    # return Response({'success': 'the login was created successful'})
    return Response({"token": token.key, "user": serializer.data})


@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=User)
        return Response({"token": token.key, "user": serializer.data})
    return Response(serializer.errors, status=400)


from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("passed for {}".format(request.user.email))


# @api_view(['GET'])
# def GetAllPosts(request):
#     get_post = Post.objects.all()
#     serializer = PostSerializer(get_post, many=True)
    
#     return Response(serializer.data)

# @api_view(['GET', 'POST'])
# def CreatePost(request):
#     data = request.data
#     serializer = PostSerializer(data=data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({'Success': 'The post was successfully created '})
#     else:
#         return Response(serializer.errors, status=400)
    
    
# @api_view(['DELETE'])
# def DeletePost(request):
#     post_id = request.data.get('post_id')
#     try:
#         post = Post.objects.get(id=post_id)
#         Post.delete()
#         return Response({"Success": "The post was successfully deleted "})
#     except Post.DoesNotExist:
#         return Response({"Error": "The post does not exist"}, status=404),