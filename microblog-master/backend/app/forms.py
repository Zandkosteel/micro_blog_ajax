from django import forms
from backend.app.models import Post
from mptt.forms import TreeNodeChoiceField

class PostForm(forms.ModelForm):
    """"Форма добавление сообщения"""
    class Meta:
        model = Post
        fields = ("text", )
        widgets = {'text': forms.Textarea(attrs={'cols': 80, 'rows': 5, "class": "form-control"})}
        # widgets = {'text': forms.Textarea(attrs={"class": "form-control"})}
