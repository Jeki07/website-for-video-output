from django.shortcuts import render, redirect, get_object_or_404
from .models import Post_2
from .forms import *
from django.views.generic import DetailView
from mysite.settings import STATIC_ROOT
from django.contrib.auth import authenticate
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post_2, slug=post,
                                    publish__year=year,
                                    publish__month=month,
                                    publish__day=day)
    comments = post.comments.filter(active=True)
    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request,
                  'main/detail.html',
                 {'post': post,
                  'comments': comments,
                  'comment_form': comment_form})

class PostListView(ListView):
    queryset = Post_2.objects.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'main/list.html'


def contact(request):
    return render(request, 'main/contact.html')

def about(request):
    
    return render(request, 'main/about.html')

def login(request):
    return render(request, 'main/login.html')

        
