from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from .models import Post, Comment, Reply
from .forms import CommentForm
# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = "blog/index.html"
    paginate_by = 6  
    


def post_blog(request, slug):
    queryset = Post.objects.all()
    post = get_object_or_404(queryset, slug=slug)
    comment_form = CommentForm()
    
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
        return redirect('post_blog', slug=post.slug)
    else:
        comment_form = CommentForm()
    return render(
        request,
        "blog/post_blog.html",
        {"post": post,
        "comment_form": comment_form,
        },
    )