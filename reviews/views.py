from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post
from .forms import ReviewPostForm

# Create your views here.
def get_posts(request):
    """
    Create a view that returns reviews that have already been posted
    """
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    
    return render (request, "reviewposts.html", {'posts': posts})
    
def post_detail(request, pk):
    """
    Create a view to return a single review object based on the Post ID(pk)
    and render it to reviewdetails.html template or return a 404 error if no 
    post is found
    """
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    return render(request, "reviewdetails.html", {'post': post})

@login_required()  
def create_or_edit_post(request, pk=None):
    post = get_object_or_404(Post, pk=pk) if pk else None
    if request.method == "POST":
        form = ReviewPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect(post_detail, post.pk)
    else:
        form = ReviewPostForm(instance=post)
    return render(request, 'reviewforms.html', {'form': form})
    
    