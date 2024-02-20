from django.urls import path, re_path
# from .import views
from .views import SigninView,LoginView, ViewUser,LogoutView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('signup',SigninView.as_view()),
    path('login',LoginView.as_view()),
    path('user',ViewUser.as_view()),
    path('logout',LogoutView.as_view()),
    
    
    
#     path('get-all-posts/', views.GetAllPosts),
#     path('create-new-post', views.CreatePost),
#     path('delete-post/', views.DeletePost),
]
