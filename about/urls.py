from django.urls import path
from . import views
 
urlpatterns = [
    path('profile/', views.profile, name='users-profile'),
    path('update-profile/', views.UpdateProfile, name ='update-profile')
]