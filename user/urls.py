from django.urls import path
from django.contrib.auth import views as auth_views
from .import views
urlpatterns = [
    path('/signup',views.signup, name='signup'),
    path('home/',views.home),
    path('user/',views.executive,name='user'),
    path('reset_password/',auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset_password/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]