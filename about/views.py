from django.shortcuts import render
from .models import Profile
# Create your views here.
def profile(request):
    """
    Renders the Profile page
    """
    profile = Profile.objects.all().order_by('updated_on').first
    
    return render(
    request,
    "about/profile.html",
    {"profile": profile},
)