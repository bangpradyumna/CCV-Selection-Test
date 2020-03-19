from rest_framework import filters
from rest_framework import serializers
from rest_framework import generics
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['post_id', 'post_type_id', 'parent_id', 'creation_date', 'score', 'body', 'owner_user_id', 'last_editor_user_id', 'last_edit_date', 'last_activity_date', 'comment_count']
