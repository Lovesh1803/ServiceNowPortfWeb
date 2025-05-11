from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import (
    UserCreationForm, 
    AuthenticationForm, 
    SetPasswordForm as DjangoSetPasswordForm
)

User = get_user_model()

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ["username", "email", "phone", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.fields.values():
            f.widget.attrs.update({"class": "form-control"})

class SignInForm(AuthenticationForm):
    username = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={
        "class": "form-control",
        "placeholder": "you@example.com",
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "••••••••",
    }))

class SetPasswordForm(DjangoSetPasswordForm):
    # Used after user is already identified (e.g. via token)
    new_password1 = forms.CharField(label="New password",
        widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"••••••••"}))
    new_password2 = forms.CharField(label="Confirm password",
        widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"••••••••"}))
