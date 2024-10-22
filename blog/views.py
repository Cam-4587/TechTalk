from django.shortcuts import render
from django.views import generic
from django.shortcuts import render, get_object_or_404, reverse
from .models import Post 
# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = "blog/index.html"
    paginate_by = 6  
    


def post_blog(request, slug):
    queryset = Post.objects.all()
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/post_blog.html",
        {"post": post},
    )