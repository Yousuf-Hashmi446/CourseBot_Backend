from django.urls import path
from . import views

urlpatterns = [
    path('', views.abc),
    path('abc', views.index)
]
