from django.db import models

# Create your models here.
class Post(models.Model):
    post_id = models.IntegerField(unique=True)
    post_type_id = models.IntegerField()
    parent_id = models.IntegerField(null=True)
    creation_date = models.DateTimeField(null=True)
    score = models.IntegerField(null=True)
    body = models.TextField(max_length=10000, null=True)
    owner_user_id = models.IntegerField(null=True)
    last_editor_user_id = models.IntegerField(null=True)
    last_edit_date = models.DateTimeField(null=True)
    last_activity_date = models.DateTimeField(null=True)
    comment_count = models.IntegerField(null=True)



    

