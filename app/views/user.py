from rest_framework import generics
from rest_framework.views import APIView
from app.serializer import UserSerializer , UserLoginSerializer
from app.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status


class CreateUser(generics.CreateAPIView):
    queryset = User.object.all()
    serializer_class = UserSerializer
      

class LoginUserView(APIView):
    
    def post(self , request):
        serializer = UserLoginSerializer(data = request.data)

        if serializer.is_valid():
            try:
                user = User.object.get(email = serializer.validated_data["email"])
                if user.password == serializer.validated_data["password"]:
                    token = Token.objects.get_or_create(user=user)
                    return Response({"success":True, "message":token[0].key})
                else:
                    return Response({"success":False , "message":"incorrect password"})

            except ObjectDoesNotExist:
                return Response({"success":False , "message":"User does not exists"})
                

class RetriveUser(generics.RetrieveAPIView):
    queryset = User.object.all()
    serializer_class = UserSerializer

class RetriveAllUser(generics.ListAPIView):
    queryset = User.object.all()
    serializer_class = UserSerializer


class UpdateUser(APIView):
    queryset = User.object.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    

    def put(self, request):
        serializer = self.serializer_class(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({ "success": True, "message": "user updated" })
        else:
            print(serializer.errors)
            return Response({ "success": False, "message": "error updating user" })

class DestroyUser(generics.DestroyAPIView):
    queryset = User.object.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def destroy(self, request, pk):
        try:
            # user = User.object.get(id = pk)
            if pk == request.user.id:
                self.perform_destroy(request.user)
                return Response({ "success": True, "message": " user deleted " })
            else:
                return Response({ "success": False, "message": " No Permissions " })
        
        except:
            return Response({"success":False , "message":"User does not exists"})