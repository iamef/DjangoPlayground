from django.urls import path
from . import views

urlpatterns = [
    # views is a python file
    path("", views.post_list, name='post_list'),  # tells Django that views.posts_list is the right place to go
    # post_list is a function in views.py

    path('post/<int:pk>/', views.post_detail, name="post_detail"),
    # post_detail is a function is views.py

    path('post/new/', views.post_new, name='post_new')

]
