from django.shortcuts import render
from .models import Post, Comment

# Create your views here.
# forum/views.py



def post_list(request):
    posts = Post.objects.all()
    return render(request, 'PawsitiveAdoptionHub/templates/forum/post_list.html', {'posts': posts})

# Add views for creating posts, adding comments, etc.
