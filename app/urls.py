
from django.contrib import admin
from django.urls import path
from app.views.user import CreateUser , LoginUserView ,RetriveUser , UpdateUser ,DestroyUser ,RetriveAllUser , RetriveUserByID
from app.views.post import CreatePost ,RetrivePost , RetrieveUserPosts , RetrieveAllPosts ,UpdatePost , DestroyPost , LikePost , LikePostExist
from app.views.announce import COCreateAPIView ,EECreateAPIView ,EJCreateAPIView , MECreateAPIView , IFCreateAPIView 
from app.views.announce import COListAPIView , EEListAPIView ,EJListAPIView , IFListAPIView ,MEListAPIView
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('user/create/', CreateUser.as_view()),
    path('user/get/', RetriveAllUser.as_view()),
    path('user/login/' , LoginUserView.as_view()),
    path('user/', RetriveUser.as_view()),
    path('user/<int:pk>/', RetriveUserByID.as_view()),
    path('user/update/', UpdateUser.as_view()),
    path('user/delete/<int:pk>', DestroyUser.as_view()),

    path('post/create/' , CreatePost.as_view()),
    path('post/<int:pk>/' , RetrivePost.as_view()),
    path('post/update/<int:pk>/', UpdatePost.as_view()),
    path('post/delete/<int:pk>/', DestroyPost.as_view()),
    path('post/user/all/' , RetrieveUserPosts.as_view()),
    path('post/like/<int:pk>/', LikePost.as_view()),
    path('post/Getlike/<int:pk>/', LikePostExist.as_view()),
    path('posts/', RetrieveAllPosts.as_view(), name='retrieve-all-posts'),

    path('announce/co/', COCreateAPIView.as_view()),
    path('announce/ee/', EECreateAPIView.as_view()),
    path('announce/ej/', EJCreateAPIView.as_view()),
    path('announce/me/', MECreateAPIView.as_view()),
    path('announce/if/', IFCreateAPIView.as_view()),

    path('announce/get/co/', COListAPIView.as_view()),
    path('announce/get/ee/', EEListAPIView.as_view()),
    path('announce/get/ej/', EJListAPIView.as_view()),
    path('announce/get/me/', MEListAPIView.as_view()),
    path('announce/get/if/', IFListAPIView.as_view()),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
