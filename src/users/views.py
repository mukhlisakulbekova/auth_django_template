from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import views as auth_views

from users import forms
from users.models import User


# Create your views here.

class HomePageTemplateView(generic.TemplateView):
    template_name = 'index.html'


class UserCreatedView(generic.CreateView):
    model = User
    form_class = forms.UserCreatedForm
    template_name = "auth/register.html"
    success_url = reverse_lazy('login')


class UserLoginView(auth_views.LoginView):
    redirect_authenticated_user = True
    template_name = 'auth/login.html'
    next_page = 'home'


class UserLogoutView(auth_views.LogoutView):
    next_page = 'home'


class UserPasswordResetView(auth_views.PasswordResetView):
    template_name = 'auth/password_reset.html'
    next_page = 'password_reset_done'
    html_email_template_name = 'auth/message_to_email.html'


class UserPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'auth/password_reset_confirm.html'
    success_url = reverse_lazy("login")
