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

class BCA(models.Model):
    text = models.CharField(max_length = 64)
    created_at = models.DateField(auto_now_add=True)

class BMS(models.Model):
    text = models.CharField(max_length = 64)
    created_at = models.DateField(auto_now_add=True)

class BBI(models.Model):
    text = models.CharField(max_length = 64)
    created_at = models.DateField(auto_now_add=True)

class BSC(models.Model):
    text = models.CharField(max_length = 64)
    created_at = models.DateField(auto_now_add=True)

class BAF(models.Model):
    text = models.CharField(max_length = 64)
    created_at = models.DateField(auto_now_add=True)

class LecturesBMS(models.Model):
    title = models.CharField(max_length = 32)
    link = models.CharField(max_length= 64)
    time = models.CharField(max_length=32 , default = "7:00 AM") 
    password = models.CharField(max_length=32)

class LecturesBCA(models.Model):
    title = models.CharField(max_length = 32)
    link = models.CharField(max_length= 64)
    time = models.CharField(max_length=32 , default = "7:00 AM") 
    password = models.CharField(max_length=32)

class LecturesBBI(models.Model):
    title = models.CharField(max_length = 32)
    link = models.CharField(max_length= 64)
    time = models.CharField(max_length=32 , default = "7:00 AM") 
    password = models.CharField(max_length=32)

class LecturesBSC(models.Model):
    title = models.CharField(max_length = 32)
    link = models.CharField(max_length= 64)
    time = models.CharField(max_length=32 , default = "7:00 AM") 
    password = models.CharField(max_length=32)

class LecturesBAF(models.Model):
    title = models.CharField(max_length = 32)
    link = models.CharField(max_length= 64)
    time = models.CharField(max_length=32 , default = "7:00 AM") 
    password = models.CharField(max_length=32)

class Sports(models.Model):
    name = models.CharField(max_length=64)
    enrollmentId = models.IntegerField()
    yearAndDept = models.CharField(max_length=16)
    sport = models.CharField(max_length=32)

class Complaints(models.Model):
    name = models.CharField(max_length=64)
    enrollmentId = models.IntegerField()
    yearAndDept = models.CharField(max_length=16)
    Complaint = models.CharField(max_length=164)