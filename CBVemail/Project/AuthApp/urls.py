from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
urlpatterns=[
    path('login/',views.loginView,name='login'),
    path('register/',views.registerView,name='register'),
    path('out/',views.logoutView,name='logout'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='AuthApp/paasword_reset_form.html'),name='reset_password'),
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(template_name='AuthApp/password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='AuthApp/password_reset_confirm.html') ,name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='AuthApp/password_reset_complete.html'),name='password_reset_complete')


]