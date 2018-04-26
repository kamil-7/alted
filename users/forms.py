from django import forms

from users.models import User


class AvatarForm(forms.Form):
    avatar = forms.ImageField()


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password')

