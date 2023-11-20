from django.urls import path

from .views import LoginView, register, log_out, user_account_main_page, edit_user_profile

urlpatterns = [
    path('login/', LoginView),
    path('register', register),
    path('log-out', log_out),
    path('user', user_account_main_page),
    path('user/edit', edit_user_profile)
]
