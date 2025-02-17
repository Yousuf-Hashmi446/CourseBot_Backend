from django.contrib.auth import authenticate

from rest_framework import serializers

from .models import User, Course, CourseContent


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data['email']
        password = data['password']
        user = authenticate(email=email, password=password)
        if user is None:
            try:
                user = User.objects.get(email=email)
                raise serializers.ValidationError("Incorrect password")
            except User.DoesNotExist:
                raise serializers.ValidationError("User does not exist")
        data['user'] = user
        return data


class CourseContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseContent
        fields = "__all__"
        read_only_fields = ['id', 'created_at', 'updated_at']


class CourseSerializer(serializers.ModelSerializer):
    contents = CourseContentSerializer(many=True, read_only=True, source='coursecontent_set')

    class Meta:
        model = Course
        fields = "__all__"
        read_only_fields = ['id', 'created_at', 'updated_at']
