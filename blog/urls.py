from . import views
from django.urls import path 

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_blog, name='post_blog'),
]  