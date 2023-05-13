from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    PasswordResetForm,
    SetPasswordForm
)
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomBaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control cform'
            field.field.widget.attrs['placeholder'] = field.label


class CustomUserCreationForm(UserCreationForm, CustomBaseForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'country']


class CustomUserLoginForm(AuthenticationForm, CustomBaseForm):
    pass


class CustomUpdateForm(forms.ModelForm, CustomBaseForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'country']
        labels = {
            'first_name': 'Новое имя',
            'last_name': 'Новая фамилия',
            'country': 'Новая страна',
        }


class CustomPasswordResetForm(PasswordResetForm, CustomBaseForm):
    pass


class CustomSetPasswordForm(SetPasswordForm, CustomBaseForm):
    pass
