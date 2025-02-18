from rest_framework import generics, status
from rest_framework import viewsets

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User, Course, CourseContent

from .serializers import RegisterSerializer, LoginSerializer, CourseSerializer, CourseContentSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class LoginView(APIView):
    print('here')
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        user_data = {
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
        }
        return Response({'message': 'Login successful', 'user': user_data}, status=status.HTTP_200_OK)


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseContentViewSet(viewsets.ModelViewSet):
    queryset = CourseContent.objects.all()
    serializer_class = CourseContentSerializer
