from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('accounts/signup', views.signup, name='signup'),
    path('accounts/login',views.login,name='login'),
    path('accounts/logout',auth_views.LogoutView.as_view(),name='logout'),


]