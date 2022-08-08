from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Forms
class SignupForm(UserCreationForm):
    username = forms.CharField(
        label='Username',
        help_text='Letters, digits and @/./+/-/_ only.',
        widget=forms.TextInput(attrs={'type':'text'})
    )
    password1 = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )

    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2')
