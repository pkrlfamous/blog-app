from django.views.generic import ListView, DetailView
# DetailView returns object we can use object.title to extract 
# title fo the database

#  and the ListView returns name  of the model i.e we post 
# and we can use post.title to extract title of the post

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']
    # Notice that in BlogUpdateView we are explicitly listing the fields we want to use
# ['title', 'body'] rather than using '__all__'. This is because we assume that the
# author of the post is not changing; we only want the title and text to be editable.

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
    
# We use reverse_lazy as opposed to just reverse so that it won’t execute 
# the URL redirect until our view has finished deleting the blog post.