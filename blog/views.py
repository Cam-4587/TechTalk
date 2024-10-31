from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from .models import Post, Comment, Reply
from .forms import CommentForm, ReplyForm
import uuid
# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = "blog/index.html"
    paginate_by = 6  
    


def post_blog(request, slug):
    queryset = Post.objects.all()
    post = get_object_or_404(queryset, slug=slug)
    comment_form = CommentForm()
    reply_form = ReplyForm()
   
    context = {
    "post": post,
    "comment_form": comment_form,
    "reply_form": reply_form,
    }
    
    return render(
        request,
        "blog/post_blog.html",
         context
    )
    
def comment_sent(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_blog', slug=post.slug)
    return redirect('post_blog', slug=post.slug)


def comment_delete(request, pk, slug):
    post = get_object_or_404(Post, slug=slug)
    comment = get_object_or_404(Comment, id=pk, author=request.user)

    if request.method == "POST":
        comment.delete()
        return redirect('post_blog', slug=post.slug)

    return render(request, 'blog/comment_delete.html', {'comment': comment, 'post': post})
