import uuid
from django.db import models
from users.models import User

class Forum(models.Model):
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    forum_image = models.ImageField(null=True, blank=True, upload_to='forums/', default="dog1.jpg")
    title = models.CharField(max_length=200, null=True)
    post = models.TextField(max_length=750, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.title) + " - " + str(self.owner)

    class Meta:
        ordering = ['-created']


class ForumComment(models.Model):
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    forum = models.ForeignKey(Forum, null=True, on_delete=models.CASCADE)
    body = models.TextField(max_length=120, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.forum) + " - " + str(self.owner)

    class Meta:
        ordering = ['created']



