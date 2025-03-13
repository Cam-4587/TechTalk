from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import generic
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from blog.models import Post
from .forms import UpdateProfileForm


# Create your views here.
class UsersPostList(LoginRequiredMixin, generic.ListView):
    """
    Displays the user's blog posts
    """
    template_name = "about/users_blog_posts.html"
    context_object_name = "posts"
    paginate_by = 6

    def get_queryset(self):
        # Get the username from the URL parameters
        username = self.kwargs['username']
        user = get_object_or_404(User, username=username)
        # Ensure only the author's posts are displayed
        return Post.objects.filter(author=user, status=1)

    def dispatch(self, request, *args, **kwargs):
        # Custom permission check
        username = self.kwargs['username']
        if request.user.username != username:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)



def profile(request):
    """
    Renders the Profile page
    """
    profile, created = Profile.objects.get_or_create(user=request.user)
    profile_form = UpdateProfileForm(instance=profile)

    if request.method == "POST":
        profile_form = UpdateProfileForm(
            request.POST, request.FILES, instance=profile
        )
        if profile_form.is_valid():
            profile_form.save()
            messages.success(
                request, 'Your profile has been created and is pending review'
            )
            return redirect('users-profile')

    context = {
        "profile": profile,
        "profile_form": profile_form,
        "profile_created": not created,
    }

    return render(request, "about/profile.html", context)


def UpdateProfile(request):
    """
    Updates the users Profile
    """
    profile, created = Profile.objects.get_or_create(user=request.user)
    profile_form = UpdateProfileForm(instance=profile)

    if request.method == "POST":
        profile_form = UpdateProfileForm(
            request.POST, request.FILES, instance=profile
        )
        if profile_form.is_valid():
            profile_form.save()
            messages.success(
                request, 'Your profile has been updated successfully'
            )
            return redirect('users-profile')

    context = {
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

    if request.method == "POST":
        profile.delete()
        return redirect('users-profile')

    return render(request, "about/profile_delete.html")


def AboutUs(request):
    """
    Displays the About us page
    """
    return render(request, "about/about_us.html")


def profile_view(request, username=None):
    """
    Displays the public profile of a user
    """
    if username:
        user = get_object_or_404(User, username=username)
        profile = get_object_or_404(Profile, user=user)
    else:
        if request.user.is_authenticated:
            profile = request.user.profile
        else:
            raise Http404("User does not exist")

    return render(request, 'about/public_profile.html', {'profile': profile})
