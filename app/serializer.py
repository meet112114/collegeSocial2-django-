from rest_framework import serializers
from app.models import User , Post ,PostLike ,CO ,EE ,EJ , ME , IF , Sports ,Complaints
from app.models import LecturesCO , LecturesEE ,LecturesEJ ,LecturesIF ,LecturesME 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()
    bio = serializers.CharField()


    def create(self , validate_data):
        return User.object.create(**validate_data)
    

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

    title = serializers.CharField()
    description = serializers.CharField()
    image = serializers.ImageField()
    username = serializers.CharField()
    def update(self, instance, validated_data):
        if instance.user.id != validated_data.get("user").id:
            raise serializers.ValidationError("You are not allowed to modify this post.")

        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.image = validated_data.get("image", instance.image)
        instance.save()
        return instance
    
class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = "__all__"

    user = serializers.PrimaryKeyRelatedField(read_only=True)
    post = serializers.PrimaryKeyRelatedField(read_only=True)

class COSerializer(serializers.ModelSerializer):
    class Meta:
        model = CO
        fields = '__all__'

class IFSerializer(serializers.ModelSerializer):
    class Meta:
        model = IF
        fields = '__all__'

class MESerializer(serializers.ModelSerializer):
    class Meta:
        model = ME
        fields = '__all__'

class EESerializer(serializers.ModelSerializer):
    class Meta:
        model = EE
        fields = '__all__'

class EJSerializer(serializers.ModelSerializer):
    class Meta:
        model = EJ
        fields = '__all__'





class LectureSerializerIF(serializers.ModelSerializer):
    class Meta:
        model = LecturesIF
        fields = '__all__'

class LectureSerializerCO(serializers.ModelSerializer):
    class Meta:
        model = LecturesCO
        fields = '__all__'

class LectureSerializerME(serializers.ModelSerializer):
    class Meta:
        model = LecturesME
        fields = '__all__'

class LectureSerializerEE(serializers.ModelSerializer):
    class Meta:
        model = LecturesEE
        fields = '__all__'

class LectureSerializerEJ(serializers.ModelSerializer):
    class Meta:
        model = LecturesEJ
        fields = '__all__'

class SportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sports
        fields = '__all__'

class complaintSerializers(serializers.ModelSerializer):
    class Meta:
        model = Complaints
        fields = '__all__'