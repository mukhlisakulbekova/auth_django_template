from django.contrib.auth.views import PasswordResetDoneView
from django.urls import path
from users import views

urlpatterns = [
    path('', views.HomePageTemplateView.as_view(), name='home'),
    path('register/', views.UserCreatedView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('password-reset/', views.UserPasswordResetView.as_view(), name='password_reset'),

    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='auth/password_reset_done.html'),
         name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',views.UserPasswordResetConfirmView.as_view(),name='password_reset_confirm'),
]
