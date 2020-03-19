from django.shortcuts import render
from .models import Post
import xml.etree.ElementTree as ET
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import filters
from rest_framework import serializers
from rest_framework import generics
from .serializers import PostSerializer

# Create your views here.
def parse_and_store_xml():
    tree = ET.parse('bioinformatics_posts_se.xml')
    root = tree.getroot()
    for row in root:
        post_dict = row.attrib
        post_id = post_dict["Id"]
        post_type_id = post_dict.get("PostTypeId")
        parent_id = post_dict.get("ParentId")
        creation_date = post_dict.get("CreationDate")
        score = post_dict.get("Score")
        body = post_dict.get("Body")
        owner_user_id = post_dict.get("OwnerUserId")
        last_editor_user_id = post_dict.get("LastEditorUserId")
        last_edit_date = post_dict.get("LastEditDate")
        last_activity_date = post_dict.get("LastActivityDate")
        comment_count = post_dict.get("CommentCount")
        post = Post(post_id=post_id, post_type_id=post_type_id, 
            parent_id=parent_id, creation_date=creation_date, score=score, body=body, 
            owner_user_id=owner_user_id, last_editor_user_id=last_editor_user_id,
            last_edit_date=last_edit_date, last_activity_date=last_activity_date,
            comment_count=comment_count)
        post.save()

@csrf_exempt
@api_view(['GET'])
def postList(request):
    sort_by = request.query_params.get('sort_by','creation_date')
    if sort_by not in ['score', 'comment_count']:
        sort_by = 'creation_date'

    posts = Post.objects.all().order_by('-'+str(sort_by))
    payload = {}   
    payload["posts"] = []
    for post in posts:
        post_dict = {}
        post_dict["Id"] = post.post_id
        post_dict["PostTypeId"] = post.post_type_id
        post_dict["ParentId"] = post.parent_id
        post_dict["CreationDate"] = post.creation_date
        post_dict["Score"] = post.score
        post_dict["Body"] = post.body
        post_dict["OwnerUserId"] = post.owner_user_id
        post_dict["LastEditorUserId"] = post.last_editor_user_id
        post_dict["LastEditDate"] = post.last_edit_date
        post_dict["LastActivityDate"] = post.last_activity_date
        post_dict["CommentCount"] = post.comment_count
        payload["posts"].append(post_dict)
    response = Response(payload, status=200)
    return response

class UserListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['body']