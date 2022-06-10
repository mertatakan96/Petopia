import uuid
from django.db import models
from users.models import User

class Blog(models.Model):
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    blog_image = models.ImageField(null=True, blank=True, upload_to='blogs/', default="dog1.jpg")
    title = models.CharField(max_length=200, null=True)
    post = models.TextField(max_length=7500, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.title) + " - " + str(self.owner)

    class Meta:
        ordering = ['-created']


class BlogComment(models.Model):
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, null=True, on_delete=models.CASCADE)
    body = models.TextField(max_length=120, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.blog) + " - " + str(self.owner)

    class Meta:
        ordering = ['created']




