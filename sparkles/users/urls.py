from django.urls import path

from .views import *

app_name = 'users'

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/<slug:username>/', ProfileView.as_view(), name='profile'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('update/<slug:username>', ProfileUpdateView.as_view(), name='update'),
    path('password_reset/', UserPasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', UserPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', UserPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
