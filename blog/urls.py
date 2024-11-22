from django.urls import path
from . import views
from about.views import profile_view


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_blog, name='post_blog'),
    path('comment-sent/<slug:slug>/', views.comment_sent, name='comment-sent'),
    path(
        'comment-delete/<uuid:pk>/<slug:slug>/',
        views.comment_delete, name='comment-delete'
    ),
    path('reply-sent/<uuid:pk>/', views.reply_sent, name='reply-sent'),
    path('reply-delete/<uuid:pk>/', views.reply_delete, name='reply-delete'),
    path('post-delete/<slug:slug>/', views.post_delete, name='delete-post'),
    path('post-edit/<slug:slug>/', views.EditPost, name='edit-post'),
    path('profile/<str:username>/', profile_view, name="userprofile"),
]
