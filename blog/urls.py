from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_list, name='post_list'),  # tells Django that views.posts_list is the right place to go
    # views is a python file
    # post_list is a function in views
]
