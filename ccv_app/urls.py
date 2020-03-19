from django.urls import include, path
from rest_framework import routers, serializers, viewsets
from .models import Post
from .views import postList
urlpatterns = [
    path('posts/', postList, name='postList'),
]