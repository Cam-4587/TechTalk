from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Profile
from .forms import UpdateProfileForm

# Create your views here.
@login_required
def profile(request):
    """
    Renders the Profile page
    """
    # Ensure the profile is fetched using the user relationship
    profile, created = Profile.objects.get_or_create(user=request.user)
    profile_form = UpdateProfileForm(instance=profile)
    
    if request.method == "POST":
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile has been created and is pending review')
            return redirect('users-profile')

    context =  {
        "profile": profile,
        "profile_form": profile_form,
        "profile_created": not created,
    }
    
    return render(request, "about/profile.html", context)



def UpdateProfile(request):
    """
    Updates the Users Profile
    """
    # Ensure the profile is fetched using the user relationship
    profile, created = Profile.objects.get_or_create(user=request.user)
    profile_form = UpdateProfileForm(instance=profile)

    if request.method == "POST":
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile has been updated successfully')
            return redirect('users-profile')

    context =  {
        "profile": profile,
        "profile_form": profile_form,
        "profile_created": not created,
    }
    
    return render(request, "about/profile_edit.html", context)

def DeleteProfile(request):
    """
    Deletes the Users Profile
    """
    profile, created = Profile.objects.get_or_create(user=request.user)
    profile_form = UpdateProfileForm(instance=profile)
    
    if request.method == "POST":
        profile.delete()
        return redirect('users-profile')
    return render(request, "about/profile_delete.html")


def AboutUs(request):
    return render(request, "about/about_us.html")


def profile_view(request, username=None):
    if username:
        user = get_object_or_404(User, username=username)
        profile = get_object_or_404(Profile, user=user)
    else:
        if request.user.is_authenticated:
            profile = request.user.profile
        else:
            raise Http404("User does not exist")

    return render(request, 'about/public_profile.html', {'profile': profile})


