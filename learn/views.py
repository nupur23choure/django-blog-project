from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Post, Comment
from .forms import CommentForm

def post_list(request):
    posts = Post.objects.order_by('-created_at')
    paginator  = Paginator(posts, 4) 
    page_number = request.GET.get('page')
    post_page = paginator.get_page(page_number)
    return render(request, 'learn/post_list.html', {'posts': post_page})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    next_post = Post.objects.filter(id__gt=post.id).order_by('id').first()
    previous_post = Post.objects.filter(id__lt=post.id).order_by('-id').first()
    
    comments = Comment.objects.filter(post=post)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect('post_detail', id=post.id)
    else:
        comment_form = CommentForm()

    return render(request, 'learn/post_detail.html', {'post': post, 'next_post': next_post, 'previous_post': previous_post, 'comments': comments, 'comment_form': comment_form})
