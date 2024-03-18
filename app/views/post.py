from rest_framework import generics
from app.models import Post , PostLike , PostComment , UserFollow ,User 
from app.serializer import PostSerializer , CommentSerializer , UserFollowSerializer ,PostLikeSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView

class CreatePost(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class RetrivePost(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class RetrieveUserPosts(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def list(self, request, *args, **kwargs):
        user_posts = Post.objects.filter(user=request.user.id)
        print(user_posts)
        serializer = self.serializer_class(user_posts, many=True)
        return Response({ "success": True, "posts": serializer.data })


class RetrieveAllPosts(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UpdatePost(APIView):
    ueryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({ "success": True, "message": "updated post" })
        else:
            print(serializer.errors)
            return Response({ "success": False, "message": "error updating post" })
        

class DestroyPost(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    
    def destroy(self, request, *args, **kwargs):
        try:
            pk = kwargs.get("pk")
            post = Post.objects.get(id=pk)
            if post.user.id == request.user.id:
                self.perform_destroy(post)
                return Response({ "success": True, "message": "post deleted" })
            else:
                return Response({ "success": False, "message": "not enough permissions" })
        except ObjectDoesNotExist:
            return Response({ "success": False, "message": "post does not exist" })
        
class LikePostExist(APIView):
    queryset = Post.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PostLikeSerializer
    
    def get(self, request, pk):
        try:
            context = {
                "request": request,
            }
            like = Post.objects.get(id=pk)
            like = PostLike.objects.filter(post=like , user = request.user)
            print(like)
            serializer = self.serializer_class(like, many=True)
            return Response({"success": True, "is_liked": len(serializer.data)})


        except ObjectDoesNotExist:
            return Response({ "success": False, "message": "post does not exist" })


class LikePost(APIView):
    queryset = Post.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PostLikeSerializer

    def get(self, request, pk):
        try:
            context = {
                "request": request,
            }
            like = Post.objects.get(id=pk)
            like = PostLike.objects.filter(post=like)
            print(like)
            serializer = self.serializer_class(like, many=True)
            return Response({"success": True, "likes_count": len(serializer.data)})


        except ObjectDoesNotExist:
            return Response({ "success": False, "message": "post does not exist" })
        

    def post(self, request, pk):
        try:
            post = Post.objects.get(id=pk)
            like = PostLike.objects.filter(post=post, user=request.user)
            if like.exists():
                like.delete()
                return Response({"success": True, "message": "Post unliked successfully"})
            else:
                PostLike.objects.create(post=post, user=request.user)
                return Response({"success": True, "message": "Post liked successfully"})

        except ObjectDoesNotExist:
            return Response({"success": False, "message": "Post does not exist"})
        
class CommentPost(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            context = {
                "request": request,
            }
            post = Post.objects.get(id=pk)
            comments = PostComment.objects.filter(post=post)
            print(comments)
            serializer = self.serializer_class(comments, many=True)
            return Response({ "success": True, "comments": serializer.data })


        except ObjectDoesNotExist:
            return Response({ "success": False, "message": "post does not exist" })

    def post(self, request, pk):
        try:
            context = {
                "request": request,
            }
            post = Post.objects.get(id=pk)
            #  request.data["post"] = post
            #  PostComment.objects.create(post=post, user=request.user, comment_text=request.data["comment_text"])
            serializer = self.serializer_class(context=context, data=request.data)
            if serializer.is_valid():
                serializer.save(post=post)
                return Response({ "success": True, "message": "comment added" })
            else:
                print(serializer.errors)
                return Response({ "success": False, "message": "error adding a comment" })


        except ObjectDoesNotExist:
            return Response({ "success": False, "message": "post does not exist" })
        
class FollowUser(APIView):
    queryset = UserFollow.objects.all()
    serializer_class = UserFollowSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        following = UserFollow.objects.filter(user=request.user)
        followers = UserFollow.objects.filter(follows=request.user)

        following_serializer = UserFollowSerializer(following, many=True)
        followers_serializer = UserFollowSerializer(followers, many=True)
        return Response({ "success": True, "following": following_serializer.data, "followers": followers_serializer.data })


    def post(self, request, pk):
        try:
            following_user = User.object.get(id=pk)
            follow_user = UserFollow.objects.get_or_create(user=request.user, follows=following_user)
            if not follow_user[1]:
                follow_user[0].delete()
                return Response({ "success": True, "message": "unfollowed user" })
            else:
                return Response({ "success": True, "message": "followed user" })


        except ObjectDoesNotExist:
            return Response({ "success": False, "message": "following user does not exist" })
