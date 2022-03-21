from django.contrib.auth.models import User
from django.forms import ModelForm


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', ]
