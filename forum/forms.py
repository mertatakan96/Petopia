from django.forms import ModelForm
from .models import Forum, ForumComment

class ForumCreationForm(ModelForm):
    class Meta:
        model = Forum
        fields = ['forum_image', 'title', 'post']


class ForumEditForm(ModelForm):
    class Meta:
        model = Forum
        fields = ['forum_image', 'title', 'post']


class ForumCommentForm(ModelForm):
    class Meta:
        model = ForumComment
        fields = ['body']