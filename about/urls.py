from django.urls import path
from . import views
import blog
from blog.views import CreatePost
 
urlpatterns = [
    path('profile/', views.profile, name='users-profile'),
    path('user/<str:username>/', views.UsersPostList.as_view(), name='users-blog-posts'),
    path('update-profile/', views.UpdateProfile, name ='update-profile'),
    path('delete-profile/', views.DeleteProfile, name ='delete-profile'),
    path('about-us/', views.AboutUs, name = 'about-us'),
    path('create-blog-post/', CreatePost, name ='create-blog-post'),
]