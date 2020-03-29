from django.urls import re_path, path
from .views import RegisterView
from django.contrib.auth import views as auth_views
from .forms import LoginForm

app_name = 'accounts'
urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/',  auth_views.LoginView.as_view(template_name="accounts/login.html", authentication_form=LoginForm), name="login"),
    path('logout/',  auth_views.logout_then_login, name="logout"),
]
