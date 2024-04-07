from django.urls import path, re_path
from .views import index


urlpatterns = [
    path('', index, name='home'),
    re_path(r'^(?P<path>.+?)/$', index),
]