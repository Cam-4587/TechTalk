from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.utils.text import slugify
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import about
import uuid
import requests
from .models import Post, Comment, Reply
from .forms import CommentForm, ReplyForm, CreateBlogPost

# Create your views here.


class PostList(generic.ListView):
    """ Display published blog posts on the home page"""
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6


def post_blog(request, slug):
    """ Display individual blog post with comment section at the bottom"""
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
    """ Sends comment form and redirects user back to blog post """
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.success(request, 'Comment added successfully')
            return redirect('post_blog', slug=post.slug)
    return redirect('post_blog', slug=post.slug)


def comment_delete(request, pk, slug):
    """ deletes comment and redirects user back to blog post """
    post = get_object_or_404(Post, slug=slug)
    comment = get_object_or_404(Comment, id=pk, author=request.user)

    if request.method == "POST":
        comment.delete()
        messages.success(request, 'Comment was deleted')
        return redirect('post_blog', slug=post.slug)

    return render(
        request, 'blog/comment_delete.html', {'comment': comment, 'post': post}
    )


def reply_sent(request, pk):
    """ Sends Reply form and redirects user back to blog post """
    comment = get_object_or_404(Comment, id=pk)
    post = comment.post

    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid:
            reply = form.save(commit=False)
            reply.author = request.user
            reply.reply = comment
            messages.success(request, 'Reply added successfully')
            reply.save()
            return redirect('post_blog', slug=post.slug)
    return redirect('post_blog', slug=post.slug)


def reply_delete(request, pk):
    reply = get_object_or_404(Reply, id=pk, author=request.user)
    post = reply.reply.post

    if request.method == "POST":
        reply.delete()
        messages.success(request, 'Reply deleted successfully')
        return redirect('post_blog', slug=post.slug)

    return render(
        request, 'blog/reply_delete.html', {'reply': reply, 'post': post}
    )


@login_required(login_url='home')
def CreatePost(request):
    """ Sends Post form and redirects user back to home page """
    blogpost = CreateBlogPost()

    if request.method == 'POST':
        form = CreateBlogPost(request.POST, request.FILES)
        if form.is_valid():
            blogpost = form.save(commit=False)
            blogpost.author = request.user
            blogpost.slug = slugify(blogpost.title)
            blogpost.save()
            form.save_m2m()
            messages.success(request, 'Post Submitted and awaiting approval')
            return redirect('home')
    else:
        form = CreateBlogPost()

    context = {
        'form': form
    }
    return render(request, 'blog/create_blog_post.html', context)


def post_delete(request, slug):
    """ Deletes blog post form and redirects user back to home page """
    post = get_object_or_404(Post, slug=slug)

    # Check if the current user is the author of the post
    if post.author != request.user:
        messages.error(
            request, 'You do not have permission to delete this post.')
        return redirect('home')

    if request.method == "POST":
        post.delete()
        return redirect('home')

    return render(request, 'blog/delete_blog_post.html', {'post': post})


def EditPost(request, slug):
    """ Edits Users blog post and redirects user back to their blog post """
    post = get_object_or_404(Post, slug=slug)

    # Check if the current user is the author of the post
    if post.author != request.user:
        messages.error(
            request, "You do not have permission to edit this post.")
        return redirect('home')

    if request.method == 'POST':
        form = CreateBlogPost(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateBlogPost(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form, 'post': post})
