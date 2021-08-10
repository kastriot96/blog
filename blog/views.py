from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from django.views import View

from .models import Comment, Post
from .forms import CommentForm

# Create your views here.

class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"


#writing to limit the number

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


#reaching the posts from database

class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"


#identified_post = next(post for post in all_posts if post['slug'] == slug)
    #right side of slug is the argument which is related to the slug above


class SinglePostView(View):
    def get(self,request, slug):
        post = Post.objects.get(slug=slug)
        context= {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments" : post.comments.all().order_by("-id")
        }
        return render(request, "blog/post-detail.html", context)

    def post(self, request, slug):
        post = Post.objects.get(slug=slug)
        #request.POST cotains the submited data
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment= comment_form.save(commit = False) #we can save since is based on model
            #post field in models !
            comment.post = post 
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page"), args=[slug])
        

        context= {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": comment_form,
            "comments" : post.comments.all().order_by("-id")
        }
        
        return render(request, "blog/post-detail.html", context)
