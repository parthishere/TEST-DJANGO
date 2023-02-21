from django import forms
from django.contrib.auth import get_user_model


class UserProfileInfoForm(forms.Form):
    name = forms.CharField(max_length=20)
    email = forms.EmailField(label="Input Email", required=False)
    password = forms.CharField(widget=forms.PasswordInput)
    # class Meta():
    #     model = UserProfileInfo

    #     exclude = ('last_name',)


user = get_user_model()


class UserRegister(forms.Form):
    name = forms.CharField(max_length=20)
    email = forms.EmailField(label="Input Email", required=False)
    password = forms.CharField(widget=forms.PasswordInput)
