from django.shortcuts import render
from datetime import date

all_posts = [
    {   
        "slug" : "hike-in-the-mountains",
        "image" : "mountains.jpg",
        "author" : "Kastriot",
        "date" : date(2021, 8 , 1), 
        "title": "Mountain Hiking",
        "excerpt" : "DUMMY TEXT" ,
        "content" : "MORE DUMMY TEXT",
    }
]

def get_date(post):
    return post['date'] # or post.get('date')

# Create your views here.

def starting_page(request):
    sorted_posts = sorted(all_posts, key= get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts" : latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts" : all_posts
    })

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post" : identified_post
    })