from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from app.manager import UserManager

# Create your models here.

class User(AbstractBaseUser):
    username = None
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True , max_length=16)
    first_name = models.CharField(max_length=30 , default = "name")  
    last_name = models.CharField(max_length=30 , default = "name")   
    bio = models.CharField(max_length=164 ,  null = True , default = "Update your bio")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name']
    object = UserManager()

class Post(models.Model):
    title = models.CharField(max_length = 32)
    description = models.CharField(max_length=164)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    username = models.CharField(max_length = 32 , default = 'NES_dept')

class PostLike(models.Model):
    post = models.ForeignKey(Post, null=False , on_delete = models.CASCADE)
    user = models.ForeignKey(User , null=False , on_delete = models.CASCADE)

    class META:
        unique_together = (("post","user"),)

class CO(models.Model):
    text = models.CharField(max_length = 64)
    created_at = models.DateField(auto_now_add=True)

class IF(models.Model):
    text = models.CharField(max_length = 64)
    created_at = models.DateField(auto_now_add=True)

class ME(models.Model):
    text = models.CharField(max_length = 64)
    created_at = models.DateField(auto_now_add=True)

class EE(models.Model):
    text = models.CharField(max_length = 64)
    created_at = models.DateField(auto_now_add=True)

class EJ(models.Model):
    text = models.CharField(max_length = 64)
    created_at = models.DateField(auto_now_add=True)