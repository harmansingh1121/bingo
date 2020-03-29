from django.urls import re_path, path
from .views import IndexView

app_name = 'game'
urlpatterns = [
    path('index/', IndexView.as_view(), name="index"),
]

