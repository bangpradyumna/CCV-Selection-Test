from django.urls import include, path
from rest_framework import routers, serializers, viewsets
from .models import Post
from .views import postList, UserListView

router = routers.DefaultRouter()

urlpatterns = [
    path('posts/', postList, name='postList'),
    path('search/', UserListView.as_view(), name='search-post') 
]