from . import views
from django.urls import path 

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_blog, name='post_blog'),
    path('comment-sent/<slug:slug>/', views.comment_sent, name='comment-sent'),
    path('comment-delete/<uuid:pk>/<slug:slug>/', views.comment_delete, name='comment-delete'),
    path('reply-sent/<uuid:pk>/', views.reply_sent, name='reply-sent'),
]  