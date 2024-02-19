from django.urls import path, re_path
from .import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('login/',views.login, name='login'),
    path('signup/',views.signup, name='signup'),
    
    
    
#     path('get-all-posts/', views.GetAllPosts),
#     path('create-new-post', views.CreatePost),
#     path('delete-post/', views.DeletePost),
]
