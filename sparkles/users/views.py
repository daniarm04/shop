from django.contrib.auth import login, get_user_model
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetCompleteView
)
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView

from . import forms

User = get_user_model()


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = forms.CustomUserLoginForm

    def get_success_url(self):
        return self.request.user.get_absolute_url()


class UserRegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = forms.CustomUserCreationForm

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.instance
        login(self.request, user)
        return response


class ProfileView(DetailView):
    model = User
    template_name = 'users/profile.html'
    context_object_name = 'user'
    slug_field = 'username'
    slug_url_kwarg = 'username'


class UserLogoutView(LogoutView):
    template_name = 'users/logout_success.html'


class ProfileUpdateView(UpdateView):
    model = User
    template_name = 'users/update.html'
    form_class = forms.CustomUpdateForm
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_success_url(self):
        return self.request.user.get_absolute_url()


class UserPasswordResetView(PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    form_class = forms.CustomPasswordResetForm
    success_url = reverse_lazy('users:password_reset_done')


class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'users/password_reset_confirm.html'
    form_class = forms.CustomSetPasswordForm
    success_url = reverse_lazy('users:password_reset_complete')


class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'users/password_reset_complete.html'
