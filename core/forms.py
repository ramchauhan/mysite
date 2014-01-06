from django.forms import ModelForm

from core.models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]
