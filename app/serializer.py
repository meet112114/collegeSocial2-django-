from rest_framework import serializers
from app.models import User , Post ,PostLike ,BCA , BSC , BBI , BMS , BAF , Sports ,Complaints
from app.models import LecturesBCA , LecturesBSC ,LecturesBBI ,LecturesBMS ,LecturesBAF 
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

class BCASerializer(serializers.ModelSerializer):
    class Meta:
        model = BCA
        fields = '__all__'

class BMSSerializer(serializers.ModelSerializer):
    class Meta:
        model = BMS
        fields = '__all__'

class BBISerializer(serializers.ModelSerializer):
    class Meta:
        model = BBI
        fields = '__all__'

class BSCSerializer(serializers.ModelSerializer):
    class Meta:
        model = BSC
        fields = '__all__'

class BAFSerializer(serializers.ModelSerializer):
    class Meta:
        model = BAF
        fields = '__all__'





class LectureSerializerBMS(serializers.ModelSerializer):
    class Meta:
        model = LecturesBMS
        fields = '__all__'

class LectureSerializerBCA(serializers.ModelSerializer):
    class Meta:
        model = LecturesBCA
        fields = '__all__'

class LectureSerializerBBI(serializers.ModelSerializer):
    class Meta:
        model = LecturesBBI
        fields = '__all__'

class LectureSerializerBSC(serializers.ModelSerializer):
    class Meta:
        model = LecturesBSC
        fields = '__all__'

class LectureSerializerBAF(serializers.ModelSerializer):
    class Meta:
        model = LecturesBAF
        fields = '__all__'

class SportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sports
        fields = '__all__'

class complaintSerializers(serializers.ModelSerializer):
    class Meta:
        model = Complaints
        fields = '__all__'