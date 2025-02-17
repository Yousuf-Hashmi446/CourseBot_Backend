from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import RegisterView, LoginView, CourseViewSet, CourseContentViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'course-contents', CourseContentViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('', include(router.urls)),
]
