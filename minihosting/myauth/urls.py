from .views import profile
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

app_name = "myauth"

urlpatterns = [
    path('login/', LoginView.as_view(template_name='myauth/login.html',
                                     redirect_authenticated_user=True),
         name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),

    ]