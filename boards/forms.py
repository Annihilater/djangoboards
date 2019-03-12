from django import forms
from .models import Topic, Post


class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 5, "placeholder": "你的想法是什么?"}),
        max_length=4000,
        help_text="内容最长4000字。",
    )

    class Meta:
        model = Topic
        fields = ["subject", "message"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["message"]
