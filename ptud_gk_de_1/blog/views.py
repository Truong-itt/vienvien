from .forms import CommentForm
from .models import Post, Comment
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect


def layout1(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def layout2(request):
    posts = Post.objects.all()
    return render(request, 'blog/cardvased.html ', {'posts': posts})

def layout5(request):
    posts = Post.objects.all()
    return render(request, 'blog/sidebar.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        content = request.POST.get('content')
        Comment.objects.create(post=post, user=request.user, content=content)
        return redirect('post_detail', pk=post.pk)
    return render(request, 'blog/post_detail.html', {'post': post})




@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)  
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()

    comments = post.comments.all()
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'form': form})
