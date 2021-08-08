from django.shortcuts import render, get_object_or_404

from .models import Post

# Create your views here.


def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {
      "posts": latest_posts
    })


#reaching the posts from database

def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {
      "all_posts": all_posts
    })


#identified_post = next(post for post in all_posts if post['slug'] == slug)
    #right side of slug is the argument which is related to the slug above

def post_detail(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {
      "post": identified_post,
      "post_tags": identified_post.tags.all()
    })