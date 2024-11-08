from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.utils.text import slugify
from .models import Post, Comment, Reply
from .forms import CommentForm, ReplyForm, CreateBlogPost
import about
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

def reply_sent(request, pk):
    comment= get_object_or_404(Comment, id=pk)
    post = comment.post
    
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid:
            reply = form.save(commit=False)
            reply.author = request.user
            reply.reply = comment            
            reply.save()
            return redirect('post_blog', slug=post.slug)
    return redirect('post_blog', slug=post.slug)

def reply_delete(request, pk):
    reply = get_object_or_404(Reply, id=pk, author=request.user)
    post = reply.reply.post

    if request.method == "POST":
        reply.delete()
        return redirect('post_blog', slug=post.slug)

    return render(request, 'blog/reply_delete.html', {'reply': reply, 'post': post})


def CreatePost(request):
    blogpost = CreateBlogPost()
    
    if request.method == 'POST':
        form = CreateBlogPost(request.POST)
        if form.is_valid():
            blogpost = form.save(commit=False)
            blogpost.author = request.user       
            blogpost.slug = slugify(Post.title)
            blogpost.save()
            form.save_m2m()
            return redirect('users-profile') 
    else: 
        form = CreateBlogPost()
    
    context = {
        'blogpost': blogpost
    }
    return render(request, 'blog/create_blog_post.html', context)


def post_delete(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == "POST":
        post.delete()
        return redirect('home')

    return render(request, 'blog/delete_blog_post.html', {'post': post})

def EditPost(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    if request.method == 'POST':
        form = CreateBlogPost(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateBlogPost(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form, 'post': post})

    


