from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    """Form for adding comments with Bootstrap styling and email field."""
    class Meta:
        model = Comment
        fields = ['name', 'email', 'comment']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'you@example.com'
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Your comment'
            }),
        }
        labels = {
            'name': 'Name',
            'email': 'Email',
            'comment': 'Comment',
        }
