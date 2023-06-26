from django.contrib.auth import forms
from users.models import User


class UserCreatedForm(forms.UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'username', 'phone', 'password1', 'password2')
