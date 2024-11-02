from django.shortcuts import render
from.models import Profile
from .forms import UpdateProfileForm
# Create your views here.
def profile(request):
    """
    Renders the Profile page
    """
    profile = Profile.objects.all().order_by('updated_on').first
    profile_form = UpdateProfileForm()
    
    return render(
    request,
    "about/profile.html",
    {"profile": profile,
    "profile_form": profile_form},
)