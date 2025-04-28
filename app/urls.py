
from django.contrib import admin
from django.urls import path
from app.views.user import CreateUser , LoginUserView ,RetriveUser , UpdateUser ,DestroyUser ,RetriveAllUser , RetriveUserByID
from app.views.post import CreatePost ,RetrivePost , RetrieveUserPosts , RetrieveAllPosts ,UpdatePost , DestroyPost , LikePost , LikePostExist

from app.views.announce import BCADeleteAPIView , BSCDeleteAPIView , BAFDeleteAPIView , BBIDeleteAPIView , BMSDeleteAPIView

from app.views.announce import BCACreateAPIView ,BSCCreateAPIView ,BAFCreateAPIView , BBICreateAPIView , BMSCreateAPIView 

from app.views.announce import BCAListAPIView , BSCListAPIView ,BAFListAPIView , BBIListAPIView ,BMSListAPIView

from app.views.Lectureview import LecCreateBCA , LecCreateBSC , LecCreateBAF , LecCreateBBI , LecCreateBMS , SportsApplication , CreateComplaint

from app.views.Lectureview import LecGetBCA , LecGetBSC , LecGetBAF , LecGetBBI , LecGetBMS , GetSportsApplication  , GetComplaint , DeleteSportsApplication ,DeleteComplaint


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

    path('announce/bca/', BCACreateAPIView.as_view()),
    path('announce/bsc/', BSCCreateAPIView.as_view()),
    path('announce/bms/', BMSCreateAPIView.as_view()),
    path('announce/bbi/', BBICreateAPIView.as_view()),
    path('announce/baf/', BAFCreateAPIView.as_view()),

    path('announce/get/bca/', BCAListAPIView.as_view()),
    path('announce/get/bsc/', BSCListAPIView.as_view()),
    path('announce/get/bms/', BMSListAPIView.as_view()),
    path('announce/get/bbi/', BBIListAPIView.as_view()),
    path('announce/get/baf/', BAFListAPIView.as_view()),

    path('bca/delete/<int:pk>/', BCADeleteAPIView.as_view(), name='bca-delete'),
    path('bsc/delete/<int:pk>/', BSCDeleteAPIView.as_view(), name='bsc-delete'),
    path('baf/delete/<int:pk>/', BAFDeleteAPIView.as_view(), name='baf-delete'),
    path('bbi/delete/<int:pk>/', BBIDeleteAPIView.as_view(), name='bbi-delete'),
    path('bms/delete/<int:pk>/', BMSDeleteAPIView.as_view(), name='bms-delete'),

    path('lecture/create/bca/' , LecCreateBCA.as_view()),
    path('lecture/get/bca/' , LecGetBCA.as_view()),

    path('lecture/create/bsc/' , LecCreateBSC.as_view()),
    path('lecture/get/bsc/' , LecGetBSC.as_view()),

    path('lecture/create/bms/' , LecCreateBMS.as_view()),
    path('lecture/get/bms/' , LecGetBMS.as_view()),

    path('lecture/create/bbi/' , LecCreateBBI.as_view()),
    path('lecture/get/bbi/' , LecGetBBI.as_view()),

    path('lecture/create/baf/' , LecCreateBAF.as_view()),
    path('lecture/get/baf/' , LecGetBAF.as_view()),

    path('sports/create/' , SportsApplication.as_view()),
    path('sports/get/' , GetSportsApplication.as_view()),

    path('complaint/create/' , CreateComplaint.as_view() ) ,
    path('complaint/get/' , GetComplaint.as_view() ),

    path('sports/delete/<int:pk>/', DeleteSportsApplication.as_view()),
    path('complaint/delete/<int:pk>/', DeleteComplaint.as_view()), 

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
